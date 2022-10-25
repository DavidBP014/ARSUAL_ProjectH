-- Create test database and user
CREATE DATABASE IF NOT EXISTS arsual_test_data_base;
CREATE USER IF NOT EXISTS 'arsual_test'@'localhost' IDENTIFIED BY 'root';
GRANT USAGE ON *.* TO 'arsual_test'@'localhost';
GRANT ALL ON arsual_test_data_base.* TO 'arsual_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'arsual_test'@'localhost';
