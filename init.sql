-- Clinic Management Database Initialization
-- This file will be executed when the MySQL container starts for the first time

-- Set character set and collation
ALTER DATABASE clinic_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Create tables will be handled by Flask-SQLAlchemy migrations
-- This file is mainly for any initial data or database configuration

-- You can add any initial data here if needed
-- For example:
-- INSERT INTO users (username, email) VALUES ('admin', 'admin@clinic.com');