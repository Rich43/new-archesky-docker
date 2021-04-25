CREATE SCHEMA IF NOT EXISTS content;
USE content;
CREATE USER IF NOT EXISTS 'content'@'%' IDENTIFIED BY 'Password1';
GRANT SELECT, INSERT, UPDATE, DELETE ON content.content TO 'content'@'%';
GRANT SELECT, INSERT, DELETE ON content.content_revision TO 'content'@'%';
