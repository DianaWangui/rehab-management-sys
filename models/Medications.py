from app import db
from models.Common import CommonMethods


class MedicationsModel(db.Model, CommonMethods):
    __tablename__ = 'medications'
    id = db.Column(db.Integer, primary_key=True)
    medicine = db.Column(db.String())
    times = db.Column(db.Integer())

    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'))
