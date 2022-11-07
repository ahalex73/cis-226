import sqlite3
from flask import Flask, flash, render_template, request, redirect, url_for

DB_PATH = 'db.sqlite3'

app = Flask(__name__)
app.secret_key = b'Upg3zhGacjrP4mAf6bDU71GL7p7acQvPHIQknxBte4o'

# Our DB class does not need to know anything about flask or the web
class Vegetables:
    def __init__(self, conn):
        """Initializes Vegetable"""
        self.conn = conn
        self.c = self.conn.cursor()

    def setup(self):
        """Sets up the vegetable"""
        self.c.execute(
            'CREATE TABLE IF NOT EXISTS vegetable ('
            'pk INTEGER NOT NULL PRIMARY KEY,'
            'quantity INTEGER,'
            'name TEXT,'
            'price DECIMAL,'
            'total_price DECIMAL)'
                )
        self.conn.commit()
    def get_all(self):
        """Gather all"""
        for row in self.c.execute("SELECT * FROM vegetable"):
            yield row

    def add_vegetable(self, name, quantity, price, total_price, pk):
        """Adds an order to the vegetable table"""
        total_price = (float(quantity) * float(price))
        if pk:
            # Do an UPDATE
            self.c.execute(
                "UPDATE vegetable SET name=?, quantity=?, price=?, total_price WHERE pk=?",
                [name, quantity, price, total_price, pk])
        else:
            # Do an INSERT
            self.c.execute(
                "INSERT INTO vegetable (name, quantity, price, total_price) VALUES (?, ?, ?, ?)",
                [name, quantity, price, total_price])

            # Get a pk for the insert
            pk = self.c.lastrowid
        

        self.conn.commit()

    def find_vegetable(self, name):
        self.c.execute("SELECT * FROM vegetable WHERE name=?", [name])
        row = self.c.fetchone() # Get first row
        return row

    # def get_total_price(self, quantity, price, pk):
    #     """Gets the total price for each item"""
    #     self.c.execute("SELECT quantity, price WHERE pk=?", [quantity, price, pk])
    #     total_price = quantity * price
    #     self.c.execute("INSERT INTO vegetable (total_price) VALUES (?)", [total_price])
        
    #     self.conn.commit()

def db_setup():
    """Setup the db if needed"""
    app.logger.debug("Setting up db...")
    with sqlite3.connect(DB_PATH) as conn:
        v = Vegetables(conn)
        v.setup()
    app.logger.debug("Setting up db [Done]")

# Create table if needed when app starts
app.before_first_request(db_setup)

@app.route('/', methods=['GET', 'POST'])
def index():
    pk = 0
    price = ''
    total_price = ''
    name = ''
    quantity = ''
    valid = False
    if request.method == 'POST':
        # Validate form
        name = request.form.get('name')
        quantity = request.form.get('quantity')
        price = request.form.get('price')
        valid = True
        if not name or not quantity:
            flash('You must give a name and a quantity')
            valid = False
        else:
            try:
                quantity = int(quantity)
            except ValueError:
                flash('quantity must be an integer')
                valid = False

    # Open and close the db within the request
    with sqlite3.connect(DB_PATH) as conn:
        v = Vegetables(conn)
        # Add order if form was valid
        if valid:
            v.add_vegetable(name, quantity, price, total_price, pk)
            flash('{} was added with quantity {}'.format(name, quantity))
            # Always redirect after a POST was valid
            return redirect(url_for('index'))
        # Get new list of vegetables to display
        vegetables = v.get_all()
    return render_template(
        'base.html',
        title="DB Example",
        vegetables=vegetables,
        name=name,
        quantity=quantity,
        price=price,
        total_price=total_price,
    )