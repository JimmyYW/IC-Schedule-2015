#!/usr/bin/env python
__author__ = 'yanmingwang'

from flask.ext.mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from datetime import datetime
from flask import Flask, render_template, session, redirect, url_for, flash
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import Required
# from config import config
import os
# import models

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm(Form):
    name = StringField('Artist Name:', validators=[Required()])
    description = TextAreaField('Description:')
    submit = SubmitField('Submit')

@app.errorhandler(404)
def page_not_found(e):
    print(e)
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    print(e)
    return render_template('500.html'), 500

# def createInitialArtistDict():
#     if 'aList' not in session:
#         session['aList'] = dict()
#         session['aList']['Also VulgarCafeteria'] = 'Also VulgarCafeteria, Live healthier. Live happier!'
#         session['aList']['Selfish Lavatory'] = 'Selfish Lavatory is an investment in good appearance!'
#         session['aList']['Donkey Suspension'] = 'The Human friendly Donkey Suspension!'

@app.route('/')
def index():
    # createInitialArtistDict()
    return render_template('courses.html',current_time=datetime.utcnow(),session = session)

# @app.route('/artist/<artistName>')
# def artistName(artistName):
#     if artistName in session['aList']:
#         return render_template('artistPage.html', artistName=artistName, session=session['aList'],)
#     else:
#         return render_template('404.html'), 404
#
# @app.route('/artist')
# def artist():
#     createInitialArtistDict()
#     sortedSession = sorted(session['aList'].keys())
#     return render_template('artistList.html',session=session,sortedSession = sortedSession)
#
# @app.route('/newArtists', methods=['GET', 'POST'])
# def test():
#     createInitialArtistDict()
#     form = NameForm()
#     if form.validate_on_submit():
#         session['aList'][form.name.data] = form.description.data
#         flash('New Artist ' + form.name.data + ' Added!! Thank you!')
#     return render_template('newArtists.html', form=form)

if __name__ == '__main__':
    manager.run()
