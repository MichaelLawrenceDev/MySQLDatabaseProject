import pyodbc

def read(conn):
  print("Read")
  cursor = conn.cursor()
  cursor.execute("Select * from Customer")
  for row in cursor:
    print(f'row = {row}')
  print()

conn = pyodbc.connect(
  "DRIVER={SQL Server Native Client 11.0};"
  "Server=104.36.123.122,8592;"
  "Database=BookStoreDatabase;"
  "UID=Lawrence;"
  "PWD=assword;"
)

read(conn)