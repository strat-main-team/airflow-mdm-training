-- staging table for raw records
CREATE TABLE IF NOT EXISTS ecommerce_customer_staging (
    source_system TEXT,
    customer_id TEXT,
    customer_unique_id TEXT,
    zip_code_prefix INTEGER,
    city TEXT,
    state TEXT
);

-- final master customer table
CREATE TABLE IF NOT EXISTS ecommerce_customer_master (
    master_customer_id UUID PRIMARY KEY,
    customer_unique_id TEXT,
    first_order_id TEXT,
    zip_code_prefix INTEGER,
    city TEXT,
    state TEXT,
    source_count INT,
    created_at TIMESTAMP DEFAULT NOW()
);
