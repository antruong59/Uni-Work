-- Question One
-- Find the names of all the people who live in Tasmania
-- (2 Rows)
SELECT * FROM Addresses WHERE region = 'Tasmania' OR region = 'TAS';

-- Question Two
-- Using 2 different approaches show the names of all the customers who have yet to purchase anything
-- (1,005 Rows)

-- 1st way
SELECT  firstName, lastName
FROM Customers c LEFT OUTER JOIN CustomerOrders co 
ON c.customerID = co.customerID 
WHERE co.customerID IS NULL;

--2nd way
SELECT  firstName, lastName
FROM Customers c
WHERE c.customerID NOT IN (
	SELECT customerID
	FROM CustomerOrders);

-- Question Three
-- Find the names of all customers who have paid more than $500 on any item and the totalItemCost in a single customer order.  This includes purchases where more than one of the same item add up to more than $500
-- (551 Rows)

SELECT firstName, lastName
FROM Customers c 
JOIN CustomerOrders co 
ON c.customerID = co.customerID
JOIN ItemsInOrder iio
ON co.orderNumber = iio.orderNumber
--WHERE co.orderNumber IN (
	--SELECT orderNumber
	--FROM ItemsInOrder 
WHERE totalItemCost > 500;


-- Question Four
-- Altering your query from above find the item name, show how many of the item and what order it came from and whose name is attached to the order. Still limiting orders under $500 and sorting by last name and order number
-- (551 Rows)
SELECT firstName, lastName, itemName, numberOf, itemDescription
FROM Customers c 
JOIN CustomerOrders co 
ON c.customerID = co.customerID
JOIN ItemsInOrder iio
ON co.orderNumber = iio.orderNumber
JOIN Items i
ON i.itemID = iio.itemID
WHERE totalItemCost > 500
ORDER BY lastName ASC , iio.orderNumber;

-- Question Five
-- Using 2 different approaches find the last 5 items purchased, what are the differences?
-- (5 Rows)
SELECT itemID
FROM ItemsInOrder
JOIN CustomerOrders
ON 
WHERE endDate IN (
	SELECT TOP 5 * FROM ItemMarkupHistory 
	WHERE endDate IS NOT NULL
	ORDER BY endDate DESC);
--?

-- Question Six
-- Find all the suburbs that have brought anatomy items
-- (83 Rows)
SELECT DISTINCT suburb
FROM Addresses a
JOIN Customers c
ON a.addressID = c.addressID
JOIN CustomerOrders co 
ON c.customerID = co.customerID
JOIN ItemsInOrder iio
ON co.orderNumber = iio.orderNumber
JOIN Items i
ON i.itemID = iio.itemID
JOIN ItemCategories ic
ON i.categoryID = ic.categoryID
WHERE categoryName = 'Anatomy';



-- Question Seven
-- Show all the item categories and their subcategories, order the results by parent category name and then by the subcategory names.
-- (26 Rows)
SELECT* FROM ItemCategories

--1ST
SELECT ic.categoryName, result.categoryName
FROM ItemCategories ic
JOIN(
	SELECT *
	FROM ItemCategories
	WHERE parentCategoryID IN (
		SELECT categoryID
		FROM ItemCategories)
) AS result
ON ic.categoryID = result.parentCategoryID;

--2ND
SELECT ic.categoryName, result.categoryName
FROM ItemCategories ic
RIGHT OUTER JOIN (
	SELECT*
	FROM ItemCategories
	WHERE parentCategoryID IS NOT NULL) AS result
ON ic.categoryID = result.parentCategoryID;

SELECT par.categoryName, sub.categoryName 
FROM ItemCategories AS par
LEFT JOIN ItemCategories AS sub
ON par.parentCategoryID = sub.categoryID




-- Question Eight
-- Show the full name of the people, in one column, who created the last order. Also show the order number, the items in the order and how many of that item are in the order, finally the order date
-- (1 Row)

SELECT c.firstName, c.lastName, co.orderNumber, iio.numberOf, iio.itemID, i.itemName, co.orderDate

