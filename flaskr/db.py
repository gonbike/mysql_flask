#coding=utf-8
import config
from flask import Flask
import MySQLdb
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.mysql_config

db = SQLAlchemy(app,use_native_unicode="utf8")

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(32),nullable=False)


    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return "<User '{:s}'>".format(self.username)

class Alticle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(100),nullable=False)
    text = db.Column(db.String(3000),nullable=False)

    def __init__(self,userId,title,text):
        self.userid = userId
        self.title = title
        self.text = text

class Dboj():
    global db
    global app
    @classmethod
    def getdb(self):
        return db

    @classmethod
    def getapp(self):
        return app

if __name__ == '__main__':
    db.create_all()
    innset=User(username='admin',password='123456')
    db.session.add(innset)
    db.session.commit()
    #insetA=Alticle(userId=int(12),title="you?",text="I love you")
    #db.session.add(insetA)
    #db.session.commit()
    #entries=Alticle.query.with_entities(Alticle.title,Alticle.text).all()
    #res= User.query.with_entities(User.password).all()
    #print entries
