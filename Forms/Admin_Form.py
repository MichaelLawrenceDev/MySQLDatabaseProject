import pyodbc
from tkinter import *
from tkinter import messagebox
# Admin Form - What it should accomplish
#
#   1. View all customers
#   2. View orders    
#   3. View all Books    
#   4. View Suppliers
#   5. View Authors    
#   6. Update Customer Details   
#   7. Update Author Details
#   8. Update Book Details   
#   9. Remove customer/author/book/supplier from database

    
# Entry into Admin_Form.py and view all customer
def Start(admin_conn, username):
    # cursor should already be connected.
    print("Logging in as admin under username: " + username)
    cursor = admin_conn.cursor()
    root = Tk()
    root.title('Admin_Login')
    root.geometry('600x300')
    
    def View():
        def ViewCustomer():
            cursor.execute("select * from Customer")
            
        def ViewOrder():
            cursor.execute("select * from Orders")
            print(list(admin_cursor))

        def ViewBooks():
            cursor.execute("select * from Books")
            print(list(admin_cursor))

        def ViewSupplier():
            admin_cursor.execute("select * from Supplier")
            print(list(admin_cursor))

        def ViewAuthor():
            cursor.execute("select * from Author_of_the_books")
            print(list(admin_cursor))
        
        view1Button = Button(root, text="View Customers", command = ViewCustomer)
        view2Button = Button(root, text="View Orders", command = ViewOrder)
        view3Button = Button(root, text="View Books", command = ViewBooks)
        view4Button = Button(root, text="View Suppliers", command = ViewSupplier)
        view5Button = Button(root, text="View Authors", command = ViewAuthor)
        view1Button.place(x=100, y=30)
        view2Button.place(x=100, y=60)
        view3Button.place(x=100, y=90)
        view4Button.place(x=100, y=120)
        view5Button.place(x=100, y=150)
    

    def Update():
        def CustomerDetails():
            cursor.execute("update Customer set First_Name='" + First_Name +"', Last_Name='" + Last_Name +"', ContactID='" + ContactID +"', Username='" + Username +"' where CustomerID='"+ CustomerID +"'")
            print(list(admin_cursor))

        def AuthorDetails():
            cursor.execute("update Author_of_the_books set First_Name='" + First_Name +"', Last_Name='" + Last_Name +"', Gender='" + Gender +"', Date_of_Birth='" + Date_of_Birth +"', ContactID='" + ContactID +"' where AuthorID='"+ AuthorID +"'")
            print(list(admin_cursor))

        def BookDetails():
            cursor.execute("update Books set Title='" + Title +"', Publication_Date='" + Publication_Date +"', Price='" + Price +"', User_Reviews='" + User_Reviews +"' where ISBN='"+ ISBN +"'")
            print(list(admin_cursor))

    
        update1Button = Button(root, text="Update Author Details", command = AuthorDetails)
        update2Button = Button(root, text="Update Book Details", command = BookDetails)
        update1Button.place(x=200, y=30)
        update2Button.place(x=200, y=60)
    

    def Remove():
        
        def RemoveCustomer():
            CustomerID = y_CustomerID.get()
            First_Name = y_First_Name.get()
            Last_Name = y_Last_Name.get()
            ContactID = y_ContactID.get()
            Username = y_Username.get()
            Password = y_Password.get()
            cursor.execute("delete from Customer where CustomerID=='"+ y_CustomerID.get() +"'")
            cursor.execute('commit')

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
            cursor.execute("delete from Author_of_the_books where AuthorID=='"+ y_AuthorID.get() +"'")
            cursor.execute('commit')
        
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
            cursor.execute("delete from Books where ISBN=='"+ y_ISBN.get() +"'")
            cursor.execute('commit')
        
            y_ISBN.Remove(0, 'end')
            y_Title.Remove(0, 'end')
            y_Publication_Date.Remove(0, 'end')
            y_Price.Remove(0, 'end')
            y_User_Reviews.Remove(0, 'end')
            y_SupplierID.Remove(0, 'end')
        
        def RemoveSupplier():
            SupplierID = y_SupplierID.get()
            Supplier_Name = y_Supplier_Name.get()
            cursor.execute("delete from Supplier where SupplierID=='"+ y_SupplierID.get() +"'")
            cursor.execute('commit')
        
            y_SupplierID.Remove(0, 'end')
            y_Supplier_Name.Remove(0, 'end')


   
        remove1Button = Button(root, text="Remove Customer", command = RemoveCustomer)
        remove2Button = Button(root, text="Remove Author", command = RemoveAuthor)
        remove3Button = Button(root, text="Remove Book", command = RemoveBook)
        remove4Button = Button(root, text="Remove Supplier", command = RemoveSupplier)
        remove1Button.place(x=350, y=30)
        remove2Button.place(x=350, y=60)
        remove3Button.place(x=350, y=90)
        remove4Button.place(x=350, y=120)
    
    def disableButtons():
        viewButton['state'] = DISABLED
        updateButton['state'] = DISABLED
        removeButton['state'] = DISABLED

    def enableButtons():
        viewButton['state'] = ACTIVE
        updateButton['state'] = ACTIVE
        removeButton['state'] = ACTIVE

    viewButton = Button(root, text="View", command = View)
    viewButton.place(x=20, y=30)
    updateButton = Button(root, text="Update", command = Update)
    updateButton.place(x=20, y=60)
    removeButton = Button(root, text="Delete", command = Remove)
    removeButton.place(x=20, y=90)
