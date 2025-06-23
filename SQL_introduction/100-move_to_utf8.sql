-- Select the database first
USE hbtn_0c_0;

-- Convert the database character set and collation
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the whole table's charset and collation
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Modify the column to remove explicit character set, only keep COLLATE
ALTER TABLE first_table
MODIFY name VARCHAR(256) COLLATE utf8mb4_unicode_ci;
