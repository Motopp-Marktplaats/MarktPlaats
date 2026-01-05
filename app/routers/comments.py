from fastapi import APIRouter, Depends, HTTPException
from requests import Session
from schemas import CommentBase
from db.database import get_db
from db import db_comment


router = APIRouter(
    prefix="/comments",
    tags=["comments"]
)

#create comment endpoint
@router.post("/")
def create_comment(request: CommentBase, db: Session = Depends(get_db)):
    return db_comment.create_comment(db, request)

#Read comment endpoint

#Update comment endpoint

#Delete comment endpoint