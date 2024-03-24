--script to create a table for users
-- id, email, name
-- id is a primary key
-- email is unique

CREATE TABLE IF NOT EXISTS users (
	id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
	email varchar(255) NOT NULL UNIQUE,
	name varchar(255)
)
