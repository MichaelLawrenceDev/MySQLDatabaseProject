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
#

# Entry into Admin_Form.py
def Start(admin_cursor, username):
    # cursor should already be connected.
    print("Logging in as admin under username: " + username)
    admin_cursor.execute("select * from Customer")
    print(list(admin_cursor))
