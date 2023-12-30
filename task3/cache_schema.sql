CREATE TABLE IF NOT EXISTS cached_prop_info (
    id BIGINT PRIMARY KEY NOT NULL,
    address VARCHAR(255) NOT NULL,
    price VARCHAR(16) NOT NULL,
    price_ext VARCHAR(16),
    area VARCHAR(8) NOT NULL,
    area_ext VARCHAR(16),
    bedrooms_count INT,
    description TEXT NOT NULL,
    expired_at TIMESTAMP NOT NULL
);
