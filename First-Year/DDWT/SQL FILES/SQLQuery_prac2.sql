--Question 1.	Find all the Items that cost less than $10
--13 rows
SELECT*FROM Items WHERE itemCost < 10;

--Question 2.	Find all the Customers who have an ‘a’ in their first name and an ‘l’ in their last name
--541 rows
SELECT*FROM Customers WHERE firstName LIKE '%a%' AND lastName LIKE '%l%';

--Question 3.	Find all the Customers who have a secondary phone number
--3726 rows
SELECT*FROM Customers WHERE NOT secondaryPhoneNumber IS NULL AND LEN(secondaryPhoneNumber) > 0;

--Question 4.	Find the five most expensive items
--5 rows
SELECT TOP 5 *FROM Items ORDER BY itemCost DESC;

--Question 5.	Find all the orders that were paid later than when they were ordered
--4716 rows
SELECT* FROM CustomerOrders WHERE datePaid > orderDate OR datePaid IS NULL;

--Question 6.	Find all the first names of our customers, removing any duplications
--676 rows
 SELECT DISTINCT firstName FROM Customers ORDER BY firstName ASC ; 
