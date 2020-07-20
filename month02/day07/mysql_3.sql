-- 练习1：使用book表
-- 1. 统计每位作家图书的平均价格
select author,avg(price) from book
group by author;

-- 2. 统计每个出版社出版图书的数量
select publication,count(title) from book
group by publication;

-- 3. 统计相同时间出版图书的平均价格
select publication_time,avg(price) from book
group by publication_time ;

-- 4. 查看总共有多少个出版社
select count(distinct publication) from book;

-- 5. 筛选出那些出版过超过50元图书的出版社，并按照其
-- 出版图书的平均价格进行降序排序
select publication,avg(price)
from book
group by publication
having max(price) > 50
order by avg(price) desc;





