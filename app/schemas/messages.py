from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MessageCreate(BaseModel):
    receiver_id: int
    content: str
    ad_id: Optional[int] = None

class MessageOut(BaseModel):
    id: int
    sender_id: int
    receiver_id: int
    ad_id: Optional[int] = None
    content: str
    created_at: datetime

    class Config:
        from_attributes = True
