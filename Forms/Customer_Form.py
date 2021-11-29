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