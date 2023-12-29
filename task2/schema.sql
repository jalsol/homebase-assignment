CREATE TABLE product (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(32) NOT NULL,
  description VARCHAR(1024) NOT NULL,
  price DECIMAL(12,3) NOT NULL,
  quantity_in_stock INT NOT NULL,
  type VARCHAR(32) NOT NULL
);

CREATE TABLE customer (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(32) NOT NULL,
  address VARCHAR(64) NOT NULL,
  phone_number VARCHAR(16) NOT NULL
);

CREATE TABLE purchase (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  date DATETIME NOT NULL,
  status VARCHAR(16) NOT NULL,
  customer_id BIGINT NOT NULL,
  FOREIGN KEY (customer_id) REFERENCES customer (id)
);

CREATE TABLE purchase_product (
  purchase_id BIGINT NOT NULL,
  product_id BIGINT NOT NULL,
  PRIMARY KEY (purchase_id, product_id),
  FOREIGN KEY (purchase_id) REFERENCES purchase (id),
  FOREIGN KEY (product_id) REFERENCES product (id)
);

CREATE TABLE inventory_transaction (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  date DATETIME NOT NULL,
  product_id BIGINT NOT NULL,
  quantity_change INT NOT NULL,
  FOREIGN KEY (product_id) REFERENCES product (id)
);
