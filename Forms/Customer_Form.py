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
        viewForm = Toplevel(cForm)
        viewForm.title("Account Holder Details")


        def queryToText(query):
            text = ""
            for i in range(len(query)):
                if i != len(query)-1:
                    text += str(query[i][0]) + ", "
                else:
                    text += str(query[i][0])
            return text

            
        # Customer Details
        query = list(cursor.execute(f"""select First_Name, Last_Name from Customer where username = '{username}'"""))
        NameText = f"{query[0][0]} {query[0][1]}"
        NameLabel = Label(viewForm, text="Full Name:")
        Name = Label(viewForm, text=NameText)
        usernameLabel = Label(viewForm, text="Username:")
        User = Label(viewForm, text=username)
        passwordLabel = Label(viewForm, text="Password:")
        passwordText = cursor.execute(f"""select password from Customer where username = '{username}'""")
        Pass = Label(viewForm, text="*************")
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
        

    def addDetails():
        addForm = Toplevel(cForm)
        addForm.title("Add Details")
        
        def closeAddForm():
            enableButtons()
            addForm.destroy()

        AddressLabel = Label(addForm, text="Address:")
        AddressText = Entry(addForm, width=25)
        EmailLabel = Label(addForm, text="Email:")
        EmailText = Entry(addForm, width=25)
        PhoneLabel = Label(addForm, text="Phone:")
        PhoneText = Entry(addForm, width=25)
        AddressLabel.grid(row=0, column=0)
        AddressText.grid(row=0, column=1)
        EmailLabel.grid(row=1, column=0)
        EmailText.grid(row=1, column=1)
        PhoneLabel.grid(row=2, column=0)
        PhoneText.grid(row=2, column=1)

        def addInfo():
            address = AddressText.get()
            email = EmailText.get()
            phone = PhoneText.get()
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
                    messagebox.showerror("Add Failure", f"Cannot add {phone}, phone Number is already registered to this or another account.")

            conn.commit()
        
        add = Button(addForm, text="Add", command = addInfo)
        add.grid(row=4, column=1)

    def removeDetails(): #DOESN'T WORK YET
        removeForm = Toplevel(cForm)
        removeForm.title("Delete Customer Details")

        rLabel = Label(removeForm, text="Not sure how to go about this yet...")
        rLabel.grid(row=1, column=1)


#Books
    def viewBooks():
        booksForm = Toplevel(cForm)
        booksForm.title("Browse Books")

        def search(): #DOESN'T WORK YET
            bookTitle = cursor.execute(f"""select Title from Books where Title like '%key%' order by Title""")
            s = Listbox(booksForm, width = 35)
            Scrollbar(s, orient="vertical")
            
            for x in bookTitle:
                s.insert(END, *x)

            s.grid(column=1, row=1, sticky='NS')
            
        SearchLabel = Label(booksForm, text="Search keyword:")
        SearchText = Entry(booksForm, width=35)
        key = SearchText.get()
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
    addButton = Button(cForm, text="Add to Account Details", command = addDetails)
    removeButton = Button(cForm, text="Remove Account Details", command = removeDetails)
    viewButton.grid(row=1, column=1)
    addButton.grid(row=2, column=1)
    removeButton.grid(row=3, column=1)
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
