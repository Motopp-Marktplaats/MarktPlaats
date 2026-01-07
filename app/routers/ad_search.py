from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.db.database import get_db
from app.models.ads import Ad
from app.schemas.ads import AdOut

router = APIRouter(
    prefix="/ads",
    tags=["ads"]
)

@router.get("/search", response_model=List[AdOut])
def search_ads(
    category: Optional[str] = Query(None),
    search: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(Ad)

    if category:
        query = query.filter(Ad.category == category)

    if search:
        query = query.filter(Ad.title.ilike(f"%{search}%"))

    query = query.order_by(Ad.id.desc())

    return query.all()
