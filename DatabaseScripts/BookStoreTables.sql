CREATE TABLE Customer(
	CustomerID int identity(1, 1) primary key,
	First_Name varchar(40) not null,
	Last_Name varchar(40) not null
);

CREATE TABLE Author_of_the_books(
	AuthorID int identity(1, 1) primary key,
	First_Name varchar(40) not null,
	Last_Name varchar(40) not null,
	Gender varchar(20),
	Date_of_Birth date
);

CREATE TABLE Orders(
	OrderID int identity(1, 1) primary key,
	Order_Date date not null,
	Order_Value decimal(9,2)
);

CREATE TABLE Books(
	ISBN bigint primary key,
	Title varchar(100) not null,
	Publication_Date date not null,
	Price decimal(9,2) not null,
	User_Reviews varchar(100)
);

CREATE TABLE Order_Items(
	Item_Number int identity(1, 1) primary key,
	Item_Price decimal(9,2) not null,
);

CREATE TABLE Supplier(
	SupplierID int identity(1, 1) primary key,
	Supplier_Name varchar(40) not null
);

CREATE TABLE Book_Categories(
	Category_Code int identity(1, 1) primary key,
	Category_Desc varchar(100) not null
);

CREATE TABLE Contact_Details(
	ContactID int identity(1, 1) primary key,
);

CREATE TABLE Supplier_Rep(
	First_Name varchar(40) not null,
	Last_Name varchar(40) not null,
	Work_Number bigint,
	Cell_Number bigint,
	Email varchar(40),
	primary key(First_Name, Last_Name)
);
