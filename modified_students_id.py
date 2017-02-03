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
    post = db.relationship('posts',backref='student',lazy='dynamic')
    
    def __init__(self, username, password, name, roll_no ):
        self.username = username
        self.password = password
        self.name = name
        self.roll_no = roll_no
       
st1= students("username","password","name","roll_no")
db.create_all()
db.session.add(st1)
db.session.commit()


class posts(db.model):
    id = db.Column('post_id', db.Integer, primary_key = True)
    student_id = db.Column(db.Integer,db.foreign_key("students.id"))
    post = db.Column(db.String(10000))
    comment = db.relationship('comments',backref='post',lazy='dynamic')

    def __init__(self,post ):
        self.post = post

sp = posts("post")
db.create_all()
db.session.add(sp)
db.session.commit()


class comments(db.model):
    id = db.Column('comment_id', db.Integer, primary_key = True)
    post_id = db.Column(db.Integer,db.foreign_key("posts.id"))
    comment = db.Column(db.string(10000))

    def __init__(self,comments):
        self.comment = comment
        
sc = comments("comment")
db.create_all()
db.sessoin.add(sc)
db.session.commit()


