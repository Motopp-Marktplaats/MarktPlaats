# voor de vorm van de data die in DB gaan opslaan
from app.db.dbAds import Base

from sqlalchemy import Column, Integer, String, Float


class Ad(Base):
    __tablename__ = 'advertenties'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    category = Column(String, nullable=False)
