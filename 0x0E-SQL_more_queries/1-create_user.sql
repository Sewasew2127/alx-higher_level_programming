-- script tp create MYSQL server user called user_od_1
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- query to grant perms to user
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost';
