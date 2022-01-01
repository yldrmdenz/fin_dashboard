import sqlite3

connection = sqlite3.connect ( "currency_records.db" )

# cursor
crsr = connection.cursor ()

# print statement will execute if there
# are no errors
print ( "Connected to the database" )

# close the connection
connection.close ( )