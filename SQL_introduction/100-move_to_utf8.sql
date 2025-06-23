USE hbtn_0c_0;

-- Convert database
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- Convert table
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Modify 'name' field without setting CHARACTER SET (only COLLATE)
ALTER TABLE first_table
MODIFY name VARCHAR(256)
COLLATE utf8mb4_unicode_ci;
