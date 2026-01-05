from pydantic import BaseModel
from datetime import date

class CommentBase(BaseModel):
    comment_id: int
    comment: str
    create_by_id: int
    sent_to_id: int
    date: date