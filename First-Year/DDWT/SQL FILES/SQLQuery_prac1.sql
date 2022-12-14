CREATE TABLE Addresses (
addressID	INT	IDENTITY NOT NULL,
addressLine	VARCHAR(100)	NOT NULL,
suburb	VARCHAR(50)	NOT NULL,
postcode	VARCHAR(10)	NOT NULL,
region	VARCHAR(50)	NOT NULL,
country	VARCHAR(50)	NOT NULL,
CONSTRAINT Addresses_PK PRIMARY KEY (addressID),
);

CREATE TABLE ItemCategories (
categoryID	INT	IDENTITY,
parentCategoryID	INT,
categoryName	VARCHAR(100) NOT NULL,
CONSTRAINT ItemsCat_PK PRIMARY KEY (categoryID),
CONSTRAINT xx FOREIGN KEY (parentCategoryID) REFERENCES ItemCategories(categoryID) 

);

--ON UPDATE CASCADE
--ON DELETE NO ACTION

CREATE TABLE Customers (
customerID	INT	IDENTITY, 
firstName	VARCHAR(100)	NOT NULL,
lastName	VARCHAR(100)	NOT NULL,
email	VARCHAR(100)	NOT NULL,
mainPhoneNumber	VARCHAR(15)	NOT NULL,
secondaryPhoneNumber	VARCHAR(15)	,
addressID	INT	,
CONSTRAINT Customers_PK PRIMARY KEY (customerID),
CONSTRAINT Customers_FK FOREIGN KEY (addressID) REFERENCES Addresses(addressID)
);

CREATE TABLE Items (
itemID	INT	IDENTITY NOT NULL, 
itemName	VARCHAR(150)	NOT NULL,
itemDescription	VARCHAR(MAX)	NOT NULL,
itemCost	DECIMAL(10,2)	NOT NULL,
itemImage	VARCHAR(MAX)	NOT NULL,
categoryID	INT	,
CONSTRAINT Items_PK PRIMARY KEY (itemID),
CONSTRAINT Items_FK FOREIGN KEY (categoryID) REFERENCES ItemsCategories(categoryID)
);

CREATE TABLE CustomerOrders (
orderNumber	INT	IDENTITY,
customerID	INT,
orderDate	DATE	DEFAULT GetDate(),
--totalValue	DECIMAL(10,2),
datePaid	DATE,	
CONSTRAINT CO_PK PRIMARY KEY (orderNumber),
CONSTRAINT CO_FK FOREIGN KEY (customerID) REFERENCES Customers(customerID)
);

CREATE TABLE ItemsInOrder (
orderNumber	INT,
itemID	INT	,
numberOf	INT	NOT NULL,
totalItemCost	Decimal(9,2),
CONSTRAINT IIO_PK PRIMARY KEY (orderNumber, itemID),
CONSTRAINT IIO_FK1 FOREIGN KEY (orderNumber) REFERENCES CustomerOrders(orderNumber),
CONSTRAINT IIO_FK2 FOREIGN KEY (itemID) REFERENCES Items(itemID)
);

CREATE TABLE Reviews (
reviewID	INT	IDENTITY, 
customerID	INT,
itemID	INT,
reviewDate	DATE	 NOT NULL DEFAULT GetDate(),
rating	INT	NOT NULL, 
reviewDescription	VARCHAR(MAX)	NOT NULL,
CONSTRAINT Reviews_PK PRIMARY KEY (reviewID),
CONSTRAINT Reviews_FK1 FOREIGN KEY (customerID) REFERENCES Customers(customerID),
CONSTRAINT Reviews_FK2 FOREIGN KEY (itemID) REFERENCES Items(itemID),
CONSTRAINT Reviews_UK UNIQUE (reviewDate, customerID, itemID),
CONSTRAINT Rating_Check CHECK (rating BETWEEN 1 AND 5)
);

CREATE TABLE ItemMarkupHistory (
itemID	INT	NOT NULL, 
startDate	Date	NOT NULL, 
endDate	Date,	
markup	Decimal(4,1)	Default 1.3 NOT NULL,
sale	Bit	Default 'False',
CONSTRAINT IMH_PK PRIMARY KEY (itemID, startDate),
CONSTRAINT IMH_FK FOREIGN KEY (itemID) REFERENCES Items(itemID)
);

SELECT*FROM Addresses;
SELECT*FROM CustomerOrders;
SELECT*FROM Customers;
SELECT*FROM ItemCategories;
SELECT*FROM Items WHERE itemCost < 10;
SELECT*FROM ItemsInOrder;
SELECT*FROM Reviews;



