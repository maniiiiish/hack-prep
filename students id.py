from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'

db = SQLAlchemy(app)
class students(db.Model):
    id = db.Column('student_id', db.Integer, primary_key = True)
    username = db.Column(db.String(100)) 
    password = db.Column(db.String(50))
    name =  db.Column(db.String(100))
    roll_no =  db.Column(db.String(50))
    ##students model is created where identity of students stores

    def __init__(self, username, password, name, roll_no ):
        self.username = username
        self.password = password
        self.name = name
        self.roll_no = roll_no
       
st1= students("username","password","name","roll_no")
db.create_all()
db.session.add(st1)


