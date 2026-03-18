from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.core.deps import get_current_user_from_token
from app.db.db_messages import create_message

router = APIRouter(tags=["messages-ws"])


class ConnectionManager:
    def __init__(self):
        self.active_connections: dict[int, WebSocket] = {}

    async def connect(self, user_id: int, websocket: WebSocket):
        await websocket.accept()
        self.active_connections[user_id] = websocket

    def disconnect(self, user_id: int):
        self.active_connections.pop(user_id, None)

    async def send_to_user(self, user_id: int, data: dict):
        ws = self.active_connections.get(user_id)
        if ws:
            await ws.send_json(data)


manager = ConnectionManager()


@router.websocket("/ws/messages")
async def ws_messages(websocket: WebSocket):
    db: Session = SessionLocal()
    current_user = None

    try:
        token = websocket.query_params.get("token")
        if not token:
            await websocket.close(code=1008)  # policy violation
            return

        # authenticate user
        current_user = get_current_user_from_token(token, db)


        await manager.connect(current_user.id, websocket)

        while True:
            payload = await websocket.receive_json()

            receiver_id = int(payload["receiver_id"])
            content = str(payload["content"])
            ad_id = payload.get("ad_id")

            msg = create_message(
                db=db,
                sender_id=current_user.id,
                receiver_id=receiver_id,
                content=content,
                ad_id=ad_id,
            )

            data_out = {
                "id": msg.id,
                "sender_id": msg.sender_id,
                "receiver_id": msg.receiver_id,
                "ad_id": msg.ad_id,
                "content": msg.content,
                "created_at": msg.created_at.isoformat(),
            }


            await manager.send_to_user(receiver_id, {"status": "new_message", "message": data_out})


            await websocket.send_json({"status": "sent", "message": data_out})

    except WebSocketDisconnect:
        pass
    except Exception as e:

        try:
            await websocket.close(code=1011)
        except Exception:
            pass
    finally:
        if current_user:
            manager.disconnect(current_user.id)
        db.close()
