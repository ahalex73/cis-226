# Alexander Holmes
# 10/31/22
# CRN: 10235
# CIS 226: Advanced Python Programming
# Total time it took to complete --- 3.5 hours ---

'''
This program allows the end user to view and maniupulate a database using a Graphical User Interface.

How to use:
Simply view your database -- in this case were using vegetables-- and insert in a desired name and quantity
to modify or add. Then hit the 'Add/Update Vegetable' button to update your database.

For more documentation or assistance look at the About and Help menu options.
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
        rows = self.c.execute("SELECT * FROM vegetable")
        vegetable_information = []
        for row in rows:
            vegetable_information.append(row)
        return vegetable_information


    def add_update_vegetable(self, name, quantity):
        """Add or update a vegetable in vegetable"""
        self.c.execute("SELECT name, quantity FROM vegetable WHERE name=?", [name])
        row = self.c.fetchone()
        found = row

        if found:
            try:
                self.c.execute("UPDATE vegetable SET quantity=? WHERE name=?", [quantity, name])
                self.conn.commit()
            except ValueError:
                print("Invalid name or quantity values.")
                sys.exit()

        else:
            try:
                self.c.execute("INSERT INTO vegetable VALUES (?, ?)", [int(quantity), str(name)])
                self.conn.commit()
            except ValueError:
                print("Invalid name or quantity values.")
                sys.exit()

    '''Additional options to add later.'''
    # def find_vegetable(self, name):
    #     """Find a vegetable in our table"""
    #     self.c.execute("SELECT quantity, name FROM vegetable WHERE name=?", [name])
    #     row = self.c.fetchone() 
    #     return row

    # def delete_vegetable(self, name):
    #     found = self.c.execute("SELECT quantity, name FROM vegetable WHERE name=?", [name])
    #     if found:
    #         self.c.execute("DELETE FROM vegetable WHERE name=?", [name])
    #         self.conn.commit() # Save work so far
    #         print("{} has been removed".format(name))

    #     else:
    #         print("Unable to find {}".format(name))

    #     return

    def close(self):
        self.conn.close()


def set_veggie_data(window, v):
    """Set up veggie data"""
    window['vegetable_data'].update(v.show_all())
    pass
    

def main():
    print("-=-=-=-=-=-")
    v = Vegetables()
    v.setup()

    sg.theme('Dark Blue 3')
    headings=["Quantity", "Vegetable's Name"]

    layout = [
                [sg.T("Hi, Welcome to your very own VegeTable! You can manipulate it however you'd like")],
                [sg.T('The VegeTable:')],
                [sg.Table(values = v.show_all(),
                            headings = headings,
                            max_col_width=35,
                            num_rows=10,
                            row_height=35,
                            justification= "center",
                            key="vegetable_data"
                )],
                [sg.I(key='-VEG_NAME-'), sg.T("Name")],
                [sg.I(key='-VEG_QUANTITY-'), sg.T("Quantity")],
                [sg.B('Add/Update VegeTable', key="add_update_veg"), sg.B('Exit')],

                [sg.Menu(
                    [['Help', ['Help']],
                    ['About', 'About']], key='-MenuBar-')],
            ]
    window = sg.Window('Alexander Holmes - Database GUI', layout, finalize=True)
    set_veggie_data(window, v)

    while True:  # Event Loop
        event, values = window.read()
        print(event, values)
        

        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        elif event == 'add_update_veg':
            veg_quantity = values['-VEG_QUANTITY-']
            veg_name = values['-VEG_NAME-']
            v.add_update_vegetable(veg_name, veg_quantity)
            window['vegetable_data'].update(v.show_all())

        elif event =='About':
                    ''' About page dropdown content '''
                    about_content = '' +\
                        'Design: The design of the Sort GUI was to display a database to the end user and allow them to manipulate it.\n\n' +\
                        'Develop: Using python and PySimpleGUI, the VegeTable was able to be created.\n\n' +\
                        'Test: There are no tests.\n\n'+\
                        'Document: The only files required are requirements.txt, gui_db.py(The GUI part of the application), and my_data.db (Example database)'
                
                    sg.popup(about_content, title="About")

        elif event == 'Help':
                    ''' Help page dropdown content'''
                    help_section = "How to use\n\n" +\
                        "1. View your VegeTable.\n\n" +\
                        "2. Think about what you would like to add/update\n\n" +\
                        "3. Enter a name of the vegetable and the quantity of the vegetable in the input boxes\n\n" +\
                        "4. Hit 'Add/Update VegeTable' to add or update your vegetable inside of the table!\n\n" 

                    sg.popup(help_section, title="Help")
                    print("A popup should display. If not," + \
                        "there is documentation to reference at the top of the program.")

    window.close()

if __name__ == '__main__':
    main()
