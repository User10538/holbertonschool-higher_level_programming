-- This script create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- This script creates the MySQL server user user_0d_2.
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant select privileges to the user
GRANT SELECT PRIVILEGES ON *.* TO 'user_0d_2'@'localhost';
