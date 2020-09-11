use encore;
SELECT * FROM customer;

SELECT name
FROM customer
WHERE address='seoul';

SELECT*
FROM book;

SELECT bookname
FROM book
ORDER BY bookname;

SELECT address
FROM customer 
GROUP BY address;

SELECT DISTINCT(address)
FROM customer;

SELECT COUNT(DISTINCT address) AS add_count 
FROM customer;

show tables;

SELECT*
FROM NewBook
order by PRICE;

SELECT AVG(price) AS 'avg. price of books'
FROM book;

SELECT COUNT(bookname) AS 'num of books'
FROM book;

SELECT COUNT(*) AS 'num of books'
FROM book;

SELECT*
FROM book;

SELECT COUNT(DISTINCT publisher) AS 'num of publisher'
FROM book;

SELECT publisher,COUNT(*) AS 'num of book', MAX(price) AS 'max price'
FROM book
GROUP BY publisher;

SELECT publisher, COUNT(*) AS 'num of book', MAX(price) AS 'max price'
FROM book
GROUP BY publisher 
HAVING COUNT(*) >=2;

select publisher from book;

SELECT COUNT(publisher) AS 도서수량
FROM book
WHERE price >=10000
GROUP by publisher
Having COUNT(*) >=2;

SELECT*
FROM orders, book;

SELECT*
FROM orders, book
WHERE orders.bookid=book.bookid
ORDER BY book.bookname;

SELECT*
FROM ORDERS;

SELECT*
FROM Orders O inner join book B
WHERE O.bookid = B.bookid
ORDER BY B.bookname;

SELECT customer.name, orders.bookid
FROM customer left outer join orders on customer.custid = orders.custid;

SELECT name, address

SELECT customer.name, book.bookname
FROM customer LEFT OUTER JOIN orders ON customer.custid = orders.custid;






