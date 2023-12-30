CREATE TABLE IF NOT EXISTS hierarchy (
    id INT PRIMARY KEY NOT NULL,
    uuid VARCHAR(32) NOT NULL,
    parent_id INT,
    FOREIGN KEY (parent_id) REFERENCES hierarchy(id)
);
