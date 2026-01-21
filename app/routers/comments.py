from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.deps import get_current_user
from app.models.user import User
from app.schemas.comments import CommentBase, CommentDisplay, CommentUpdate, CommentDisplayUpdate
from app.db.database import get_db
from app.db import db_comment
from typing import List

router = APIRouter(
    prefix="/comments",
    tags=["comments"]
)
#Create comment endpoint
@router.post("/", response_model=CommentDisplay)
def create_comment(request: CommentBase, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db_comment.create_comment(db, request, current_user.id)

#Read all comments endpoint
@router.get("/", response_model= List[CommentDisplay])
def get_all_comments(db: Session = Depends(get_db)):
    return db_comment.read_all_comments(db)

#Read comment endpoint
@router.get("/{id}", response_model= CommentDisplay)  #user.id
def get_comment(id: int, db: Session = Depends(get_db)):
    return db_comment.read_comment(db, id)

#Update comment endpoint
@router.put("/{id}/update")  #user.id
def update_comment(id: int, request: CommentUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db_comment.update_comment(db, id, request, user_id=current_user.id)

#Delete comment endpoint
@router.delete("/{id}/delete")  #user.id
def delete_comment(id: int, db: Session = Depends(get_db)):
    return db_comment.delete_comment(db, id)

#Read another users comments /sent_to_id is another user
@router.get("/{id}", response_model= CommentDisplay)  #user.id
def get_comment(id: int, db: Session = Depends(get_db)):
    return db_comment.read_comment(db, id)

#Read another ads comments /ads_id is another ad
@router.get("/{id}", response_model= CommentDisplay)  #user.id
def get_comment(id: int, db: Session = Depends(get_db)):
    return db_comment.read_comment(db, id)

#Read another user comments about current user /sent_to_id is current_user_id
@router.get("/{id}", response_model= CommentDisplay)  #user.id
def get_comment(id: int, db: Session = Depends(get_db)):
    return db_comment.read_comment(db, id)
# @router.get("/ad/{ad_id}", response_model=List[CommentDisplay])
# def get_comments_by_ad(ad_id: int, db: Session = Depends(get_db)):
#     return db_comment.read_comments_by_ad(db, ad_id)