# Create a SQLite3 database and table


# import the sqlite3 library
import sqlite3

# create the connection object
conn = sqlite3.connect("new.db")

# get a cursor object used to execute SOL commands
cursor = conn.cursor()

# create a table
cursor.execute("""CREATE TABLE population
(city TEXT, state TEXT, population INT)
""")

# close the database connection
conn.close()
