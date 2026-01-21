from sqlalchemy.orm.session import Session

from app.models import user
from app.models.comments import DbComment
from app.schemas.comments import CommentBase
from fastapi import HTTPException
from app.models.ads import Ad
from sqlalchemy.orm import relationship


def create_comment(db: Session, request: CommentBase, user_id: int):
    new_comment = DbComment(
        comment=request.comment,
        create_by_id=user_id,
        sent_to_id=request.sent_to_id,
        advertisement_id = request.advertisement_id,
        date=request.date
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment

def read_all_comments(db:Session):
    return db.query(DbComment).all()

def read_comment(db:Session, id: int):
    return db.query(DbComment).filter(DbComment.id == id).first()

def read_other_users_comment(db:Session, id: int):
    return db.query(DbComment).filter(DbComment.sent_to_id == id).all()

def read_current_users_comment(db:Session, user_id= int):
    return db.query(DbComment).filter(DbComment.sent_to_id == user_id).all()

def read_advertensiment_comment(db: Session, advertisement_id: int):
    return (
        db.query(
            DbComment.id,
            DbComment.comment,
            DbComment.create_by_id,
            DbComment.sent_to_id,
            DbComment.date,

            Ad.id.label("advertisement_id"),
            Ad.title.label("advertisement_title"),
            Ad.description.label("advertisement_description"),
            Ad.price.label("advertisement_price"),
            Ad.status.label("advertisement_status"),
        )
        .join(Ad, DbComment.advertisement_id == Ad.id)
        .filter(DbComment.advertisement_id == advertisement_id)
        .all()
    )


def update_comment(db: Session, id: int, request: CommentBase, user_id=int):
    comment = db.query(DbComment).filter(DbComment.id == id, DbComment.create_by_id == user_id).first()
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    comment.comment = request.comment

    db.commit()
    db.refresh(comment)
    return comment

def delete_comment(db: Session, id: int, user_id=int):
    comment = db.query(DbComment).filter(DbComment.id == id, DbComment.create_by_id == user_id).first()
    try:
        db.delete(comment)
        db.commit()
    except:
        raise HTTPException(status_code=404, detail="Comment not found")
    return comment

