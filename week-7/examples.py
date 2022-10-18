# Import SQLite Library
import sqlite3

# Connect to database (normally you would
# give a path like "my_data.db")
conn = sqlite3.connect(':memory:')

# Create a cursor to let you pass in SQL
c = conn.cursor()

# Send our first CRUD operations: Create!
c.execute("CREATE TABLE fruit (name text)")
c.execute("INSERT INTO fruit VALUES ('Apple'), ('Orange')")

# Always commit your work
conn.commit() # Useful if saving to a file, or to rollback to

# CRUD operation: Reading
print("Current fruit in db:")
for row in c.execute("SELECT * FROM fruit"):
    # row is a tuple where each index
    # matches the index of the table columns
    name = row[0] # First column
    print(name)

# Close the database connection
conn.close()