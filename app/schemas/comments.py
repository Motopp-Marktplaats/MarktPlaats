from pydantic import BaseModel
from datetime import date
from typing import Optional


class CommentBase(BaseModel):
    #id: int
    comment: str
    #create_by_id: int # current_user = Depends(get_current_user)
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


class CommentDisplay_sent_to_id(BaseModel):
    id: int
    comment: str
    create_by_id: int
    sent_to_id: int
    advertisement_id: int
    date: date

    class Config:
        orm_mode = True

class CommentDisplay_current_user_to_id(BaseModel):
    id: int
    comment: str
    create_by_id: int
    #sent_to_id: int
    #advertisement_id: int
    date: date

    class Config:
        orm_mode = True

class AdvertisementOut(BaseModel):
    id: int
    title: str
    description: str

    class Config:
        orm_mode = True

class CommentWithAdvertisement(BaseModel):
    id: int
    comment: str
    create_by_id: int
    #sent_to_id: int
    date: date

    advertisement_id: int
    advertisement_title: str
    advertisement_description: Optional[str]
    advertisement_price: float
    advertisement_status: str

    class Config:
        orm_mode = True