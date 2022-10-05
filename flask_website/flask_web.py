from flask import (
    Flask,
    render_template,
    request,
)

app = Flask(__name__)

@app.route('/')
def home():
    if request.args =="GET":
        ''' Shows we move to home page'''
        print("Redirecting to home")
        

    return render_template('home.html')

@app.route('/projects/')
def projects():
    if request.method =="GET":
        ''' Shows we move to projects page'''
        print("Redirecting to projects")


    return render_template('projects.html')
    
@app.route('/contacts/', methods=['GET','POST'])
def contacts():
    user_address = ''
    user_email_content = ''


    if request.method =="GET":
        ''' Shows we move to contacts page'''

        print("Redirecting to contacts")
        #print(request.form)                     #Debugging dict

    if request.method == "POST":
        ''' Display form user's email address and email content to console.'''
        # User submitted the Post Form

        #print(request.form)                     #Debugging dict
        user_address = request.form['email-add'] # Contains what user typed in
        user_email_content = request.form['email-content']

        print("Address is: ", user_address)
        print("The content of inquiry by {}: {}".format(user_address, user_email_content))

    return render_template('contacts.html')

@app.route('/design')
def design():
    if request.method =="GET":
        ''' Shows we move to design page'''

        print("Redirecting to design")

    return render_template('design.html')



