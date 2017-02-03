from flask_sqlalchemy import SQLALchemy
from flask import Flask
db = SQLALchemy()

if__name__=='__main__':
    from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(20), unique=True)
    upass = db.Column(db.String(20))
    email = db.Column(db.String(20))
    phone = db.Column(db.String(20))
    skills = db.Column(db.String(300))
    roll_no = db.column(db.String(20), unique=True)
    branch = db.column(db.String(100))
    post = db.relationship('posts',backref='student',lazy='dynamic')
    

    def __init__(self, uname, upass, email, phone,skills,roll_no,branch):
        self.uname = uname
        self.upass = upass
        self.email = email
        self.phone = phone
        self.skills = skills
        self.roll_no = roll_no
        self.branch = branch

        def __repr__(self):
        return ('<User {}>'.format(self.uname))

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

