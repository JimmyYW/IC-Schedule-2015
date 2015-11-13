__author__ = 'Kelly'

from flask import Flask
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
import os
import datetime as dt

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
    prof = db.Column(db.String(64))
    course = db.Column(db.Integer, db.ForeignKey('course.id'))

    def __init__(self, crn, prof, course):
        self.crn = crn
        self.prof = prof
        self.course = course

    def __repr__(self):
        return "<Course %r>" % self.crn


class Time(db.Model):
    __tablename__ = 'time'
    id = db.Column(db.Integer, primary_key=True)
    timeStart = db.Column(db.Time)
    timeEnd = db.Column(db.Time)
    day = db.Column(db.Integer)  # 0=Sunday, 6=Saturday

    def __init__(self, start, end, day):
        self.timeStart = start
        self.timeEnd = end
        self.course = day

    def __repr__(self):
        return "<Time %r>" % self.id


class SectionToTime(db.Model):
    __tablename__ = 'section2time'
    id = db.Column(db.Integer, primary_key=True)
    timeId = db.Column(db.Integer, db.ForeignKey('time.id'))
    sectionId = db.Column(db.Integer, db.ForeignKey('section.id'))

    def __init__(self, sectionId, timeId):
        self.timeId = timeId
        self.sectionId = sectionId

    def __repr__(self):
        return "<SectionToTime %r>" % self.id


db.create_all()
db.session.commit()


def populate_db():
    dept = Dept("Computer Science", "COMP")
    course = Course("Adv. Web", "Doug rocks", 20500, 4, dept.id)
    section = Section(12345, "Doug", course.id)
    time = Time(dt.time(14, 0), dt.time(14, 50), 1)
    section2time = SectionToTime(section.id, time.id)
    db.session.add(dept)
    db.session.add(course)
    db.session.add(section)
    db.session.add(time)
    db.session.add(section2time)
    db.session.commit()


def main():
    populate_db()


main()



