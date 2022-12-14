--Question One
--Show the names of people who have purchase the most goods (ie total number of items).
--Hint:
-- 1/ get the sum of numberOf for each customer
-- 2/ get the max of this sum
-- 3/ compare the sum of numberOf for each customer to the max and return the customerID
-- 4/ Join customerID from 3 to customer table to get the names.
SELECT firstName, lastName, totalItems
FROM Customers c JOIN
(SELECT customerID, SUM(numberOf) AS totalItems FROM (ItemsInOrder iio JOIN CustomerOrders co ON iio.orderNumber = co.orderNumber) GROUP BY customerID) AS Total
ON c.customerID = Total.customerID
WHERE totalItems = (SELECT MAX(totalItems) FROM (SELECT customerID, SUM(numberOf) AS totalItems FROM (ItemsInOrder iio JOIN CustomerOrders co ON iio.orderNumber = co.orderNumber) GROUP BY customerID) AS Total)

--Question Two
--Show the day, week day name, month name and year as individual columns of all orders that were made after January 1st, 2021. Show the month as the word month (January, February… etc) instead of the number value.
--For each day show the number of orders that were made for that day and the total number of items across all the orders. Show the date with the most orders first, for ties then order by the number of items from lowest to highest
--select orderDate from CustomerOrders

SELECT COUNT(co.orderNumber) AS totalOrder, SUM(numberOf) AS totalItems, DATEPART(d,orderDate) AS theDay, DATENAME(dw, orderDate) AS weekDayName, DATENAME(m, orderDate) AS monName 
FROM CustomerOrders co JOIN ItemsInOrder iio
ON iio.orderNumber = co.orderNumber
WHERE orderDate > ('2021-01-01')
GROUP BY orderDate
ORDER BY totalOrder DESC, totalItems DESC

--Question Three
--Ahh no, our front-end developer has set our order values to be Strings and the boss cannot generate his reports.
--We need to run a query that returns the order number, order date and paid date as strings whilst the total cost of the order can be a decimal type.  Dates should be in long format (Monday 15, Monthname Year).
SELECT CAST(co.orderNumber AS VARCHAR) AS orderNumber, CAST(DATENAME(dw, orderDate) AS VARCHAR) + ' ' + CAST(DATEPART(d,orderDate) AS VARCHAR) + ', ' +  CAST(DATENAME(m, orderDate) AS VARCHAR) + ' ' + CAST(DATEPART(yy,orderDate) AS VARCHAR) AS fullDate, totalItemCost
FROM CustomerOrders co JOIN ItemsInOrder iio
ON co.orderNumber = iio.orderNumber
GROUP BY orderDate, co.orderNumber, totalItemCost

--Question Four
--We need to find out who our whales are so we can send them advertising materials.
--Find out how much each person has spent in our stores.  If they have spent over $10000 label them a ‘goldmine’, for those who’ve spent over $1000 they’re a ‘big spender’, for over $500 they’re an ‘average spender’ and anyone else can be deemed ‘unworthy’
--// Hint
-- 1/ get the total spent for each customer 
-- 2/ merge the result with the customer table
-- 3/ convert the max numbers to words

SELECT firstName, lastName, totalCost,
(
CASE WHEN (totalCost > 10000)
THEN 'goldmine'

WHEN (totalCost > 1000)
THEN 'big spender'

WHEN (totalCost > 500)
THEN 'average spender'

ELSE
'unworthy'
END) AS customerLabel

FROM Customers c JOIN
(SELECT customerID, SUM(totalItemCost) AS totalCost FROM (ItemsInOrder iio JOIN CustomerOrders co ON iio.orderNumber = co.orderNumber) GROUP BY customerID) AS Total
ON c.customerID = Total.customerID


--Bonus Question - Hard
--Show how much each region has spent on houses. For those that spent nothing, remove the NULLs and replace it with 0.00. Order by the highest spent. 
select * from ItemCategories
SELECT region, SUM(totalItemCost) AS sumSpent
FROM Addresses a
LEFT JOIN Customers c
ON a.addressID = c.addressID
JOIN CustomerOrders co
ON c.customerID = co.customerID
JOIN ItemsInOrder iio
ON co.orderNumber = iio.orderNumber
JOIN Items i
ON iio.itemID = i.itemID
JOIN ItemCategories ic
ON i.categoryID = ic.categoryID
WHERE categoryName = 'House'
GROUP BY region



--Bonus Question – Fix
--If you ran the previous query you will note that region is a mix of abbreviations and full names.  Fix up the remaining regions by converting the full names to their corresponding abbreviations (eg, South Australia -> SA).  Can you work out how to do this using a single query?

