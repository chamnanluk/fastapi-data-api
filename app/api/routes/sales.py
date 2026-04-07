from fastapi import APIRouter

from app.schemas.sales import SalesQuery, SalesResponse
from app.services.postgres_service import simulate_sales_query

router = APIRouter(tags=["Sales"])


@router.post("/sales/query", response_model=SalesResponse)
def query_sales(payload: SalesQuery):
    return simulate_sales_query(payload)
