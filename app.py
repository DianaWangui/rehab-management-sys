from flask import Flask, render_template, url_for, redirect, request, flash, session, g
from flask_sqlalchemy import SQLAlchemy
from config.config import Development, Production
from functools import wraps

app = Flask(__name__)

app.config.from_object(Development)
# app.config.from_object(Production)

db = SQLAlchemy(app)

from models.Admin import AdminModel
from models.Receptionist import ReceptionistsModel
from models.Doctors import DoctorsModel
from models.Nurses import NursesModel
from models.Rooms import RoomsModel
from models.Patients import PatientsModel
from models.Medications import MedicationsModel


# create tables in our database
@app.before_first_request
def create_tables():
    db.create_all()

# set session
@app.before_request
def setg():
    g.user = None
    try:
        if session:
            if session['username']:
                g.user = session['username']
            else:
                g.user = None
        else:
            g.user = None
    except:
        print('no worries')


# create the login required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


# login used applies to everyone including admin
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if AdminModel.fetch_by_username(username):
            if AdminModel.check_password(username, password):
                session['username'] = username
                session['id'] = AdminModel.fetch_by_username(username).id
                session['role'] = AdminModel.fetch_by_username(username).role

                return redirect(url_for(''))
    return render_template('login.html')


# register admin
@app.route('/register_admin', methods=['POST', 'GET'])
def register_admin():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        username = request.form['username']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        hashed_password = AdminModel.generate_hash(password)
        role = 'admin'

        if password == confirm_password:
            if AdminModel.check_username(username) and AdminModel.check_email(email):
                flash('Username/Email already exists!')
                return render_template('register.html')
            else:
                admin = AdminModel(first_name=first_name, last_name=last_name, username=username, phone=phone,
                                   email=email, role=role, password=hashed_password)
                admin.insert_records()
                return redirect(url_for('login'))
        else:
            flash("The two passwords do not match!")
            return render_template("register.html")
    return render_template('register.html')


# recover admin password
@app.route('/recover_admin_password')
def recover_admin_password():
    return render_template('forgot.html')


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('admin_dashboard.html')


@app.route('/admin_receptionists')
@login_required
def admin_receptionists():
    return render_template('admin_receptionists.html')


@app.route('/admin_doctors')
@login_required
def admin_doctors():
    return render_template('admin_doctors.html')


@app.route('/admin_nurses')
@login_required
def admin_nurses():
    return render_template('admin_nurses.html')


@app.route('/admin_rooms')
@login_required
def admin_rooms():
    return render_template('admin_rooms.html')


if __name__ == '__main__':
    app.run()
