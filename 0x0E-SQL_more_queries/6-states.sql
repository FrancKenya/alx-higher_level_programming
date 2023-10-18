--  a script that creates the database hbtn_0d_usa and the table states

-- Createse the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switches to the hbtn_0d_usa database
USE hbtn_0d_usa;

-- create it if it does not exist
CREATE TABLE IF NOT EXISTS states (
	id INT UNIQUE NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY(id)
);
