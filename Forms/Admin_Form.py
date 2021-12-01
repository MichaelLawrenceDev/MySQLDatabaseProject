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
    admin_cursor.execute("update Author_of_the_books set First_Name='" + First_Name +"', Last_Name='" + Last_Name +"', Gender='" + Gender +"', Date_of_Birth='" + Date_of_ Birth +"', ContactID='" + ContactID +"' where AuthorID='"+ AuthorID +"'")
    print(list(admin_cursor))

#   8. Update Book Details
def BookDetails(admin_cursor, username):
    # cursor should already be connected.
    print("Logging in as admin under username: " + username)
    admin_cursor.execute("update Books set Title='" + Title +"', Publication_Date='" + Publication_Date +"', Price='" + Price +"', User_Reviews='" + User_Reviews +"' where ISBN='"+ ISBN +"'")
    print(list(admin_cursor))
    
#   9. Remove customer/author/book/supplier from database
#

# Entry into Admin_Form.py
def Start(admin_cursor, username):
    # cursor should already be connected.
    print("Logging in as admin under username: " + username)
    admin_cursor.execute("select * from Customer")
    print(list(admin_cursor))
