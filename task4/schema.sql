CREATE TABLE IF NOT EXISTS hierarchy (
    id INT PRIMARY KEY NOT NULL,
    uuid VARCHAR(32) NOT NULL,
    parent_id INT,
    FOREIGN KEY (parent_id) REFERENCES hierarchy(id)
);

CREATE TABLE IF NOT EXISTS nested_set (
    id INT PRIMARY KEY NOT NULL,
    uuid VARCHAR(32) NOT NULL,
    lft INT NOT NULL,
    rgt INT NOT NULL
);