
create table book(id int primary key auto_increment,
                书名 varchar(20) not null,
                作者 varchar(30) not null,
                出版社 varchar(30),
                价格 float default 0,
                备注 TEXT);
