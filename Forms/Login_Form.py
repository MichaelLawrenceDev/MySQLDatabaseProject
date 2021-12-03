from tkinter import *
from tkinter import messagebox
import Customer_Form
import Admin_Form
import pyodbc
import bcrypt
import sys

### Description:
### This is the login script, it will create a login form that logs
### in a user or signs up an account into the bookstore database.

# You can also run 'python3 customer_form.py <username> <password>' to log in faster

### TODO: Username comparison query is not case sensitive (ie: user2 = UseR2),
###       need to make it case sensitive.

def main():

    def startLogin():
        disableButtons()

        username = usernameText.get()
        password = passwordText.get()
        
        if (username == ''):
            messagebox.showwarning("Username Error", "Please enter username.")
        elif (password == ''):
            messagebox.showwarning("Password Error", "Please enter password.")
        if login(username, password, conn.cursor(), True):
            return

        enableButtons()

    def login(username, password, cursor, close_form, allow_admin_login=True):

        # try to login as admin.
        admin_login_success = False
        if (allow_admin_login):
            try:
                admin_conn = pyodbc.connect(
                    "DRIVER={SQL Server Native Client 11.0};"
                    "Server=104.36.123.122,8592;"
                    "Database=BookStoreDatabase;"
                   f"UID={username};"
                   f"PWD={password};"
                )
                if close_form:
                    root.destroy()
                admin_login_success = True
            except:
                pass # This should only error as failing to login via pyodbc
        if (admin_login_success):
            Admin_Form.Start(admin_conn, username)
            return True
        else:
            # try to log in as customer
            result = list(cursor.execute("select Password from Customer where Username='"+username+"';"))
            if len(result) == 0:
                messagebox.showerror("Login Failure", "Username does not exist")
                return False

            user_hash = result[0][0].encode()
            if bcrypt.checkpw(password.encode(), user_hash):
                # Password match
                if close_form:
                    root.destroy() 
                Customer_Form.Start(conn, username)
                return True
            else:
                messagebox.showerror("Login Failure", "Password is invalid.")
            return False

    def signupForm():

        def closeSignupForm():
            enableButtons()
            newForm.destroy()

        def signup():
            signupButton['state'] = DISABLED

            reqInfo = [
                usernameText.get(),  # 0
                passwordText.get(),  # 1
                passwordText2.get(), # 2
                firstNameText.get(), # 3
                lastNameText.get()]  # 4

            for infoPiece in reqInfo:
                if (infoPiece == ''):
                    messagebox.showerror("Signup Failure", "Some required fields are empty.")
                    signupButton['state'] = ACTIVE
                    return

            if (reqInfo[1] != reqInfo[2]): # passwords don't match
                messagebox.showerror("Signup Failure", "Passwords provided do not match.")
                signupButton['state'] = ACTIVE
                return

            # SQL Connection (Check for Username uniqueness)
            cursor = conn.cursor()
            cursor.execute("select Username from Customer where Username='"+reqInfo[0]+"';")
            if len(list(cursor)) != 0:
                messagebox.showerror("Signup Failure", "Username provided already exists.")
                signupButton['state'] = ACTIVE
                return

            ### Signup criteria met, adding account to database...

            # get next customerID
            # Get CustomerID, Hash password, and add to database
            try:
                # If query returns nothing, then start with id = 0
                CustomerID = int(list(cursor.execute("select max(CustomerID) from Customer;"))[0][0]) + 1
            except:
                CustomerID = 0
            try:
                # Assign contact_ID
                query = list(cursor.execute(f"""
                    select max(ContactID) from Contact_Details
                """))
                ContactID = int(query[0][0]) + 1
                cursor.execute(f"""
                    insert into Contact_Details values ({ContactID})
                """)
                # create password and and submit to server
                passwordHash = bcrypt.hashpw(reqInfo[1].encode(), bcrypt.gensalt()).decode()
                cursor.execute(f"insert into Customer values ({CustomerID}, '{reqInfo[3]}', '{reqInfo[4]}', {ContactID}, '{reqInfo[0]}', '{passwordHash}');")
                conn.commit()
            except Exception as er:
                messagebox.showerror("Signup Failure", er)
            
            newForm.destroy()
            login(reqInfo[0], reqInfo[1], cursor, True, False)

        ### Signup Form ###

        disableButtons()
        newForm = Toplevel(root)
        newForm.title("Sign Up")

        # On exit, enable buttons on login form
        newForm.protocol("WM_DELETE_WINDOW", closeSignupForm)

        # Signup Login Information 
        loginInfo = Label(newForm, text="Account Information")
        usernameLabel = Label(newForm, text="Username:")
        usernameText = Entry(newForm, width=25)
        passwordLabel = Label(newForm, text="Password:")
        passwordText = Entry(newForm, width=25)
        passwordLabel2 = Label(newForm, text="Reenter password:")
        passwordText2 = Entry(newForm, width=25)

        # Personal Information
        personalInfo = Label(newForm, text="Personal Information")
        firstNameLabel = Label(newForm, text="First Name:")
        firstNameText = Entry(newForm, width=25)
        lastNameLabel = Label(newForm, text="Last Name:")
        lastNameText = Entry(newForm, width=25)
        signupSubmitButton = Button(newForm, text="Sign Up", command=signup)

        # Login Info Positioning
        loginInfo.grid(row=0, column=1)
        usernameLabel.grid(row=1, column=0)
        usernameText.grid(row=1, column=1)
        passwordLabel.grid(row=2, column=0)
        passwordText.grid(row=2, column=1)
        passwordText['show'] = '*'
        passwordLabel2.grid(row=3, column=0)
        passwordText2.grid(row=3, column=1)
        passwordText2['show'] = '*'

        # Personal Info Positioning
        personalInfo.grid(row=5, column=1)
        firstNameLabel.grid(row=6, column=0)
        firstNameText.grid(row=6, column=1)
        lastNameLabel.grid(row=7, column=0)
        lastNameText.grid(row=7, column=1)
        signupSubmitButton.grid(row=8, column=1)

    def disableButtons():
        loginButton['state'] = DISABLED
        signupButton['state'] = DISABLED

    def enableButtons():
        loginButton['state'] = ACTIVE
        signupButton['state'] = ACTIVE

    # Connect to SQL Server
    conn = pyodbc.connect(
        "DRIVER={SQL Server Native Client 11.0};"
        "Server=104.36.123.122,8592;"
        "Database=BookStoreDatabase;"
        "UID=Customer;"
        "PWD=Customer;"
    )

    # Argument check (You can log in with arguments)
    logged_in = False
    if (len(sys.argv) == 3):
        if login(sys.argv[1], sys.argv[2], conn.cursor(), False):
            logged_in = True
        else:
            print("Login information provided is invalid.")
    elif (len(sys.argv) != 1):
        print("Usage: python3 Customer_Form.py <username> <password>")

    if not logged_in:
        ### Login Form ###
        root = Tk()
        root.title("Log In")

        # Login Form Initilization
        usernameLabel = Label(root, text="Username:")
        usernameText = Entry(root, width=25)
        passwordLabel = Label(root, text="Password:")
        passwordText = Entry(root, width=25)
        passwordText['show'] = '*'
        orText = Label(root, text="or")
        loginButton = Button(root, text="Log in", command=startLogin)
        signupButton = Button(root, text="Sign Up", command=signupForm)

        # Positioning
        usernameLabel.grid(row=0, column=0)
        usernameText.grid(row=0, column=1)
        passwordLabel.grid(row=1, column=0)
        passwordText.grid(row=1, column=1)
        loginButton.grid(row=2, column=1)
        orText.grid(row=3, column=1)
        signupButton.grid(row=4, column=1)


        root.mainloop()

main()
