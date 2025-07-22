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

cursor.execute('''
    INSERT INTO Products (id, name, category, price)
    VALUES
    (1, 'Laptop', 'Electronics', 799.99),
    (2, 'Coffee Mug', 'Home Goods', 15.99),
    (3, 'Jarvis', 'AI Assistant', 2999.99)
''')
