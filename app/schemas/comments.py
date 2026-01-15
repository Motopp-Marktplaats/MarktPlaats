from pydantic import BaseModel
from datetime import date

class CommentBase(BaseModel):
    #id: int
    comment: str
    create_by_id: int # current_user = Depends(get_current_user)
    sent_to_id: int
    advertisement_id: int
    date: date

class CommentUpdate(BaseModel):
    #id: int
    comment: str
    #create_by_id: int # current_user = Depends(get_current_user)
    #sent_to_id: int
    #date: date

class CommentDisplay(BaseModel):
    id: int
    comment: str
    create_by_id: int
    sent_to_id: int
    advertisement_id: int
    date: date
    #advertisements: list = []

class CommentDisplayUpdate(BaseModel):
    #id: int
    comment: str
    #create_by_id: int
    sent_to_id: int
    date: date

    class Config:
        from_attributes = True


