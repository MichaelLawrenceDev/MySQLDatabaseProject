from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pyobc
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
     #cursor should already be connected.
    print("Logging in as admin under username: " + username)
    cursor = admin_conn.cursor()
    root = Tk()
    root.title('Admin_Login')
    root.geometry('600x300')

    def Customer():
        view1Form = Toplevel(root)
        view1Form.title("Customer Details")
        view1Form.geometry("600x300")
    def show():
        cursor = admin_conn.cursor()
        cursor.execute("select * from Customer")
        rows = cursor.fetchall()

        for row in rows:
            insertData = str(row[0])+ '   '+row[1]
            list.insert(list.size()+1, insertData)
            
    def Orders():
        view2Form = Toplevel(root)
        view2Form.title("Order Details")
        view2Form.geometry("600x300")
        cursor.execute("select * from Orders")
        print(list(cursor.execute))

    def Books():
        view3Form = Toplevel(root)
        view3Form.title("Book Details")
        view3Form.geometry("600x300")
        cursor.execute("select * from Books")
        print(list(cursor.execute))

    def Suppliers():
        view4Form = Toplevel(root)
        view4Form.title("Supplier Details")
        view4Form.geometry("600x300")
        cursor.execute("select * from Supplier")
        print(list(cursor.execute))

    def Authors():
        view5Form = Toplevel(root)
        view5Form.title("Author Details")
        view5Form.geometry("600x300")
        cursor.execute("select * from Author_of_the_books")
        print(list(cursor.execute))
    
    def CustomQuery():
        view5Form = Toplevel(root)
        view5Form.title("Query")
        view5Form.geometry("600x300")
        cursor.execute("select * from Author_of_the_books")
        print(list(cursor.execute))
    list = Listbox(root)
    list.place(x=150, y=20)
        
   



    def disableButtons():
        viewButton['state'] = DISABLED
        updateButton['state'] = DISABLED
        removeButton['state'] = DISABLED

    def enableButtons():
        viewButton['state'] = ACTIVE
        updateButton['state'] = ACTIVE
        removeButton['state'] = ACTIVE
        
    ViewText = Label(root, text="View")
    ViewText.place(x=20, y=0)

    record = Label(root, text="Records")
    record.place(x=150, y=0)

    add = Label(root, text="Add")
    add.place(x=500, y=0)

    v1 = Button(root, text="Edit", command = Customer)
    v1.place(x=500, y=20)

    v2 = Button(root, text="Edit", command = Orders)
    v2.place(x=500, y=50)

    v3 = Button(root, text="Edit", command = Books)
    v3.place(x=500, y=80)

    v4 = Button(root, text="Edit", command = Suppliers)
    v4.place(x=500, y=110)

    v5 = Button(root, text="Edit", command = Authors)
    v5.place(x=500, y=140)

    list = Listbox(root)
    list.place(x=150, y=20)
    show()

    r1 = Button(root, text="Customer", command = Customer)
    r1.place(x=20, y=20)

    r2 = Button(root, text="Orders", command = Orders)
    r2.place(x=20, y=50)

    r3 = Button(root, text="Books", command = Books)
    r3.place(x=20, y=80)

    r4 = Button(root, text="Suppliers", command = Suppliers)
    r4.place(x=20, y=110)

    r5 = Button(root, text="Authors", command = Authors)
    r5.place(x=20, y=140)

    r6 = Button(root, text="Custom Query", command = CustomQuery)
    r6.place(x=20, y=170)
