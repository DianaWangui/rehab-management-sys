from app import db
from models.Common import CommonMethods


class PatientsModel(db.Model, CommonMethods):
    __tablename__ = 'patients'
    # added by the receptionist
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    age = db.Column(db.Integer())
    gender = db.Column(db.String())
    phone = db.Column(db.String(10))
    blood_group = db.Column(db.String())

    # added by doctor
    room = db.Column(db.String())
    duration = db.Column(db.Integer())
    nurse = db.Column(db.String())

    # create pseudo columns
    medications = db.relationship('MedicationsModel', backref='patient')
