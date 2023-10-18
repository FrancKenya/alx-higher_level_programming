--  a script that creates the database hbtn_0d_usa and the table states

-- Createse the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switches to the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Checks if the table states already exists in that data base
SELECT 1 FROM information_schema.tables WHERE table_name = 'states' LIMIT 1;

-- create it if it does not exist
CREATE TABLE IF NOT EXISTS states (
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
