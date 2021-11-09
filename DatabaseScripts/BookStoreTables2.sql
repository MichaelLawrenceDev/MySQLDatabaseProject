CREATE TABLE CMail(
	Email varchar(40),
	ContactID int foreign key references Contact_Details(ContactID),
	primary key(Email, ContactID)
);

CREATE TABLE CAddress(
	Address varchar(100),
	ContactID int foreign key references Contact_Details(ContactID),
	primary key(Address, ContactID)
);

CREATE TABLE CNumber(
	Phone_Number int,
	ContactID int foreign key references Contact_Details(ContactID),
	primary key(Phone_Number, ContactID)
);

CREATE TABLE Assigned_to(
	ISBN int foreign key references Books(ISBN),
	Category_Code int foreign key references Book_Categories(Category_Code),
	primary key(ISBN, Category_Code)
);

CREATE TABLE Written_by(
	ISBN int foreign key references Books(ISBN),
	AuthorID int foreign key references Author_of_the_books(AuthorID),
	primary key(ISBN, AuthorID)
);