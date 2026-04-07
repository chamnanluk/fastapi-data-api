from pydantic import BaseModel


class OrderOut(BaseModel):
    order_id: int
    customer_id: int
    total_amount: float
