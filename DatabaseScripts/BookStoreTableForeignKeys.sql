ALTER TABLE Customer
ADD ContactID int foreign key references Contact_Details(ContactID);

ALTER TABLE Author_of_the_books
ADD ContactID int foreign key references Contact_Details(ContactID);

ALTER TABLE Orders
ADD CustomerID int foreign key references Customer(CustomerID);

ALTER TABLE Books
ADD SupplierID int foreign key references Supplier(SupplierID);

ALTER TABLE Order_Items
ADD ISBN int foreign key references Books(ISBN);

ALTER TABLE Order_Items
ADD OrderID int foreign key references Orders(OrderID);

ALTER TABLE Supplier_Rep
ADD SupplierID int foreign key references Supplier(SupplierID);