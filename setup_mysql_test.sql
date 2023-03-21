-- Create test for MySQL setup

-- Create a new database 'hbnb_test_db'
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Switch to new database 'hbnb_test_db'
USE hbnb_test_db;

-- Create a new user 'hbnb_test'
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant permissions on database 'hbnb_test_db' to user 'hbnb_test'
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant permissions on database 'performance_schema' to user 'hbnb_test'
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
