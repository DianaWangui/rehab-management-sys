from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class CommonAuthMethods:
    def insert_records(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def fetch_all(cls):
        return cls.query.all()

    @classmethod
    def fetch_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    # fetch user by username
    @classmethod
    def fetch_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @staticmethod
    def generate_hash(password):
        return generate_password_hash(password)

    @classmethod
    def check_username(cls, username):
        record = cls.query.filter_by(username=username).first()
        if record:
            return True
        else:
            return False

    @classmethod
    def check_email(cls, email):
        record = cls.query.filter_by(email=email).first()
        if record:
            return True
        else:
            return False

    @classmethod
    def check_password(cls, username, password):
        record = cls.query.filter_by(username=username).first()

        if record and check_password_hash(record.password, password):
            return True
        else:
            return False