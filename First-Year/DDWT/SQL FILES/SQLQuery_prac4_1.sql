--Question One
--Find the smallest markup applied to any item
SELECT MIN(markup) AS minMarkup FROM ItemMarkupHistory;

--Question Two
--Find the names of all items that the smallest markup applied to, and the date range it was applied.
--('from ' + CAST(startDate AS VARCHAR) + ' to ' + CAST(endDate AS VARCHAR)) AS dateRange
SELECT itemName, startDate, endDate, markup
FROM Items i JOIN ItemMarkupHistory imh
ON i.itemID = imh.itemID
WHERE markup = (SELECT MIN(markup) FROM ItemMarkupHistory);

--Question Three
--Find the total cost of each customer order
--SELECT * FROM ItemsInOrder;
SELECT orderNumber, SUM(totalItemCost) AS totalOrderCost
FROM ItemsInOrder 
GROUP BY orderNumber;

--Question Five
--Find the average cost of All orders
SELECT AVG(totalItemCost) AS averageCost FROM ItemsInOrder;

--Question Six
--Show the customer name and number of orders each customer has made grouping only by customerID.  Don’t forget to convert NULL to “0” and order the results by number of orders increasing
SELECT firstName, lastName, c.customerID, ISNULL(COUNT(orderNumber), 0) AS noOrder  
FROM Customers c LEFT JOIN CustomerOrders co
ON c.customerID = co.customerID
GROUP BY c.customerID, firstName, lastName 
ORDER BY noOrder ASC, lastName;

--Question Seven
--Show the names of each customer, how much each person has spent in total, and how many orders they have made.  Order your results by order count asc then by last name.
--SELECT * FROM ItemsInOrder
SELECT firstName, lastName, c.customerID, ISNULL(COUNT(DISTINCT co.orderNumber), 0) AS noOrder, ISNULL(SUM(totalItemCost), 0) AS totalSpent
FROM Customers c 
LEFT JOIN CustomerOrders co 
ON c.customerID = co.customerID
LEFT JOIN ItemsInOrder iio 
ON co.orderNumber = iio.orderNumber
GROUP BY c.customerID, firstName, lastName 
ORDER BY noOrder ASC, lastName;

--Question Eight
--Show the names of people who have made the most orders (ie different order numbers for a given customer).
SELECT firstName, lastName, noOrder
FROM Customers c JOIN (SELECT customerID, COUNT(orderNumber) AS noOrder FROM CustomerOrders GROUP BY customerID) AS result 
ON c.customerID = co.customerID 
WHERE noOrder = 
(SELECT MAX(noOrder) AS mostOrder 
FROM (SELECT COUNT(orderNumber) AS noOrder FROM CustomerOrders GROUP BY customerID) AS result );

--Question Nine
--Find the item category that has been purchased the most
SELECT * FROM ItemCategories
SELECT MAX(
SELECT COUNT(categoryID) AS noCat FROM (SELECT * FROM Items INTERSECT SELECT * FROM ItemsInOrder 