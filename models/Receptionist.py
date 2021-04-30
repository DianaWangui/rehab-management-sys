from app import db
from models.Common import CommonMethods


class ReceptionistsModel(db.Model, CommonMethods):
    __tablename__ = 'receptionists'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    phone = db.Column(db.String(10), nullable=False)
    image = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String())

    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))