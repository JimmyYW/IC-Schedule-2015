__author__ = 'Kelly'

from flask import Flask
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = "The peperonizzi always try photogreph me in compromisin position. Unlucky for them" \
                           "my head will be soon unstuck from this sodacan. Any minut"
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)


class Dept(db.Model):
    __tablename__ = 'dept'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    abbr = db.Column(db.String(4))

    def __init__(self, name, abbr):
        self.name = name
        self.abbr = abbr

    def __repr__(self):
        return "<Dept %r>" % self.abbr


class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    desc = db.Column(db.String(256))
    number = db.Column(db.Integer)
    credits = db.Column(db.Integer)
    dept = db.Column(db.Integer, db.ForeignKey('dept.id'))

    def __init__(self, name, desc, number, credits, dept):
        self.name = name
        self.desc = desc
        self.number = number
        self.credits = credits
        self.dept = dept

    def __repr__(self):
        return "<Course %r>" % self.name


class Section(db.Model):
    __tablename__ = 'section'
    id = db.Column(db.Integer, primary_key=True)
    crn = db.Column(db.Integer)
    # time = ????????
    prof = db.Column(db.String(64))
    course = db.Column(db.Integer, db.ForeignKey('course.id'))

    def __init__(self, crn, time, prof, course):
        self.crn = crn
        self.time = time
        self.prof = prof
        self.course = course

    def __repr__(self):
        return "<Course %r>" % self.crn

db.create_all()
db.session.commit()

