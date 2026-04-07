from pydantic import BaseModel


class TopProductOut(BaseModel):
    product_name: str
    units_sold: int
    revenue: float


class RegionMetricOut(BaseModel):
    region: str
    total_units_sold: int
    total_revenue: float
