from flask import Flask
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# creating an instance of the flask application
app = Flask(__name__)

# the configuration string ya kuaccess our database.
# we are using postgres server FYI
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Developer@localhost/hakiba"

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
@app.route('/account/login')
def login():
    return render_template('login.html')


# this one here will handle the registration process
@app.route('/account/register')
def register():

    random_user = UserAccount("Joseph", "Musa")
    db.session.add(random_user)
    db.session.commit()

    return render_template('register.html')


if __name__ == "__main__":
    app.run()