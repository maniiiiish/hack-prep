from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(20), unique=True)
    upass = db.Column(db.String(20), unique=True)

    def __init__(self, id, uname, upass):
        self.id = id
        self.uname = uname
        self.upass = upass

    def __repr__(self):
        return ('<User {}>'.format(self.name))

db.create_all()

