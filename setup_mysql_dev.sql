-- this script prepares a mySQL server
IF NOT EXISTS CREATE DATABASE hbnb_dev_db;
IF NOT EXISTS CREATE USER 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL ON hbnb_dev_db TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema TO 'hbnb_dev'@'localhost';
