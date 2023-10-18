--  script that creates the MySQL server user user_0d_1.

SELECT 1 FROM mysql.user WHERE user = 'user_0d_1' LIMIT 1;
CREATE USER 'user_0d_1'@'%' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON * . * TO user_0d_1@localhost;
