#Project           : University Course Tracking Software
#Program name      : EduTrax.py
#Author            : Anthem Rukiya J. Wingate
#Creation Date     : 04.24.2019
#Purpose           : EduTrax.py - University Repository with web functionality
#Revision History  : Version 2
#Notes  : Additional revision made for interview submission.

import os 
""" imports OS module """

import sqlite3
""" imports sqlite3 module """

from prettytable import PrettyTable 
""" imports prettytable module """

from collections import defaultdict
""" imports default dict from collections module """

from flask import Flask, render_template
""" imports flask module """

import jinja2
""" imports jinja2 module """

app = Flask(__name__)

@app.route('/instructors')
def instructors_summary():
    """ Run Instructors Summary Table query """

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "810_hw11.db")
        
    query = """select i.CWID, i.Name, i.Dept, g.Course, COUNT(*) as Students
                FROM instructors i
                    JOIN grades g
                    ON i.CWID=g.Instructor_CWID
                GROUP BY i.CWID, i.Name, i.Dept, g.Course"""
    
    db = sqlite3.connect(db_path)
    rows = db.execute(query)
    data = [{'CWID':CWID, 'Name':Name, 'Dept':Dept, 'Course':Course, 'Students':Students} for CWID, Name, Dept, Course, Students in rows]
    db.close()

    return render_template('instructors_table.html', title = 'Stevens Repository', table_title = 'Number of Students by Course and Instuctor', instructors = data)

app.run(debug=True)