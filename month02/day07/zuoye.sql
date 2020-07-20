create table students (
学号 int primary key auto_increment,
姓名 varchar(32),
年龄 tinyint unsigned,
性别 enum("m","w","o"),
籍贯 varchar(32));


create table course(
课程号 int primary key auto_increment,
课程名 varchar(32),
学分 int);

create table course_student(
id int primary key auto_increment,
sid int not null,
cid int not null,
CONSTRAINT student_fk FOREIGN KEY(sid) REFERENCES students(学号),
CONSTRAINT course_fk FOREIGN KEY(cid) REFERENCES course(课程号)
);


create table teachers(
教师号 int primary key auto_increment,
教师名 varchar(32),
职称 varchar(32),
年龄 tinyint unsigned,
c_id int unique,
constraint teach_fk foreign key(c_id) references course(课程号)
);



######朋友圈
create table 用户(
id int primary key auto_increment,
姓名 varchar(32),
密码 varchar(32),
电话 bigint
);


create table 发布(
id int primary key auto_increment,
图片 mediumblob,
内容 text,
时间 datetime default now(),
地点 varchar(32),
用户_id int,
CONSTRAINT 发布_fk FOREIGN KEY(用户_id) REFERENCES 用户(id)
);

create table 用户_发布(
id int primary key auto_increment,
评论 text,
点赞 int,
用户id int not null,
发布id int not null,
CONSTRAINT 用户_fk FOREIGN KEY(用户id) REFERENCES 用户(id),
CONSTRAINT 发布_fk FOREIGN KEY(发布id) REFERENCES 发布(id)
);


