CREATE TABLE IF NOT EXISTS orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL,
    total_amount NUMERIC(12, 2) NOT NULL
);

INSERT INTO orders (customer_id, total_amount) VALUES
(101, 125.50),
(102, 320.00),
(103, 89.99),
(104, 450.25),
(105, 219.75)
ON CONFLICT DO NOTHING;
