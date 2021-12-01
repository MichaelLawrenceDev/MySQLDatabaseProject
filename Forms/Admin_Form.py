import pyodbc

# Admin Form - What it should accomplish
#
#   1. View all customers
#   2. View orders
def ViewOrder(admin_cursor, username):
    # cursor should already be connected.
    print("Logging in as admin under username: " + username)
    admin_cursor.execute("select * from Orders")
    print(list(admin_cursor))
    
#   3. View all Books
def ViewBooks(admin_cursor, username):
    # cursor should already be connected.
    print("Logging in as admin under username: " + username)
    admin_cursor.execute("select * from Books")
    print(list(admin_cursor))
    
#   4. View Suppliers
def ViewSupplier(admin_cursor, username):
    # cursor should already be connected.
    print("Logging in as admin under username: " + username)
    admin_cursor.execute("select * from Supplier")
    print(list(admin_cursor))
    
#   5. View Authors
def ViewAuthor(admin_cursor, username):
    # cursor should already be connected.
    print("Logging in as admin under username: " + username)
    admin_cursor.execute("select * from Author_of_the_books")
    print(list(admin_cursor))
    
#   6. Update Customer Details
def CustomerDetails(admin_cursor, username):
    # cursor should already be connected.
    print("Logging in as admin under username: " + username)
    admin_cursor.execute("update Customer set First_Name='" + First_Name +"', Last_Name='" + Last_Name +"', ContactID='" + ContactID +"', Username='" + Username +"' where CustomerID='"+ CustomerID +"'")
    print(list(admin_cursor))
    
#   7. Update Author Details
def AuthorDetails(admin_cursor, username):
    # cursor should already be connected.
    print("Logging in as admin under username: " + username)
    admin_cursor.execute("update Author_of_the_books set First_Name='" + First_Name +"', Last_Name='" + Last_Name +"', Gender='" + Gender +"', Date_of_Birth='" + Date_of_Birth +"', ContactID='" + ContactID +"' where AuthorID='"+ AuthorID +"'")
    print(list(admin_cursor))

#   8. Update Book Details
def BookDetails(admin_cursor, username):
    # cursor should already be connected.
    print("Logging in as admin under username: " + username)
    admin_cursor.execute("update Books set Title='" + Title +"', Publication_Date='" + Publication_Date +"', Price='" + Price +"', User_Reviews='" + User_Reviews +"' where ISBN='"+ ISBN +"'")
    print(list(admin_cursor))
    
#   9. Remove customer/author/book/supplier from database
def Remove(admin_cursor, username):
    print("Logging in as admin under username: " + username)
    
    def RemoveCustomer():
        CustomerID = y_CustomerID.get()
        First_Name = y_First_Name.get()
        Last_Name = y_Last_Name.get()
        ContactID = y_ContactID.get()
        Username = y_Username.get()
        Password = y_Password.get()
        admin_cursor.execute("delete from Customer where CustomerID=='"+ y_CustomerID.get() +"'")
        admin_cursor.execute('commit')

        y_CustomerID.Remove(0, 'end')
        y_First_Name.Remove(0, 'end')
        y_Last_Name.Remove(0, 'end')
        y_ContactID.Remove(0, 'end')
        y_Username.Remove(0, 'end')
        y_Password.Remove(0, 'end')
        y_CustomerID.Remove(0, 'end')
        
    def RemoveAuthor():
        AuthorID = y_AuthorID.get()
        First_Name = y_First_Name.get()
        Last_Name = y_Last_Name.get()
        Gender = y_Gender.get()
        Date_of_Birth = y_Date_of_Birth.get()
        ContactID = y_ContactID.get()
        admin_cursor.execute("delete from Author_of_the_books where AuthorID=='"+ y_AuthorID.get() +"'")
        admin_cursor.execute('commit')
        
        y_AuthorID.Remove(0, 'end')
        y_First_Name.Remove(0, 'end')
        y_Last_Name.Remove(0, 'end')
        y_Gender.Remove(0, 'end')
        y_Date_of_Birth.Remove(0, 'end')
        y_ContactID.Remove(0, 'end')
        
    def RemoveBook():
        ISBN = y_ISBN.get()
        Title = y_Title.get()
        Publication_Date = y_Publication_Date.get()
        Price = y_Price.get()
        User_Reviews = y_User_Reviews.get()
        SupplierID = y_SupplierID.get()
        admin_cursor.execute("delete from Books where ISBN=='"+ y_ISBN.get() +"'")
        admin_cursor.execute('commit')
        
        y_ISBN.Remove(0, 'end')
        y_Title.Remove(0, 'end')
        y_Publication_Date.Remove(0, 'end')
        y_Price.Remove(0, 'end')
        y_User_Reviews.Remove(0, 'end')
        y_SupplierID.Remove(0, 'end')
        
    def RemoveSupplier():
        SupplierID = y_SupplierID.get()
        Supplier_Name = y_Supplier_Name.get()
        admin_cursor.execute("delete from Supplier where SupplierID=='"+ y_SupplierID.get() +"'")
        admin_cursor.execute('commit')
        
        y_SupplierID.Remove(0, 'end')
        y_Supplier_Name.Remove(0, 'end')
       
# Entry into Admin_Form.py and view all customer
def Start(admin_cursor, username):
    # cursor should already be connected.
    print("Logging in as admin under username: " + username)
    admin_cursor.execute("select * from Customer")
    print(list(admin_cursor))
