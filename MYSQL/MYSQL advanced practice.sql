use encore;

-- is null/in not null
SELECT sales +100
FROM profit
WHERE pro_id =6;

SELECT*
FROM profit;

SELECT*
FROM profit
WHERE sales is null;

SELECT*
FROM profit
WHERE sales ='';

-- ifnull
SELECT IFNULL(sales,'판매가격미정') sales, tax, sales_date
FROM profit;

-- customer 에서 고객번호, 이름, 전화번호를 앞의 두명만 보이시오. 
set@seq :=0;

SELECT(@seq := @seq +1) '순번', custid, name, phone
FROM customer
WHERE @seq < 3;

-- cast/convert
use encore;
SELECT avg(price) as '평균 도서 가격' from book;

SELECT cast(avg(price) as INT) as 'average.price' 
FROM book;

SELECT convert(avg(price), INT) as 'average price' 
FROM book;

SELECT IF(100>200, 'T', 'F') as '100>200';

SELECT ifnull(1uName0*20, NULL);

SELECT nullif(10*20, NULL);

SELECT nullif(10*20, 10*20);

SELECT*
FROM pivottest;

-- pivot table 
SELECT uName,
sum(if(season ='spring', amount,0)) as 'spring',
sum(if(season = 'summer', amount,0)) as 'summer',
sum(if(season = 'Fall', amount,0)) as 'Fall',
sum(if(season ='winter', amount,0)) as 'winter',
sum(amount) as 'sum'
FROM pivottest
GROUP BY uName;

-- View table 
-- Book 테이블에서 View 테이블 생성
-- 책 금액이 전체 평균 이상의 책을 보유한 춮판사 및 책이름, 책 아이디, 가격 출력

CREATE VIEW book
AS SELECT bookid, bookname, publisher, price
	FROM book 
	WHERE price > (SELECT AVG(price) FROM book) -- 부속질의어가 포함되어 있기때문에 view 오류
WITH CHECK OPTION;

SELECT * FROM book;

create or replace view order_view
as
select c.memberid as '고객 아이디', c.membername as '고객이름',
o.order_prod as '주문제품', o.order_amount as '주문수량'
from member c
inner join orders_p o
on c.memberid = o.order_cust;

create or replace view order_date
as
select* from orders_p
where order_date >'2020-09-12'
with check option;

insert into order_date values(6,7,'bb',125,'2020-09-14');
select*from order_date;
select*from orders_p;




