-- Set up MySQL development environment for project

-- Create a new database 'hbnb_dev_db'
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Switch to 'hbnb_dev_db'
USE hbnb_dev_db;

-- Create a new user 'hbnb_dev'
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant permissions on database 'hbnb_dev_db' to user 'hbnb_dev'
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant permissions on database 'performance_schema' to user 'hbnb_dev'
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
