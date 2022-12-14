--Task 1.	View Questions:
--Question 1.	Create a view called “CustomerOrderSummary” that returns the customerID, number of different orders as “orderCount”, the totalValues of all orders as “totalSpent” and the total items purchased as “totalItems” for each customer.
CREATE VIEW CustomerOrderSummary AS 
SELECT customerID, COUNT(DISTINCT iio.orderNumber) AS orderCount, SUM(totalItemCost) AS totalSpent, SUM(numberOf) AS totalItems
FROM CustomerOrders co JOIN ItemsInOrder iio
ON co.orderNumber = iio.orderNumber
GROUP BY customerID

SELECT * FROM CustomerOrderSummary;



--Question 2.	Using the CustomerOrderSummary View Find the details of the customer who has spent the most on items?
SELECT * FROM CustomerOrderSummary WHERE totalSpent = (SELECT MAX(totalSpent) FROM CustomerOrderSummary);


--Question 3.	Create a view called “MonthlyOrderSummary” that returns the Month name as “orderMonth”, Year number as “orderYear”, the count of different customers that have made purchases as “customerCount”, the total cost of all the items sold as “totalCost”, across the different orders as “orderCount” and the total number of items sold as “itemsSold”
CREATE VIEW MonthlyOrderSummary AS
SELECT DATENAME(m, orderDate) AS orderMonth, DATEPART(yy, orderDate) AS orderYear, COUNT(DISTINCT co.customerID) AS customerCount, SUM(totalItemCost) AS totalCost, COUNT(DISTINCT iio.orderNumber) AS orderCount, SUM(numberOf) AS itemsSold
FROM CustomerOrders co JOIN ItemsInOrder iio 
ON co.orderNumber = iio.orderNumber
GROUP BY orderDate




--Question 4.	Using the MonthlyOrderSummary view, find the month and year with the highest sales value 
SELECT orderMonth, orderYear, totalCost FROM MonthlyOrderSummary WHERE totalCost = (SELECT MAX(totalCost) FROM MonthlyOrderSummary);



--Question 5.	Using the MonthlyOrderSummary view, find the month and year with the highest number of items sold
SELECT orderMonth, orderYear, itemsSold FROM MonthlyOrderSummary WHERE itemsSold = (SELECT MAX(itemsSold) FROM MonthlyOrderSummary);




 
--Question 6.	Create a view called “ItemSalesSummary” that returns the itemID, the order date month name as “orderMonth” , the order date year as an int called “orderYear”, the sum of the number of items purchased as “totalSold” and a count of the different orders where the item was purchased called “totalOrders”
CREATE VIEW ItemSalesSummary AS
SELECT itemID, DATENAME(m, orderDate) AS orderMonth, CAST(DATEPART(yy, orderDate) AS INT) AS orderYear, SUM(numberOf) AS totalSold, COUNT(DISTINCT iio.orderNumber) AS totalOrders
FROM CustomerOrders co JOIN ItemsInOrder iio
ON co.orderNumber = iio.orderNumber
GROUP BY orderDate, itemID







--Question 7.	Using the “ItemSalesSummary” view, list the items (name, description, cost), and the total sold in 2020 for any items that sold less units than the average number of units sold of all items in 2020
SELECT DISTINCT itemName, itemDescription, itemCost, totalSold 
FROM Items i JOIN ItemSalesSummary iss
ON i.itemID = iss.itemID
WHERE orderYear = 2020 AND totalSold < 
(SELECT AVG(totalSold) FROM Items i JOIN ItemSalesSummary iss
ON i.itemID = iss.itemID 
WHERE orderYear = 2020
)
ORDER BY totalSold;  




--Task 2.	Stored Procedure Questions:
--Question 1.	Create a stored procedure called “CustomerSearch” that accepts an optional firstName and lastName parameter.  The stored procedure should find all customers who’s first/lastname starts with the letters passed to the stored procedure and return results ordered by lastname then firstname ascending.  
--// don’t forget to test your procedure to see if it works with ‘a’ to return all customers with first names that start with ‘a’ then test with ‘a’, ‘r’ to see if it returns all customers who’s last name also starts with ‘r’!
CREATE PROCEDURE CustomerSearch2
@firstName VARCHAR(100),
@lastName VARCHAR(100)
AS
SELECT * FROM Customers 
WHERE (lastName LIKE @lastName + '%') OR (firstName LIKE @firstName + '%')
ORDER BY lastName, firstName

EXEC CustomerSearch2 'A', 'R'





--Question 2.	Create a stored procedure called “Customers_Insert” that accepts the firstName, lastName, email, main and secondary Phone numbers and returns the newly inserted customerID
SELECT * FROM Customers
ALTER PROCEDURE Customers_Insert
@firstName VARCHAR(100), 
@lastName VARCHAR(100), 
@email VARCHAR(100), 
@mainPhoneNumber VARCHAR(100), 
@secondaryPhoneNumber VARCHAR(100),
@customerID INT OUTPUT
AS 
INSERT INTO Customers(firstName, lastName, email, mainPhoneNumber, secondaryPhoneNumber)
VALUES (@firstName, @lastName, @email, @mainPhoneNumber, @secondaryPhoneNumber)
SELECT @customerID = SCOPE_IDENTITY()
RETURN

DECLARE @newcustomerID INT
EXEC Customers_Insert 'a', 'A', 'AA', 'AAA', 'AAAA', @customerID = @newcustomerID OUTPUT  

SELECT @newcustomerID




 
--Task 3.	Trigger Questions
--Question 1.	Add a new column to Customers called “dateLastEdit” that accepts a date value and allows null values



--Question 2.	Create a new Trigger “Customers_Edit” that updates the “dateLastEdit” column with the current date each time a new customer is added or an existing customer record is edited.
--// test that your trigger works by adding a new customer as well as editing the name of an existing customer





--Question 3.	[Optional – difficult!!!] 
--(A)	Add a new column called “totalValue” that is decimal(9,2).
--(B)	Create a new Trigger “CustomerPurchases_Calc” that updates the “totalValue” column in the CustomerOrders table each time a new purchase item is added to a customer order or an existing item is returned (removed from the order).



