from typing import List

from fastapi import APIRouter, Query

from app.schemas.metrics import RegionMetricOut, TopProductOut
from app.services.duckdb_service import fetch_metrics_by_region, fetch_top_products

router = APIRouter(tags=["Metrics"])


@router.get("/metrics/top-products", response_model=List[TopProductOut])
def top_products(limit: int = Query(5, ge=1, le=50)):
    return fetch_top_products(limit)


@router.get("/metrics/by-region", response_model=RegionMetricOut)
def metrics_by_region(region: str = Query(..., min_length=2, max_length=100)):
    return fetch_metrics_by_region(region)
