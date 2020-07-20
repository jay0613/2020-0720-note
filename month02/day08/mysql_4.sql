--朋友圈作业练习示例
--用户表 存储用户信息
create table user(
id int primary key auto_increment,
name varchar(30),
passwd char(64)
);

--朋友圈表 存储朋友圈信息
create table pyq(
id int primary key auto_increment,
image blob,
content text,
time datetime,
user_id int,
foreign key(user_id) references user(id)
);

--点赞评论 可以看做是用户和朋友圈的多对多关系
create table user_pyq(
id int primary key auto_increment,
`like` bit default 0,
comment text default null,
u_id int,
p_id int,
foreign key(u_id) references user(id),
foreign key(p_id) references pyq(id)
);

--查询操作综合练习
--1. 查询每位老师教授的课程数量
select tname,count(teacher_id)
from teacher left join course
on teacher.tid=course.teacher_id
group by tname;

--2. 查询学生的信息及学生所在班级信息
select caption,sname,gender
from class inner join student
on class.cid = student.class_id;

--3. 查询各科成绩最高和最低的分数,
--形式 : 课程ID  课程名称 最高分  最低分
select cid,cname,max(number),min(number)
from score left join course
on score.course_id = course.cid
group by cid,cname;
--4. 查询平均成绩大于85分的所有学生学号,姓名和平均成绩
select stu.sid,sname,avg(number) as 平均分
from student as stu left join score
on stu.sid = score.student_id
group by stu.sid,sname
having avg(number) > 85;

--5. 查询课程编号为2且课程成绩在80以上的学生学号和姓名
select stu.sid,sname,number
from student as stu left join score
on stu.sid = score.student_id
where score.course_id=2 and number>80;


--6. 查询各个课程及相应的选修人数
select cname,count(course_id) as 选修人数
from course left join score
on course.cid = score.course_id
group by cname;

--修改视图
alter view good_student
as
select * from cls where score>85;

--对原有视图覆盖
create or replace view good_student
as
select * from cls where score>90;



--  ; --> $$  先改符号

--定义函数
def sql_fun:
   select .....from xxx;
   select .....from xxx;
   select .....from xxx;
$$  --函数定义完$$结尾

--   $$--->; 符号改回来


--函数 变量设置
delimiter $$
create function get_name2()
returns varchar(30)
begin
declare s varchar(30);
set s=(select name from class where id=1);
return s;
end $$
delimiter ;

--带参数的函数
delimiter $$
create function queryNameById(uid int)
returns varchar(20)
begin
return  (select name from cls where id=uid);
end $$
delimiter ;

--基本的存储过程 不带参数
delimiter $$
create procedure st()
begin
    select name,age from cls;
    select name,score from cls
    order by score desc;
end $$
delimiter ;


--存储过程  参数类型演示
delimiter $$
create procedure p_out ( OUT num int )
begin
    select num;
    set num=100;
    select num;
end $$
​
delimiter ;


#  3. 1编写一个函数，传入两个学生的ID，返回
     这两个学生成绩之差
delimiter $$
create function subtract(sid1 int,sid2 int)
returns int
begin
return (select max(score)-min(score) from class where id=sid1 or id=sid2);
end $$
delimiter ;

select subtract(1,10)

     2编写一个存储过程，传入一个学生姓名
     在外部得到这个学生的成绩


select max(score)-min(score) from class where id=1 or id=5;

