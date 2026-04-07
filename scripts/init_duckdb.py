from pathlib import Path

import duckdb

DB_PATH = Path("analytics.duckdb")


def main():
    conn = duckdb.connect(str(DB_PATH))
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS product_metrics (
            product_name VARCHAR,
            region VARCHAR,
            units_sold INTEGER,
            revenue DOUBLE
        )
        """
    )

    conn.execute("DELETE FROM product_metrics")

    conn.executemany(
        "INSERT INTO product_metrics VALUES (?, ?, ?, ?)",
        [
            ("Rice", "Phnom Penh", 120, 2400.0),
            ("Rice", "Siem Reap", 80, 1600.0),
            ("Coffee", "Phnom Penh", 95, 2850.0),
            ("Coffee", "Battambang", 70, 2100.0),
            ("Tea", "Phnom Penh", 110, 1980.0),
            ("Tea", "Siem Reap", 60, 1080.0),
            ("Sugar", "Phnom Penh", 75, 1500.0),
            ("Sugar", "Battambang", 65, 1300.0),
        ],
    )
    conn.close()
    print(f"DuckDB initialized at {DB_PATH.resolve()}")


if __name__ == "__main__":
    main()
