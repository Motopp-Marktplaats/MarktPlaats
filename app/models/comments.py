import datetime
from app.db.database import Base

from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.core.deps import get_current_user as get_user

class DbComment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)  # uniqe id
    comment = Column(String(100), nullable=False)
    create_by_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    #user=relationship("users", back_populates="comments")

    sent_to_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    #receiver_id =relationship("users", back_populates="comments")

    advertisement_id = Column(Integer, ForeignKey("advertisements.id"), nullable=False)
    #ads =relationship('advertisements', back_populates="comments")

    date = Column(Date, default=datetime.date.today)
