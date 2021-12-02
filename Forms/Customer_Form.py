from tkinter import *
from tkinter import messagebox
import Customer_Form
import Admin_Form
import pyodbc
import bcrypt
import sys

# Customer Form - What it should accomplish
#
#   1. Edit customer contact cetails (View, Add, Remove)
#       * I would recommend that this would open another form. (like the signup form)
#   2. Display a browser for books in the database
#       - Display books in either ascending/descending order.
#       - Display books ordered by either Title, Publication date or Category.
#       - Allows for keyword searches
#           * EX: Find all books with keyword "Dragon" in Title
#   3. Add book from browser into customer order
#       - Can edit current order(View, Remove)
#       * I would also recommend that this is done through another form.
#       - Can submit the order to the database when ready.
#



# Entry into Customer_Form.py
def Start(conn, username):
    # cursor should already be connected.
    print("Logging in under Customer's username: ", username)
    cursor = conn.cursor()

    ### Customer Form ###
    cForm = Tk()
    cForm.title("Customer Details")
    
    def viewDetails():
        disableButtons()
        viewForm = Toplevel(cForm)
        viewForm.title("Account Holder Details")

        
        def closeViewForm():
            enableButtons()
            viewForm.destory()

        def queryToText(query):
            text = ""
            for i in range(len(query)):
                if i != len(query)-1:
                    text += str(query[i][0]) + ", "
                else:
                    text += str(query[i][0])
            return text

        # On exit, enable buttons
        viewForm.protocol("WM_DELETE_WINDOW", closeViewForm)
            
        # Customer Details
        query = list(cursor.execute(f"""select First_Name, Last_Name from Customer where username = '{username}'"""))
        NameText = f"{query[0][0]} {query[0][1]}"
        NameLabel = Label(viewForm, text="Full Name:")
        Name = Label(viewForm, text=NameText)
        usernameLabel = Label(viewForm, text="Username:")
        User = Label(viewForm, text=username)
        passwordLabel = Label(viewForm, text="Password:")
        passwordText = cursor.execute(f"""select password from Customer where username = '{username}'""")
        Pass = Label(viewForm, text="Can you remove displaying password from this form?")
        phoneLabel = Label(viewForm, text="Phone Number:")
        query = list(cursor.execute(f"""select Phone_Number from Customer, CNumber where username = '{username}' and CNumber.ContactID = Customer.ContactID"""))
        Phone = Label(viewForm, text=queryToText(query))
        addressLabel = Label(viewForm, text="Address:")
        query = list(cursor.execute(f"""select Address from Customer, CAddress where username = '{username}' and CAddress.ContactID = Customer.ContactID"""))
        Address = Label(viewForm, text=queryToText(query))
        emailLabel = Label(viewForm, text="Email:")
        query = list(cursor.execute(f"""select Email from Customer, CMail where username = '{username}' and CMail.ContactID = Customer.ContactID"""))
        Email = Label(viewForm, text=queryToText(query))
        blankspace = Label(viewForm, text=" ")
        # Positioning
        NameLabel.grid(row=0, column=0)
        Name.grid(row=0, column=1)
        usernameLabel.grid(row=1, column=0)
        User.grid(row=1, column=1)
        passwordLabel.grid(row=2, column=0)
        Pass.grid(row=2, column=1)
        phoneLabel.grid(row=3, column=0)
        Phone.grid(row=3, column=1)
        addressLabel.grid(row=4, column=0)
        Address.grid(row=4, column=1)
        emailLabel.grid(row=5, column=0)
        Email.grid(row=5, column=1)
        blankspace.grid(row=8, column=0)


    def contactDetailEditor():

        def closeRemoveForm():
            enableButtons()
            cdForm.destroy()
        
        def updateHelper(query, col_num, type):
            # type= email, phone, address : 0/1/2
            llist = []
            blist = []
            # load button and labels into lists
            for i in range(len(query)):
                val = str(query[i][0]) # get hard copy string
                label = Label(cdForm, text=val)
                btn = Button(cdForm, text="-", command = lambda: removeDetail(val, type))
                label.grid(row=3+i, column=col_num)
                btn.grid(row=3+i, column=col_num+1)

                llist.append(label)
                blist.append(btn)
            contactLabels.append(llist.copy())
            buttons.append(blist.copy())

        def updateDetails():
            # clear contact buttons and labels
            for i in range(len(buttons)):
                for j in range(len(buttons[i])):
                    buttons[i][j].destroy()
                    contactLabels[i][j].destroy()

            contactLabels.clear()
            buttons.clear()

            # Update Form Emails
            query = list(cursor.execute(f"""
                select Email from Customer, CMail 
                where username = '{username}' and CMail.ContactID = Customer.ContactID
            """))
            updateHelper(query, 0, 0)
            
            # Phone Numbers
            query= list(cursor.execute(f"""
                select Phone_Number from Customer, CNumber 
                where username = '{username}' and CNumber.ContactID = Customer.ContactID
            """))
            updateHelper(query, 2, 1)

            # Addresses
            query = list(cursor.execute(f"""
                select Address from Customer, CAddress 
                where username = '{username}' and CAddress.ContactID = Customer.ContactID
            """))
            updateHelper(query, 4, 2)

        def removeDetail(x, type):
            # type [0=email, 1=phone, 2=address]
            query = []
            try:
                if (type == 0):
                    print(f"delete from CMail where Email = '{x}'")
                    query = list(cursor.execute(f"delete from CMail where Email = '{x}'"))
                elif (type == 1):
                    print(f"delete from CNumber where Phone_Number = {x}")
                    query = list(cursor.execute(f"delete from CNumber where Phone_Number = {x}"))
                else:
                    print(f"delete from CAddress where Address = '{x}'")
                    query = list(cursor.execute(f"delete from CAddress where Address = '{x}'"))
            except Exception as e:
                print(e)

            
            cursor.execute('commit')
            updateDetails()

        def addDetails():
            address = addressEntry.get()
            email = emailEntry.get()
            phone = phoneEntry.get()
            query_answer = cursor.execute(f"""select ContactID from Customer where Username = '{username}'""")
            contactID = int(list(query_answer)[0][0])

            if address != "":
                try:
                    cursor.execute(f"insert into CAddress values ('{address}',{contactID})")
                except:
                    messagebox.showerror("Add Failure", f"Cannot add {address}, address is already registered to this or another account.")
            if email != "":
                try:
                    cursor.execute(f"insert into CMail values ('{email}',{contactID})")
                except: # Duplicate email exists
                    messagebox.showerror("Add Failure", f"Cannot add {email}, email is already registered to this or another account.")
            if phone != "":
                try:
                    cursor.execute(f"insert into CNumber values ('{phone}',{contactID})")
                except:
                    messagebox.showerror("Add Failure", f"Cannot add {phone}, phone Number is not a valid number or it already exists in database.")

            conn.commit()
            updateDetails()
        
        ### Contact Details Form ###

        cdForm = Toplevel(cForm)
        cdForm.title("Contact Details View/Edit")
        contactLabels = []
        buttons = []

        titleLabel = Label(cdForm, text="--- Contact Details ---")
        emailLabel = Label(cdForm, text="Emails:")
        phoneLabel = Label(cdForm, text="Phone Numbers:")
        addressLabel = Label(cdForm, text="Address:")
        emailEntry = Entry(cdForm, width=35)
        phoneEntry = Entry(cdForm, width=35)
        addressEntry = Entry(cdForm, width=35)

        titleLabel.grid(row=0, column=2)
        emailLabel.grid(row=1, column=0)
        phoneLabel.grid(row=1, column=2)
        addressLabel.grid(row=1, column=4)
        emailEntry.grid(row=2, column=0)
        phoneEntry.grid(row=2, column=2)
        addressEntry.grid(row=2, column=4)
        
        addEmailButton = Button(cdForm, text="+", command = addDetails)
        addPhoneButton = Button(cdForm, text="+", command = addDetails)
        addAddressButton = Button(cdForm, text="+", command = addDetails)

        addEmailButton.grid(row=2, column=1)
        addPhoneButton.grid(row=2, column=3)
        addAddressButton.grid(row=2, column=5)

        updateDetails()
    
    def viewBooks():
        disableButtons()
        booksForm = Toplevel(cForm)
        booksForm.title("Browse Books")
        
        def closeBrowseForm():
            enableButtons()
            booksForm.destroy()

        def search():
            key = SearchText.get()  # <-- Just moved key here and added {} inside query
            bookTitle = cursor.execute(f"""select Title from Books where Title like '%{key}%' order by Title""")
            s = Listbox(booksForm, width = 35)
            Scrollbar(s, orient="vertical")
            
            for x in bookTitle:
                s.insert(END, *x)

            s.grid(column=1, row=1, sticky='NS')
            
        SearchLabel = Label(booksForm, text="Search keyword:")
        SearchText = Entry(booksForm, width=35)
        SearchButton = Button(booksForm, text="Search", command = search)
        SearchLabel.grid(row=0, column=0)
        SearchText.grid(row=0, column=1)
        SearchButton.grid(row=0, column=2)
        
        #print books
        bookTitle = cursor.execute(f"""select Title from Books order by Title""")
        b = Listbox(booksForm, width = 35)
        Scrollbar(b, orient="vertical")
        booksForm.geometry("400x300")
        
        for x in bookTitle:
            b.insert(END, *x)

        b.grid(column=1, row=1, sticky='NS')
        
    viewButton = Button(cForm, text="View Account", command = viewDetails)
    removeButton = Button(cForm, text="Change Contact Details", command = contactDetailEditor)
    viewButton.grid(row=1, column=1)
    removeButton.grid(row=2, column=1)
    browse = Button(cForm, text="Browse Books", command = viewBooks)
    browse.grid(row=4, column=1)
    
    def disableButtons():
        viewButton['state'] = DISABLED
        addButton['state'] = DISABLED
        removeButton['state'] = DISABLED

    def enableButtons():
        viewButton['state'] = ACTIVE
        addButton['state'] = ACTIVE
        removeButton['state'] = ACTIVE
    
    mainloop()
