from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox
import pyodbc
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
    
    def show():
        cursor = admin_conn.cursor()
        cursor.execute("select * from Customer")
        rows = cursor.fetchall()

        for row in rows:
            insertData = str(row[0])+ '   '+row[1]+'  '+row[2]+'  '+str(row[3])+' '+row[4]
            list.insert(list.size()+1, insertData)
            
    def Customer():
        update1Form = Toplevel(root)
        update1Form.title("Update Customer Details")
        update1Form.geometry("400x300")
        def closeupdate1Info():
            enableButtons()
            update1Form.destroy()

        CustomerIDLabel = Label(update1Form, text="CustomerID:")
        CustomerIDText = Entry(update1Form, width=25)
        First_NameLabel = Label(update1Form, text="First_Name:")
        First_NameText = Entry(update1Form, width=25)
        Last_NameLabel = Label(update1Form, text="Last_Name:")
        Last_NameText = Entry(update1Form, width=25)
        ContactIDLabel = Label(update1Form, text="ContactID:")
        ContactIDText = Entry(update1Form, width=25)
        UsernameLabel = Label(update1Form, text="Username:")
        UsernameText = Entry(update1Form, width=25)
        PasswordLabel = Label(update1Form, text="Password:")
        PasswordText = Entry(update1Form, width=25)
        
        CustomerIDLabel.place(x=20, y=50)
        CustomerIDText.place(x=200, y=50)
        First_NameLabel.place(x=20, y=80)
        First_NameText.place(x=200, y=80)
        Last_NameLabel.place(x=20, y=110)
        Last_NameText.place(x=200, y=110)
        UsernameLabel.place(x=20, y=140)
        UsernameText.place(x=200, y=140)
        PasswordLabel.place(x=20, y=170)
        PasswordText.place(x=200 ,y=170)
            
        def update1Info():
            CustomerID = CustomerIDText.get()
            First_Name = First_NameText.get()
            Last_Name = Last_NameText.get()
            #ContactID = ContactIDText.get()
            Username = UsernameText.get()
            Password = PasswordText.get()
            if(CustomerID=="" or First_Name=="" or Last_Name=="" or Username=="" ):
                MessageBox.showinfo('Update Status', 'All fields are required')
            else:
                cursor.execute("update Customer set First_Name='" + First_Name +"', Last_Name='" + Last_Name +"', Username='" + Username +"' where CustomerID='"+ CustomerID +"'")
                cursor.execute('commit')
        def remove1Info():
            CustomerID = CustomerIDText.get()
            First_Name = First_NameText.get()
            Last_Name = Last_NameText.get()
                #ContactID = ContactIDText.get()
            Username = UsernameText.get()
            Password = PasswordText.get()
            if (CustomerIDText.get() ==""):
                MessageBox.showinfo('Delete Status', 'CustomerID is compulsory for delete')
            else:
                cursor.execute("delete *from Customer where CustomerID=='"+ CustomerIDText.get() +"'")
                cursor.execute('commit')

            CustomerIDText.Remove(0, 'end')
            First_NameText.Remove(0, 'end')
            Last_NameText.Remove(0, 'end')
            #ContactIDText.Remove(0, 'end')
            UsernameText.Remove(0, 'end')
            PasswordText.Remove(0, 'end')
        update = Button(update1Form, text="Update", command = update1Info)
        update.place(x=200, y=250)
        remove = Button(update1Form, text="Remove", command = remove1Info)
        remove.place(x=300, y=250)

            
    def Orders():
        view2Form = Toplevel(root)
        view2Form.title("Order Details")
        view2Form.geometry("600x300")
        
        
    def Books():
        update3Form = Toplevel(root)
        update3Form.title("Book Details")
        update3Form.geometry("600x300")
        
        def closeupdate3Info():
            enableButtons()
            update3Form.destroy()

        ISBNLabel = Label(update3Form, text="ISBN:")
        ISBNText = Entry(update3Form, width=25)
        TitleLabel = Label(update3Form, text="Title:")
        TitleText = Entry(update3Form, width=25)
        Publication_DateLabel = Label(update3Form, text="Publication_Date:")
        Publication_DateText = Entry(update3Form, width=25)
        User_ReviewsLabel = Label(update3Form, text="User_Reviews:")
        User_ReviewsText = Entry(update3Form, width=25)
        
        ISBNLabel.place(x=20, y=50)
        ISBNText.place(x=200, y=50)
        TitleLabel.place(x=20, y=80)
        TitleText.place(x=200, y=80)
        Publication_DateLabel.place(x=20, y=110)
        Publication_DateText.place(x=200, y=110)
        User_ReviewsLabel.place(x=20, y=140)
        User_ReviewsText.place(x=200, y=140)
        
            
        def update3Info():
            ISBN =ISBNText.get()
            Title = TitleText.get()
            Publication_Date = Publication_DateText.get()
            Price = PriceText.get()
            User_Reviews = User_ReviewsText.get()
                
            if(ISBN=="" or Title=="" or Publication_Date=="" or Price=="" or User_Reviews=="" ):
                MessageBox.showinfo('Update Status', 'All fields are required')
            else:
                cursor.execute("update Books set Title='" + Title +"', Publication_Date='" + Publication_Date +"', Price='" + Price +"', User_Reviews='" + User_Reviews + "' where ISBN='"+ ISBN +"'")
                cursor.execute('commit')
        def remove3Info():
            ISBN = ISBNText.get()
            Title = TitleText.get()
            Publication_Date = Publication_DateText.get()
            Price = PriceText.get()
            User_Reviews = User_ReviewsText.get()
            SupplierID = SupplierIDText.get()
            
            if (ISBNText.get() == ""):
                MessageBox.showinfo('Delete Status', 'ISBN is compulsory for delete')
            else:
                cursor.execute("delete * from Books where ISBN=='"+ ISBNText.get() +"'")
                cursor.execute('commit')
        
            ISBNText.Remove(0, 'end')
            TitleText.Remove(0, 'end')
            Publication_DateText.Remove(0, 'end')
            PriceText.Remove(0, 'end')
            User_ReviewsText.Remove(0, 'end')
            SupplierIDText.Remove(0, 'end')
            MessageBox.showinfo('Delete Status', 'Record deleted!')
        update3 = Button(update3Form, text="Update", command = update3Info)
        update3.place(x=250, y=250)
        remove3 = Button(update3Form, text="Remove", command = remove3Info)
        remove3.place(x=350, y=250)
    
       

    def Suppliers():
        remove4Form = Toplevel(root)
        remove4Form.title("Supplier Details")
        remove4Form.geometry("600x300")
        SupplierIDLabel = Label(remove4Form, text="SupplierID:")
        SupplierIDText = Entry(remove4Form, width=25)
        Supplier_NameLabel = Label(remove4Form, text="Supplier Name:")
        Supplier_NameText = Entry(remove4Form, width=25)
        SupplierIDLabel.place(x=20, y=50)
        SupplierIDText.place(x=200, y=50)
        Supplier_NameLabel.place(x=20, y=80)
        Supplier_NameText.place(x=200, y=80)
        
        def remove4Info():
            
            SupplierID = SupplierIDText.get()
            Supplier_Name = Supplier_NameText.get()
            
            if (SupplierIDText.get() == ""):
                MessageBox.showinfo('Delete Status', 'SupplierID is compulsory for delete')
            else:
                cursor.execute("delete * from Supplier where SupplierID=='"+ SupplierIDText.get() +"'")
                cursor.execute('commit')
        
            SupplierIDText.Remove(0, 'end')
            Supplier_NameText.Remove(0, 'end')
            MessageBox.showinfo('Delete Status', 'Record deleted!')
            
        remove4 = Button(remove4Form, text="Remove", command = remove4Info)
        remove4.place(x=350, y=250)

    
    def Authors():
        update2Form = Toplevel(root)
        update2Form.title("Author Details")
        update2Form.geometry("600x300")
        def closeupdate2Info():
            enableButtons()
            update2Form.destroy()

        AuthorIDLabel = Label(update2Form, text="AuthorID:")
        AuthorIDText = Entry(update2Form, width=25)
        First_NameLabel = Label(update2Form, text="First_Name:")
        First_NameText = Entry(update2Form, width=25)
        Last_NameLabel = Label(update2Form, text="Last_Name:")
        Last_NameText = Entry(update2Form, width=25)
        GenderLabel = Label(update2Form, text="Gender:")
        GenderText = Entry(update2Form, width=25)
        Date_of_BirthLabel = Label(update2Form, text="Date_of_Birth:")
        Date_of_BirthText = Entry(update2Form, width=25)
           
        
        AuthorIDLabel.place(x=20, y=50)
        AuthorIDText.place(x=200, y=50)
        First_NameLabel.place(x=20, y=80)
        First_NameText.place(x=200, y=80)
        Last_NameLabel.place(x=20, y=110)
        Last_NameText.place(x=200, y=110)
        GenderLabel.place(x=20, y=140)
        GenderText.place(x=200, y=140)
        Date_of_BirthLabel.place(x=20, y=170)
        Date_of_BirthText.place(x=200, y=170)
        
            
        def update2Info():
            AuthorID =AuthorIDText.get()
            First_Name = First_NameText.get()
            Last_Name = Last_NameText.get()
            Gender = GenderText.get()
            Date_of_Birth = Date_of_BirthText.get()

            if(AuthorID=="" or First_Name=="" or Last_Name=="" or Gender=="" or Date_of_Birth=="" ):
                MessageBox.showinfo('Update Status', 'All fields are required')
            else:
                cursor.execute("update Author_of_the_Books set First_Name='" + First_Name +"', Last_Name='" + Last_Name +"', Gender='" + Gender +"', Date_of_Birth='" + Date_of_Birth + "' where AuthorID='"+ AuthorID +"'")
                cursor.execute('commit')
                
        def remove2Info():
            AuthorID =AuthorIDText.get()
            First_Name = First_NameText.get()
            Last_Name = Last_NameText.get()
            Gender = GenderText.get()
            Date_of_Birth = Date_of_BirthText.get()
            if (AuthorIDText.get() == ""):
                MessageBox.showinfo('Delete Status', 'AuthorID is compulsory for delete')
            else:
                cursor.execute("delete * from Author_of_the_books where AuthorID=='"+ AuthorIDText.get() +"'")
                cursor.execute('commit')
        
            AuthorIDText.Remove(0, 'end')
            First_NameText.Remove(0, 'end')
            Last_NameText.Remove(0, 'end')
            GenderText.Remove(0, 'end')
            Date_of_BirthText.Remove(0, 'end')
            ContactIDText.Remove(0, 'end')
            MessageBox.showinfo('Delete Status', 'Record deleted!')
        remove2 = Button(update2Form, text="Remove", command = remove2Info)
        remove2.place(x=200, y=250)
            
        update2 = Button(update2Form, text="Update", command = update2Info)
        update2.place(x=300, y=250)
        
    
    def CustomQuery():

        def submitQuery():
            query = []
            try:
                query = cursor.execute(textbox.get("1.0", END)).fetchall()
            except Exception as e:
                messagebox.showerror("Query Error", e)
            
            resultbox.configure(state='normal')
            resultbox.delete('1.0', END)
            print(query)
            for row in query:
                resultbox.insert(END, str(row) + "\n")
            resultbox.configure(state='disabled')
            admin_conn.commit()

        # Custom Query Form
        view5Form = Toplevel(root)
        view5Form.title("Query")

        textbox = Text(view5Form, height=15, width=100)
        resultbox = Text(view5Form, height=15, width=100)
        resultbox.configure(state='disabled')
        textbox.grid(row=0, column=0)
        resultbox.grid(row=4, column=0)

        submitButton = Button(view5Form, text="Execute", command=submitQuery)
        submitButton.grid(row=1, column=0)

        

    list = Listbox(root)
    list.place(x=150, y=20)
    
    # type indicates customer/books/ext...
    def updateRecords(table):
        list.delete(0, 'end')
        records = cursor.execute(f"select * from {table}").fetchall()

        # add records
        for row in records:
            insertData = ''
            for value in row:
                insertData += str(value) + '   '
            list.insert(list.size()+1, insertData)
            

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

    v1 = Button(root, text="Edit Customer", command = Customer)
    v1.place(x=500, y=20)

    #v2 = Button(root, text="Edit Orders", command = Orders)
    #v2.place(x=500, y=50)

    v3 = Button(root, text="Edit Books", command = Books)
    v3.place(x=500, y=60)

    v4 = Button(root, text="Edit Suppliers", command = Suppliers)
    v4.place(x=500, y=100)

    v5 = Button(root, text="Edit Authors", command = Authors)
    v5.place(x=500, y=140)

    list = Listbox(root, width=50)
    list.place(x=150, y=20)
    show()

    r1 = Button(root, text="Customer", command = lambda:updateRecords("Customer"))
    r1.place(x=20, y=20)

    r2 = Button(root, text="Orders", command = lambda:updateRecords("Orders"))
    r2.place(x=20, y=50)

    r3 = Button(root, text="Books", command = lambda:updateRecords("Books"))
    r3.place(x=20, y=80)

    r4 = Button(root, text="Suppliers", command = lambda:updateRecords("Supplier"))
    r4.place(x=20, y=110)

    r5 = Button(root, text="Authors", command = lambda:updateRecords("Author_of_the_books"))
    r5.place(x=20, y=140)

    r6 = Button(root, text="Custom Query", command = CustomQuery)
    r6.place(x=20, y=170)
