-- script to create a table for users
-- id, email, name
-- id is a primary key
-- email is unique
-- name is a string
-- country is an enum with values US, CO, TN

CREATE TABLE IF NOT EXISTS users (
	id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
	email varchar(255) NOT NULL UNIQUE,
	name varchar(255)
    country enum('US', 'CO', 'TN') DEFAULT 'US' NOT NULL
);
