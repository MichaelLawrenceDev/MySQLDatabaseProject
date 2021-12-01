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
            view1Form = Toplevel(root)
            view1Form.title("Customer Details")
            view1Form.geometry("600x300")
            cursor.execute("select * from Customer")
            
        def ViewOrder():
            view2Form = Toplevel(root)
            view2Form.title("Order Details")
            view2Form.geometry("600x300")
            cursor.execute("select * from Orders")
            print(list(cursor.execute))

        def ViewBooks():
            view3Form = Toplevel(root)
            view3Form.title("Book Details")
            view3Form.geometry("600x300")
            cursor.execute("select * from Books")
            print(list(cursor.execute))

        def ViewSupplier():
            view4Form = Toplevel(root)
            view4Form.title("Supplier Details")
            view4Form.geometry("600x300")
            cursor.execute("select * from Supplier")
            print(list(cursor.execute))

        def ViewAuthor():
            view5Form = Toplevel(root)
            view5Form.title("Author Details")
            view5Form.geometry("600x300")
            cursor.execute("select * from Author_of_the_books")
            print(list(cursor.execute))
        
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
            update1Form = Toplevel(root)
            update1Form.title("Update Customer Details")
            update1Form.geometry("400x300")

            def closeupdate1Info():
                enableButtons()
                update1Form.destroy()

            CustomerIDLabel = Label(update1Form, text="CustomerID:")
            CustomerIDText = Entry()
            First_NameLabel = Label(update1Form, text="First_Name:")
            First_NameText = Entry()
            Last_NameLabel = Label(update1Form, text="Last_Name:")
            Last_NameText = Entry()
            ContactIDLabel = Label(update1Form, text="ContactID:")
            ContactIDText = Entry()
            UsernameLabel = Label(update1Form, text="Username:")
            UsernameText = Entry()
            PasswordLabel = Label(update1Form, text="Password:")
            PasswordText = Entry()
        
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
                if(CustomerID=="" or Username=="" ):
                    MessageBox.showinfo('Update Status', 'All fields are required')
                else:
                    cursor.execute("update Customer set First_Name='" + First_Name +"', Last_Name='" + Last_Name +"', Username='" + Username +"' where CustomerID='"+ CustomerID +"'")
                    cursor.execute('commit')
                
            update = Button(update1Form, text="Update", command = update1Info)
            update.place(x=200, y=250)
        
            
        def AuthorDetails():
            update2Form = Toplevel(root)
            update2Form.title("Update Author Details")
            update2Form.geometry("400x300")

            def closeupdate2Info():
                enableButtons()
                update2Form.destroy()

            AuthorIDLabel = Label(update2Form, text="AuthorID:")
            AuthorIDText = Entry()
            First_NameLabel = Label(update2Form, text="First_Name:")
            First_NameText = Entry()
            Last_NameLabel = Label(update2Form, text="Last_Name:")
            Last_NameText = Entry()
            GenderLabel = Label(update2Form, text="Gender:")
            GenderText = Entry()
            Date_of_BirthLabel = Label(update2Form, text="Date_of_Birth:")
            Date_of_BirthText = Entry()
           
        
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
                
            update2 = Button(update2Form, text="Update", command = update2Info)
            update2.place(x=200, y=250)
            

        def BookDetails():
            update3Form = Toplevel(root)
            update3Form.title("Update Book Details")
            update3Form.geometry("400x300")
            
            def closeupdate3Info():
                enableButtons()
                update3Form.destroy()

            ISBNLabel = Label(update3Form, text="ISBN:")
            ISBNText = Entry()
            TitleLabel = Label(update3Form, text="Title:")
            TitleText = Entry()
            Publication_DateLabel = Label(update3Form, text="Publication_Date:")
            Publication_DateText = Entry()
            User_ReviewsLabel = Label(update3Form, text="User_Reviews:")
            User_ReviewsText = Entry()
        
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
                
            update3 = Button(update3Form, text="Update", command = update3Info)
            update3.place(x=250, y=250)
    
        update1Button = Button(root, text="Update Customer Details", command = CustomerDetails)
        update2Button = Button(root, text="Update Author Details", command = AuthorDetails)
        update3Button = Button(root, text="Update Book Details", command = BookDetails)
        update1Button.place(x=200, y=30)
        update2Button.place(x=200, y=60)
        update3Button.place(x=200, y=90)
    

    def Remove():
        
        def RemoveCustomer(): #not complete
            remove1Form = Toplevel(root)
            remove1Form.title("Remove Customer")
            remove1Form.geometry("600x300")

            def closeupremove1Info():
                enableButtons()
                remove1Form.destroy()
            CustomerIDLabel = Label(remove1Form, text="CustomerID:")
            CustomerIDText = Entry()
            First_NameLabel = Label(remove1Form, text="First_Name:")
            First_NameText = Entry()
            Last_NameLabel = Label(remove1Form, text="Last_Name:")
            Last_NameText = Entry()
            ContactIDLabel = Label(remove1Form, text="ContactID:")
            ContactIDText = Entry()
            UsernameLabel = Label(remove1Form, text="Username:")
            UsernameText = Entry()
            PasswordLabel = Label(remove1Form, text="Password:")
            PasswordText = Entry()
        
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
    
            remove = Button(remove1Form, text="Remove", command = remove1Info)
            remove.place(x=200, y=250)

            
        def RemoveAuthor():
            remove2Form = Toplevel(root)
            remove2Form.title("Remove Author")
            remove2Form.geometry("600x300")

            def closeupremove2Info():
                enableButtons()
                remove2Form.destroy()
                
            AuthorIDLabel = Label(remove2Form, text="AuthorID:")
            AuthorIDText = Entry()
            First_NameLabel = Label(remove2Form, text="First_Name:")
            First_NameText = Entry()
            Last_NameLabel = Label(remove2Form, text="Last_Name:")
            Last_NameText = Entry()
            GenderLabel = Label(remove2Form, text="Gender:")
            GenderText = Entry()
            Date_of_BirthLabel = Label(remove2Form, text="Date_of_Birth:")
            Date_of_BirthText = Entry()
           
        
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
            remove2 = Button(remove2Form, text="Remove", command = remove2Info)
            remove2.place(x=200, y=250)
            
        def RemoveBook():
            remove3Form = Toplevel(root)
            remove3Form.title("Remove Book")
            remove3Form.geometry("600x300")
            
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
        
        def RemoveSupplier():
            remove4Form = Toplevel(root)
            remove4Form.title("Remove Supplier")
            remove4Form.geometry("600x300")
            
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
