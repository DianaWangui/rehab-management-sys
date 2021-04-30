from app import db
# from models.Common import CommonMethods
from models.CommonAuth import CommonAuthMethods


class AdminModel(db.Model, CommonAuthMethods):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    phone = db.Column(db.String(10), nullable=False)
    password = db.Column(db.String())
    role = db.Column(db.String())

    # create pseudo columns
    receptionists = db.relationship('ReceptionistsModel', backref='admin')
    doctors = db.relationship('DoctorsModel', backref='admin')
    nurses = db.relationship('NursesModel', backref='admin')
    rooms = db.relationship('RoomsModel', backref='admin')
