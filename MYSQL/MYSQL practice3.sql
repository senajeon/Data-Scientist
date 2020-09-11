use encore;
-- join 

-- sub query: 가장 비싼 책은?
SELECT bookname
FROM book
WHERE price=(SELECT MAX(price) FROM book);

-- 도서를 구매한 적이 있는 고객의 이름은?
SELECT name
FROM customer
WHERE custid IN(SELECT custid FROM Orders)
Limit 3;

-- 태릉에서 출판한 도서를 구매한 고객의 이름은?
SELECT name 
FROM customer
WHERE custid IN(SELECT custid 
				FROM orders
				WHERE bookid IN (SELECT bookid
								FROM book
                                WHERE publisher = 'talng')); 

-- 선릉에서 출판한 도서를 구매한 고객의 이름은?
SELECT name 
FROM customer
WHERE custid IN(SELECT custid
				FROM orders
                WHERE bookid IN (SELECT bookid
								FROM book
                                WHERE publisher = 'sunlng'));
                                
-- 디자인에서 출판한 도서를 구마핸 고객의 이름은?
SELECT name
FROM customer
WHERE custid IN (SELECT custid
				FROM orders
                WHERE bookid IN (SELECT bookid
								FROM book
                                WHERE publisher ='design'));
                                
-- correlated subquery
-- 출판사별로 출판사의 평균 도서 가격보다 비싼 도서는? (not using GROUP BY)
SELECT b1.bookname
FROM book b1
WHERE b1.price > (SELECT avg(b2.price)
				 FROM book b2
                 WHERE b2.publisher =b1.publisher);

-- scalar subquery 
-- 고객별 판매수 검색 (결과는 고객이름과 고객별 판매액 출력)
SELECT (SELECT name from customer c WHERE c.custid = o.custid)'customer',
SUM(orderid) AS orders 
FROM orders o 
GROUP BY o.custid;

-- UNION/MINUS/INTERSECT - IN/NOT IN
-- 서웅에서 거주하는 고객의 이름과 도서를 주문한 고객의 이름
SELECT name
FROM customer
WHERE address LIKE 'seoul'
UNION
SELECT name 
FROM customer 
WHERE custid IN (SELECT custid FROM orders);

-- IN / NOT IN 
-- 부산에서 거주하는 고객의 이름에서 도서를 주문한 고객의 이름을 뺀 결과 NOT IN 연산자 사용
SELECT name
FROM customer
WHERE address LIKE 'busan' AND
	name NOT IN (SELECT name
				FROM customer
                WHERE custid IN(SELECT custid FROM orders));

-- 서울에서 거주하는 고객 중 도서를 주문한 고객의 이름 IN 연산자를 사용
SELECT name
FROM customer
WHERE address LIKE 'seoul' AND
	name IN (SELECT name
			FROM customer
            WHERE custid IN (SELECT custid FROM orders));
            
-- EXIST(한번이라도 주문한 고객이 있는지) / NOT EXIST
-- 주문이 있는 고객의 이름과 주소 (중복 없이) 
SELECT name, address
FROM customer cs
WHERE EXISTS (SELECT*
				FROM orders od
				WHERE cs.custid = od.custid);

-- 주문한 내역 다 출력(중복)
SELECT cs.name, cs.address
FROM customer cs, orders od
WHERE cs.custid = od.custid;

-- 주문한 내역 다 출력(중복)
SELECT cs.name, cs.address
FROM customer cs INNER JOIN orders od
WHERE cs.custid = od.custid;

-- 기존 테이블 복사 후 약간의 변경 줄때
CREATE table newCustomer(SELECT* FROM customer);

-- 기존 테이블 부분 열 복사
CREATE table newCustomer(SELECT name,custid FROM customer);

-- 복사 시 PK, FK 속상은 복사되지 않으므로 ALTER TABLE 명령으로 속성 부여
ALTER table newcustomer
ADD PRIMARY KEY('custid');



















