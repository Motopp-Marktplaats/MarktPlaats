from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.core.deps import get_current_user
from app.schemas.messages import MessageOut
from app.db.db_messages import get_conversation
from app.models.user import User

router = APIRouter(prefix="/messages", tags=["messages"])

@router.get("/", response_model=List[MessageOut])
def read_conversation(
    with_user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_conversation(db, current_user.id, with_user_id, limit=100)
