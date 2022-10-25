-- create dev database and user
CREATE DATABASE IF NOT EXISTS arsual_data_base;
CREATE USER IF NOT EXISTS 'arsual'@'localhost' IDENTIFIED BY 'root';
GRANT USAGE ON *.* TO 'arsual'@'localhost';
GRANT ALL ON arsual_data_base.* TO 'arsual'@'localhost';
GRANT SELECT ON performance_schema.* TO 'arsual'@'localhost';
