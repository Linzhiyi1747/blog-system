Use mysql;

# 在用户root下创建blog数据库和users表
CREATE SCHEMA `blog` DEFAULT CHARACTER SET utf8 ;
Use blog;
CREATE TABLE users (
    userid INT PRIMARY KEY, #是否生成id
    usernames VARCHAR(10) NOT NULL,
    passwords VARCHAR(16) NOT NULL #关于用户名密码长度和格式的限制问题
);

#创建用户work并授予blog数据库的所有权限
create user work identified by 'work1234';
grant all privileges on blog.* to 'work'@'%' ;
FLUSH PRIVILEGES;


#穿件用户
