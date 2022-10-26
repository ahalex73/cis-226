# Alexander Holmes
# 10/26/22
# CRN: 10235
# CIS 226: Advanced Python Programming
# Total time it took to complete --- 2 hours ---

'''
This console program allows the user to use the program_console_db utility tool. This tool
calls for one initial parameter - the syntax being "python program_console_db (command)".
This can consist of Add, Get, Change, ShowAll, Delete. 

Add     - Add a new vegetable 
Get     - Gets a vegetables quantity
Change  - Updates a vegetable's quantity
ShowAll - Shows all of the contents of the vegetable table
Delete  - Deletes specified vegetable

'''
import sqlite3
import sys


def main():

    class Vegetables:
        def __init__(self):
            """Connecting to our database and creating a cursor to pass in SQL"""
            self.conn = sqlite3.connect('my_data.db')
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
            item_name = input("Enter the vegetable you'd like to see the quantity of: ")
            print(v.find_vegetable(str(item_name)))

        case "Change":
            v.show_all()
            item_name = input("Enter the item you'd like to change: ")
            varied_quantity = input("Enter the new quantity: ")
            v.update_vegetable(item_name, varied_quantity)
            v.show_all()

        case "ShowAll":
            v.show_all()

        case "Delete":
            item_name = input("Enter the item you'd like to delete: ")
            v.delete_vegetable(item_name)
        
        case _:
            print("Invalid Command.")

    # in_operation = True # Flag indicating whether the user wants to keep entering commands or not
    # while in_operation:
    # stop = input("Would you like to stop using commands? (y/n): ")    
    # if stop == "y" or "Y":
    #     in_operation = False
    # elif stop =="n" or "N":
    #     pass
    # else:
    #     input("Please enter a valid option.")
    

if __name__ == '__main__':
    main()