from typing import List

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.schemas.orders import OrderOut
from app.services.postgres_service import fetch_orders

router = APIRouter(tags=["Orders"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/orders", response_model=List[OrderOut])
def get_orders(
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db),
):
    return fetch_orders(db, limit)
