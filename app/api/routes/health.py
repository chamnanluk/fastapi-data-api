from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.services.postgres_service import fetch_db_health

router = APIRouter(tags=["Health"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def root():
    return {"message": "Welcome to the Sales Analytics API"}


@router.get("/health")
def health():
    return {"status": "ok"}


@router.get("/health/db")
def db_health(db: Session = Depends(get_db)):
    return {"database_ok": fetch_db_health(db)}
