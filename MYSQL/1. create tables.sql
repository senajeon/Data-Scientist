-- Creat tables/primary key/foreign key/unique key 

CREATE DATABASE IF NOT EXISTS Sales;
CREATE TABLE sales
(
    purchase_number INT NOT NULL AUTO_INCREMENT,
    date_of_purchase DATE NOT NULL,
    customer_id INT,
    item_code VARCHAR(10) NOT NULL,
PRIMARY KEY (purchase_number),
FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE 
);

ALTER TABLE sales
DROP FOREIGN KEY sales_ibfk_1;

-- DROP TABLE sales, customers, items, companies;
-- DROP TABLE sales;
-- DROP TABLE customers;
-- DROP TABLE items;
-- DROP TABLE companies; 

USE sales;
CREATE TABLE customer (
	customer_id INT,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email_address VARCHAR(255),
    number_of_complaints INT,
PRIMARY KEY (customer_id),
UNIQUE KEY (email_address)
);

DROP TABLE customer;

CREATE TABLE customer (
	customer_id INT,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email_address VARCHAR(255),
    number_of_complaints INT,
PRIMARY KEY (customer_id)
);

ALTER TABLE customer
ADD UNIQUE KEY (email_address);


















