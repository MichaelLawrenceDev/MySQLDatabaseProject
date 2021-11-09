CREATE TABLE Customer(
	CustomerID int primary key,
	First_Name varchar(40) not null,
	Last_Name varchar(40) not null
);

CREATE TABLE Author_of_the_books(
	AuthorID int primary key,
	First_Name varchar(40) not null,
	Last_Name varchar(40) not null,
	Gender bit,
	Date_of_Birth date
);

CREATE TABLE Orders(
	OrderID int primary key,
	Order_Date date not null,
	Order_Value decimal(9,2)
);

CREATE TABLE Books(
	ISBN int primary key,
	Title varchar(100) not null,
	Publication_Date date not null,
	Price decimal(9,2) not null,
	User_Reviews varchar(100)
);

CREATE TABLE Order_Items(
	Item_Number int primary key,
	Item_Price decimal(9,2) not null,
);

CREATE TABLE Supplier(
	SupplierID int primary key,
	Supplier_Name varchar(40) not null
);

CREATE TABLE Book_Categories(
	Category_Code int primary key,
	Category_Desc varchar(100) not null
);

CREATE TABLE Contact_Details(
	ContactID int primary key,
);

CREATE TABLE Supplier_Rep(
	First_Name varchar(40) not null,
	Last_Name varchar(40) not null,
	Work_Number int,
	Cell_Number int,
	Email varchar(40),
	primary key(First_Name, Last_Name)
);