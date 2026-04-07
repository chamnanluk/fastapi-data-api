from typing import Optional

from pydantic import BaseModel, Field


class SalesQuery(BaseModel):
    country: str = Field(..., min_length=2, max_length=50)
    year: int = Field(..., ge=2000, le=2100)
    product: Optional[str] = None


class SalesResponse(BaseModel):
    country: str
    year: int
    total_sales: float
    currency: str
