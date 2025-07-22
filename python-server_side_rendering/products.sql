-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS Products;
USE Products;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (id),
    name VARCHAR(256) NOT NULL,
    price INT NOT NULL,
    category VARCHAR(256) NOT NULL,
);

INSERT INTO Products (id) VALUES (1), (2);
INSERT INTO Products (name) VALUES ("laptop"), ("Coffee Mug");
INSERT INTO Products (price) VALUES (799.99), (15.99);
INSERT INTO Products (category) VALUES (“Electronics”), (“Home Goods”);
