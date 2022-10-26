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
import PySimpleGUI as sg



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
            return(row)


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


def set_veggie_data(window, v):
    """Set up veggie data"""
    window['datainfo'].update(v.show_all())


def main():
    print("-=-=-=-=-=-")
    v = Vegetables()
    v.setup()

    sg.theme('Dark Blue 3')
    #headings=["Vegetables Name", "Quantity"]
    #print(vegetable_records)

    layout = [[sg.T('The VegeTable:')],
                #[sg.Table(values=vegetable_records)],
                [sg.T('Database', size=(12,1), key='datainfo')],
                [sg.I(key='-new_vegetable-')],
                [sg.B('Add Vegetable'), sg.B('Exit')]],

    window = sg.Window('Alexander Holmes - Database GUI', layout, finalize=True)
    set_veggie_data(window, v)

    while True:  # Event Loop
        event, values = window.read()
        print(event, values)
        

        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Add Vegetable':
            # change the "output" element to be the value of "input" element
            pass
            
    window.close()

if __name__ == '__main__':
    main()
