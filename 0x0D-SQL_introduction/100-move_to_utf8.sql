-- A script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.
-- Has to convert all of the following to UTF8:
-- Database hbtn_0c_0
-- Table first_table
-- Field name in first_table

-- Converting  the database to UTF8
ALTER DATABASE hbtn_0c_0
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- Converting the table to UTF8
ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- Converting the name field to UTF8
ALTER TABLE first_table
MODIFY name VARCHAR(256)
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

