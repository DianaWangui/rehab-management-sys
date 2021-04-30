from app import db
from models.Common import CommonMethods


class RoomsModel(db.Model, CommonMethods):
    __tablename__ = 'rooms'
    id = db.Column(db.Integer, primary_key=True)
    room_number = db.Column(db.String(), nullable=False)

    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
