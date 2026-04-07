from typing import List

import duckdb

from app.core.config import settings
from app.schemas.metrics import RegionMetricOut, TopProductOut


def fetch_top_products(limit: int) -> List[TopProductOut]:
    conn = duckdb.connect(settings.duckdb_path, read_only=True)
    try:
        query = """
            SELECT product_name, SUM(units_sold) AS units_sold, SUM(revenue) AS revenue
            FROM product_metrics
            GROUP BY product_name
            ORDER BY revenue DESC
            LIMIT ?
        """
        rows = conn.execute(query, [limit]).fetchall()

        return [
            TopProductOut(
                product_name=row[0],
                units_sold=int(row[1]),
                revenue=float(row[2]),
            )
            for row in rows
        ]
    finally:
        conn.close()


def fetch_metrics_by_region(region: str) -> RegionMetricOut:
    conn = duckdb.connect(settings.duckdb_path, read_only=True)
    try:
        query = """
            SELECT region, COALESCE(SUM(units_sold), 0) AS total_units_sold,
                   COALESCE(SUM(revenue), 0) AS total_revenue
            FROM product_metrics
            WHERE region = ?
            GROUP BY region
        """
        row = conn.execute(query, [region]).fetchone()

        if row is None:
            return RegionMetricOut(
                region=region,
                total_units_sold=0,
                total_revenue=0.0,
            )

        return RegionMetricOut(
            region=row[0],
            total_units_sold=int(row[1]),
            total_revenue=float(row[2]),
        )
    finally:
        conn.close()
