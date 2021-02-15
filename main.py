from flask import Flask, request,session,flash
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# creating an instance of the flask application
app = Flask(__name__)

# the configuration string ya kuaccess our database.
# we are using postgres server FYI
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:wambua@localhost/hakiba"

# now, we create our SQlAlchemy stuff hapa
db = SQLAlchemy(app)

# MIGRATIONS !!!!
migrate = Migrate(app, db)

""" Models 
"""
class UserAccount(db.Model):
    # the name of the database table to be created
    __tablename__ = "user_accounts"

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(120))
    lastname = db.Column(db.String(120))
    account_balance = db.Column(db.Integer, default=0)

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


class AdminAccount(db.Model):
    __tablename__ = "admin_accounts"
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(155))
    password = db.Column(db.String(100))

    def __init__(self, username, password):
        self.username = username
        self.password = password


"""
These here are the various routes that will be available
to use in our application.
Sometime later on we shall move them outside this main file. but for now,
lets just leave them here

"""
# the first route for our index page.
# it will serve as our landing page, possibly a central navigation 
@app.route('/')
def index(): 
    
    # here we display a list of all users who are registered.
    users = UserAccount.query.all()

        
    return render_template('index.html', users_list = users)



# this here will serve our login template.
# basic stuff, login pekee
@app.route('/account/login',methods=["POST","GET"])
def login():
    if request.method=="POST":
        # this value
       username=request.form.get('username')

       password=request.form.get('password')


       user_search_query = AdminAccount.query.filter_by(username = username, password=password)
       users_found = user_search_query.all()

       if(len(users_found) < 1):
           another_user_search = UserAccount.query.filter_by(firstname= username)
           user_found = another_user_search.all()

           if (len(user_found) < 1):
               error_message = "Incorrect Login Details"
               return render_template("login.html", login_message = error_message)

           normal_user = user_found[0]
           return render_template("account.html", user = normal_user)
                        
       the_found_user = users_found[0]
       return render_template('account.html', user = the_found_user)
    
    return render_template("login.html")


# this one here will handle the registration process
@app.route('/account/register', methods=["POST","GET"])
def register():

    firstname=request.form.get('firstname')
    lastname=request.form.get('lastname')

    random_user = UserAccount(firstname, lastname)
    db.session.add(random_user)
    db.session.commit()

    return render_template('register.html')


@app.route('/admin', methods = ["POST","GET"])
def admin():
    username = request.form.get('username')
    password = request.form.get('password')

    random_admin = AdminAccount(username,password)
    db.session.add(random_admin)
    db.session.commit()

    return render_template('admin.html')

if __name__ == "__main__":
    app.run()