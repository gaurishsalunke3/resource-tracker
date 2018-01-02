from db import db

class EmployeeModel(db.Model):
    __tablename__ = 'employes'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    band = db.Column(db.String(10), unique=False, nullable=False)
    designation = db.Column(db.String(80), unique=False, nullable=False)
    date_of_joining = db.Column(db.DateTime, unique=False, nullable=False)

    def get(self):
        pass
