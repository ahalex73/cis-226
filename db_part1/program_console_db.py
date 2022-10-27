# Alexander Holmes
# 10/26/22
# CRN: 10235
# CIS 226: Advanced Python Programming
# Total time it took to complete --- 4 hours ---

'''
This console program allows the user to use the program_console_db utility tool. This tool
calls for one initial parameter - the syntax: "python program_console_db (command)".
This can consist of Add, Get, Change, ShowAll, Delete. You will then be prompted accordingly
To specify changes/options.

Add     - Add a new vegetable 
Get     - Gets a vegetables quantity
Change  - Updates a vegetable's quantity
ShowAll - Shows all of the contents of the vegetable table
Delete  - Deletes specified vegetable

Design: The program was created using system arguments, python, capsys, and pytest,
        it is designed allow the user to manipulate the database inside of the console.
Develop: I researched on pytest, classes, and SQL syntax, as well as referenced the given materials.
Test: Tests the add_vegetable, update_vegetable, and delete_vegetable functions
      testing the output given by capsys in a new database to test functionality.
Document: The program_console_db.py file contains the functionality of the program_console_db utility tool
      This tool allows you to use commands to manipulate a database. As well as a test_program_console.py file
      that tests the functionality of some functions in the program_console_db file.
      There should also be requirements.txt and an example database called "my_data.db" available.

'''
import sqlite3
import sys


class Vegetables:
    def __init__(self, db='my_data.db'):
        """Connecting to our database and creating a cursor to pass in SQL"""
        self.conn = sqlite3.connect(db)
        self.c = self.conn.cursor()

    def setup(self):
        """Setup a table if it does not already exist inside our database"""
        self.c.execute("CREATE TABLE IF NOT EXISTS vegetable (quantity integer, name text)")
        self.conn.commit()

    def show_all(self):
        """Shows all values from the vegetable table"""
        for row in self.c.execute("SELECT * FROM vegetable"):
            print(row)


    def add_vegetable(self, name, quantity):
        """Add vegetable to our vegetable table"""
        try:
            self.c.execute("INSERT INTO vegetable VALUES (?, ?)", [int(quantity), str(name)])
            self.conn.commit()
        except ValueError:
            print("Invalid name or quantity values.")
            sys.exit()

    def update_vegetable(self, name, quantity):
        self.c.execute("SELECT quantity, name FROM vegetable WHERE name=?", [name])
        try:
            self.c.execute("UPDATE vegetable SET quantity=? WHERE name=?", [quantity, name])
            self.conn.commit()
        except ValueError:
            print("Invalid name or quantity values.")
            sys.exit()
        

    def find_vegetable(self, name):
        """Find a vegetable in our table"""
        self.c.execute("SELECT quantity, name FROM vegetable WHERE name=?", [name])
        row = self.c.fetchone() 
        return row

    def delete_vegetable(self, name):
        found = self.c.execute("SELECT quantity, name FROM vegetable WHERE name=?", [name])
        if found:
            self.c.execute("DELETE FROM vegetable WHERE name=?", [name])
            self.conn.commit() # Save work so far
            print("{} has been removed".format(name))

        else:
            print("Unable to find {}".format(name))

        return

    def close(self):
        self.conn.close()

if __name__ == '__main__':
    def main():
        print("-=-=-=-=-=-")
        v = Vegetables()
        v.setup()

        if len(sys.argv) < 2 or len(sys.argv) > 2:
            sys.stdout.write("Too many arguments, please input the desired sql command (Add, Get, Change, Delete, ShowAll)\n")
        sql_command = sys.argv[1]

        match sql_command:
            case "Add":
                """User enters in the add command, uses an item and a quantity to add to our database table"""
                print("Please enter a vegetable to add, and the desired quantity")
                item_name = input("Enter a vegetable to add: ")
                item_quantity = input("Enter a quantity: ")
                v.add_vegetable(str(item_name), item_quantity)
                v.show_all()

            case "Get":
                """Finds the vegetable that the user wishes to search for"""
                item_name = input("Enter the vegetable you'd like to see the quantity of: ")
                print(v.find_vegetable(str(item_name)))

            case "Change":
                """Updates an already existing vegetable in the table"""
                v.show_all()
                item_name = input("Enter the item you'd like to change: ")
                varied_quantity = input("Enter the new quantity: ")
                v.update_vegetable(item_name, varied_quantity)
                v.show_all()

            case "ShowAll":
                """Shows all vegetables and quantities"""
                v.show_all()

            case "Delete":
                """Deletes a specified vegetable"""
                item_name = input("Enter the item you'd like to delete: ")
                v.delete_vegetable(item_name)
            
            case _:
                """Edge case if sql_command from user is not entered correctly"""
                print("Invalid Command.")

    main()