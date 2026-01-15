from sqlalchemy.orm.session import Session
from app.models.comments import DbComment
from app.schemas.comments import CommentBase
from fastapi import HTTPException

def create_comment(db: Session, request: CommentBase):
    new_comment = DbComment(
        comment=request.comment,
        create_by_id=request.create_by_id,
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

def update_comment(db: Session, id: int, request: CommentBase):
    comment = db.query(DbComment).filter(DbComment.id == id).first()
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    comment.comment = request.comment

    db.commit()
    db.refresh(comment)
    return comment

def delete_comment(db: Session, id: int):
    comment = db.query(DbComment).filter(DbComment.id == id).first()
    try:
        db.delete(comment)
        db.commit()
    except:
        raise HTTPException(status_code=404, detail="Comment not found")
    return comment

