--script to create a table for users
-- id, email, name
-- id is a primary key
-- email is unique
-- name is not null

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
)
