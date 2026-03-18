from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.deps import get_current_user
from app.models.user import User
from app.schemas.comments import CommentBase, CommentDisplay, CommentUpdate, CommentDisplayUpdate, \
    CommentDisplay_sent_to_id, CommentWithAdvertisement, CommentDisplay_current_user_to_id
from app.db.database import get_db
from app.db import db_comment
from typing import List

router = APIRouter(
    prefix="/comments",
    tags=["comments"]
)
#Create comment endpoint
@router.post("/", response_model=CommentDisplay, summary="Create a new comment",
             description="""
             Creates a new comment for the currently authenticated user.

             Requirements:
             - User must be logged in.
             - The comment will automatically be linked to the logged-in user.

             
             Notes:
             - The user of the ad is determined from the JWT token.
             """)
def create_comment(request: CommentBase, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db_comment.create_comment(db, request, current_user.id)

#Read all comments endpoint
@router.get("/", response_model= List[CommentDisplay], summary="Read all comments",
             description="""
            Read all comments.
             Requirements:
             - User must be logged in.
             
            
             Notes:
             - The user is determined from the JWT token.
             """)
def get_all_comments(db: Session = Depends(get_db)):
    return db_comment.read_all_comments(db)


@router.get("/current_user_id", response_model= List[CommentDisplay_current_user_to_id])  #user.id
def get_comment(db: Session = Depends(get_db),    current_user: User = Depends(get_current_user)):
    return db_comment.read_current_users_comment(db, current_user.id)

#Read comment endpoint
@router.get("/{id}", response_model= CommentDisplay, summary="Read a comment with comment_id",
             description="""
             Read a comment with comment_id.

             Requirements:
             - User must be logged in.

           

             Notes:
             - The user of the ad is determined from the JWT token.
             """)  #user.id
def get_comment(id: int, db: Session = Depends(get_db)):
    return db_comment.read_comment(db, id)

#Update comment endpoint
@router.put("/{id}/update")  #user.id
def update_comment(id: int, request: CommentUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db_comment.update_comment(db, id, request, user_id=current_user.id)



#Delete comment endpoint
@router.delete("/{id}/delete")  #user.id
def delete_comment(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db_comment.delete_comment(db, id, user_id=current_user.id)




#Read another users comments /sent_to_id is another user
@router.get("/{id}/sent_to_id", response_model= List[CommentDisplay_sent_to_id], summary="Read a comment for other users with user_id",

            description=("\n"
                         "             Read other users comments with user_id.\n"
                         "             Requirements:\n"
                         "             - User must be logged in.\n"
                         "                        \n"
                         "\n"
                         "             Notes:\n"
                         "             - The user of the ad is determined from the JWT token.\n"
                         "             "))  #user.id
def get_comment_sent_to_id(id: int, db: Session = Depends(get_db)):
    return db_comment.read_other_users_comment(db, id)

#Read another ads comments /ads_id is another ad
@router.get("/{id}/advertensiment_id", response_model= List[CommentWithAdvertisement], summary="Read a advertensiments comment with adverstesement_id",

            description=("\n"
                         "             Read a advertensiment comment with ads_id.\n"
                         "             Requirements:\n"
                         "             - User must be logged in.\n"
                         "                        \n"
                         "\n"
                         "             Notes:\n"
                         "             - The user of the ad is determined from the JWT token.\n"
                         "             "))  #user.id
def get_comment_advertisement_id(    id: int,    db: Session = Depends(get_db)):
    return db_comment.read_advertensiment_comment(db, id)



#Read another user comments about current user /sent_to_id is current_user_id





# @router.get("/ad/{ad_id}", response_model=List[CommentDisplay])
# def get_comments_by_ad(ad_id: int, db: Session = Depends(get_db)):
#     return db_comment.read_comments_by_ad(db, ad_id)