from app import app
from app.models import Dept, Course, Section, SectionToTime
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    deptList = Dept.query.order_by('name')
    courseList = Course.query.order_by('name')
    sectionList = Section.query.order_by('id')
    return render_template('index.html', depts=deptList, courses=courseList, sections=sectionList)

