import pyodbc

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
def Start(cursor, username):
    # cursor should already be connected.
    print("Logging in under Customer's username: ", username)

    # Select all emails from customer with username
    cursor.execute(f"""
        select Email from CMail, Customer where 
        Customer.ContactID = CMail.ContactID and 
        Customer.Username = '{username}'
    """)
    print("Emails: ", list(cursor))

    # Select all addresses from customer with username
    cursor.execute(f"""
        select Address from CAddress, Customer where
        Customer.ContactID = CAddress.ContactID and
        Customer.Username = '{username}'
    """)
    print("Addresses: ", list(cursor))

    # Select all phone numbers from customer with username
    cursor.execute(f"""
        select Phone_Number from CNumber, Customer where
        Customer.ContactID = CNumber.ContactID and
        Customer.Username = '{username}'
    """)
    print("Phone Numbers: ", list(cursor))

    # To add contact details to a customer
    #   1. get contactID of customer
    #   2. insert all emails with contactID
    #   3. insert all phone numbers
    #   4. insert all addresses
    #
    # To change details, use MySQL Update query


    # How to get ContactID
    query_answer = cursor.execute(f"""
        select ContactID from Customer where
        Username = '{username}'
    """)
    contactID = int(list(query_answer)[0][0])
    print(f"ContactID: {contactID}")
