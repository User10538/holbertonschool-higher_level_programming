-- Set the database charset and collation
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Select the database
USE hbtn_0c_0;

-- Convert the table to utf8mb4
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Redefine the column, removing explicit charset
ALTER TABLE first_table
MODIFY name VARCHAR(256) COLLATE utf8mb4_unicode_ci DEFAULT NULL;
