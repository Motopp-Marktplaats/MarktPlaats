from sqlalchemy.orm import Session
from sqlalchemy import or_, and_
from app.models.messages import Message

def create_message(db: Session, sender_id: int, receiver_id: int, content: str, ad_id: int | None = None) -> Message:
    msg = Message(sender_id=sender_id, receiver_id=receiver_id, content=content, ad_id=ad_id)
    db.add(msg)
    db.commit()
    db.refresh(msg)
    return msg

def get_conversation(db: Session, user_a_id: int, user_b_id: int, limit: int = 50):
    return (
        db.query(Message)
        .filter(
            or_(
                and_(Message.sender_id == user_a_id, Message.receiver_id == user_b_id),
                and_(Message.sender_id == user_b_id, Message.receiver_id == user_a_id),
            )
        )
        .order_by(Message.created_at.asc())
        .limit(limit)
        .all()
    )
