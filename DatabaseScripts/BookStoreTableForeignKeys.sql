ALTER TABLE Customer
ADD FK_ContactID int foreign key 
references Contact_Details(ContactID)
ON DELETE SET NULL;

ALTER TABLE Author_of_the_books
ADD FK_ContactID int foreign key 
references Contact_Details(ContactID)
ON DELETE SET NULL;

ALTER TABLE Orders
ADD FK_CustomerID int foreign key
references Customer(CustomerID)
ON DELETE SET NULL;

ALTER TABLE Books
ADD FK_SupplierID int foreign key 
references Supplier(SupplierID)
ON DELETE SET NULL;

ALTER TABLE Order_Items
ADD FK_ISBN bigint foreign key 
references Books(ISBN)
ON DELETE SET NULL;

ALTER TABLE Order_Items
ADD FK_OrderID int foreign key 
references Orders(OrderID)
ON DELETE SET NULL;

ALTER TABLE Supplier_Rep
ADD FK_SupplierID int foreign key 
references Supplier(SupplierID)
ON DELETE SET NULL;;
