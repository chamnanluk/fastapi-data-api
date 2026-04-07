from typing import List

from sqlalchemy import text
from sqlalchemy.orm import Session

from app.schemas.orders import OrderOut
from app.schemas.sales import SalesQuery, SalesResponse


def fetch_db_health(db: Session) -> bool:
    result = db.execute(text("SELECT 1 AS ok"))
    row = result.fetchone()
    return bool(row.ok)


def fetch_orders(db: Session, limit: int) -> List[OrderOut]:
    query = text(
        """
        SELECT order_id, customer_id, total_amount
        FROM orders
        ORDER BY order_id DESC
        LIMIT :limit
        """
    )
    result = db.execute(query, {"limit": limit})
    rows = result.fetchall()

    return [
        OrderOut(
            order_id=row.order_id,
            customer_id=row.customer_id,
            total_amount=float(row.total_amount),
        )
        for row in rows
    ]


def simulate_sales_query(payload: SalesQuery) -> SalesResponse:
    base_sales = 250000.75
    if payload.product:
        base_sales += 15000.25

    return SalesResponse(
        country=payload.country,
        year=payload.year,
        total_sales=base_sales,
        currency="USD",
    )
