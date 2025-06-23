-- Set the database charset and collation
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Use the database
USE hbtn_0c_0;

-- Convert the table
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Remove column-level charset from `name` field
ALTER TABLE first_table
MODIFY name VARCHAR(256) COLLATE utf8mb4_unicode_ci DEFAULT NULL;
