--Question One
--Show the states that give the worst reviews (a rating less than 3) 
SELECT DISTINCT region
FROM Addresses a
JOIN Customers c
ON a.addressID = c.addressID
JOIN Reviews r
ON c.customerID = r.customerID
WHERE rating < 2;
--WHERE rating IN (
	--SELECT TOP 1 rating
	--FROM Reviews 
	--WHERE rating < 3
	--ORDER BY rating ASC
	--);

--Question Two
--Find the items that are categorised as novelty items. Display the item name and what sub-category the item is (i.e. don’t display the parent “novelty” category)
SELECT itemName, categoryName
FROM Items i
JOIN ItemCategories ic
ON i.categoryID = ic.categoryID 
WHERE categoryName = 'Novelty';

--Question Three
--Find all the orders that were made in the month of February regardless of the year (you may need to research this)
SELECT*
FROM CustomerOrders
WHERE DATEPART(MONTH, orderDate ) = 2;


--Question Four
--Find the details of customers who purchased more than three chicken harnesses in one order
SELECT *
FROM Customers c 
JOIN CustomerOrders co 
ON c.customerID = co.customerID
JOIN ItemsInOrder iio
ON co.orderNumber = iio.orderNumber
JOIN Items i
ON i.itemID = iio.itemID
WHERE itemName = 'Chicken Harness' AND numberOf = 3;

--Question Five
--Find the name and addresses of people who purchased decorations and also have a secondary phone number
SELECT* 
FROM Customers c
JOIN Addresses a
ON a.addressID = c.addressID
JOIN CustomerOrders co 
ON c.customerID = co.customerID
JOIN ItemsInOrder iio
ON co.orderNumber = iio.orderNumber
JOIN Items i
ON i.itemID = iio.itemID
JOIN ItemCategories ic
ON i.categoryID = ic.categoryID
WHERE categoryName = 'Decorations' AND secondaryPhoneNumber IS NOT NULL AND secondaryPhoneNumber <> ' ';


--Additional  Questions
--These Questions should not be undertaken unless you have fully completed all of this week’s questions. To complete these questions, you will have to do some research.

--Question One
--Find the total amount spent on all orders
SELECT SUM(totalItemCost) AS totalAmount FROM ItemsInOrder;

--Question Two
--Find the average cost of all items that have not been purchased by any customer
SELECT AVG(itemCost) AS averageCost FROM 
(SELECT i.itemCost 
FROM Items i LEFT OUTER JOIN ItemsInOrder iio
ON i.itemID = iio.itemID  
WHERE orderNumber IS NOT NULL) AS itemsNotPurchased;

--Question Three
--Calculate the number of people that live in South Australia
SELECT COUNT(customerID) AS CustomerCountSA FROM
(SELECT customerID, region
FROM Customers c
JOIN Addresses a
ON c.addressID = a.addressID
WHERE region IN ('South Australia', 'SA')) AS liveSA;

--Question Four – Hard!
--Find the name of all the people who have purchased more than a total of 10 items across all their orders.
SELECT firstName + ' ' + lastName AS fullName, sumNum, co.orderNumber
FROM Customers c
JOIN CustomerOrders co
ON c.customerID = co.customerID 
JOIN (SELECT SUM(numberOf) AS sumNum, orderNumber FROM ItemsInOrder GROUP BY orderNumber) AS result
ON co.orderNumber = result.orderNumber 
WHERE sumNum > 10
ORDER BY co.orderNumber;

--TEST
SELECT*FROM ItemsInOrder
SELECT SUM(numberOf) AS sumNum, orderNumber FROM ItemsInOrder GROUP BY orderNumber

SELECT firstName + ' ' + lastName AS fullName FROM Customers; 
SELECT CONCAT(NULL, lastName) FROM Customers; -- Enable to add NULL with values