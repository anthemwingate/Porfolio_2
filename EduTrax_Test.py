#Project           : University Course Tracking Software
#Program name      : EduTrax.py
#Author            : Anthem Rukiya J. Wingate
#Creation Date     : 4.10.19
#Purpose           : EduTrax.py - Automated Test File
#Revision History  : Version 2.0
#Notes  : Additional revision made for interview submission.

""" automated tests for AWingatehw10_v2.5 rev.py """

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

import unittest
""" imports unit test module """

from EduTrax.py import Repository, Student, Instructor, Major
""" imports program file for testing """

class Student_Prettytable_Test(unittest.TestCase):
    """ Test class for Student Pretty Table Function """

    def __init__(self):
        """ Assigns the path variable for use by test functions.  """

        self.dir_abs_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
        self.directory_path = f"{dir_abs_path}/EduTrax.py"
        self.repo = Repository(directory_path)
        

    def test_student_prettytable(self):
        """ Test function for Student Pretty Table  """
        
        expected =  [[10103,'Baldwin, C','SFEN',['CS 501', 'SSW 564', 'SSW 567', 'SSW 687'],['SSW 540','SSW 555'], None],
            [10115,'Wyatt, X','SFEN',['CS 5,45', 'SSW 564', 'SSW 567', 'SSW 687'],['SSW 540','SSW 555'], None],
            [10172,'Forbes, I','SFEN',['SSW 555', 'SSW 567'],['SSW 540','SSW 564'],['CS 501','CS 513','CS 545']],
            [10175,'Erickson, D','SFEN',['SSW 564','SSW 567','SSW 687'],['SSW 540','SSW 555'],['CS 501','CS 513','CS 545']],
            [10183,'Chapman, O','SFEN',['SSW 689'],['SSW 540','SSW 555','SSW 564','SSW 567'],['CS 501','CS 513','CS 545']],
            [11399,'Cordova, I','SYEN',['SSW 540'],['SYS 612','SYS 671','SYS 800'],None],
            [11461,'Wright, U','SYEN',['SYS 611', 'SYS 750', 'SYS 800'],['SYS 612','SYS 671'],['SSW 540','SSW 565','SSW 810']],
            [11658,'Kelly, P','SYEN',['SSW 540'],['SYS 612','SYS 671','SYS 800'],['SSW 540','SSW 565','SSW 810']],
            [11714,'Morton, A','SYEN',['SYS 611', 'SYS 645'],['SYS 612','SYS 671','SYS 800'],['SSW 540','SSW 565','SSW 810']],
            [11788,'Fuller, E','SYEN',['SSW 540'],['SYS 612','SYS 671','SYS 800'],None]]

        actual = [student.info() for student in self.repo.students.values()]
        self.assertEqual(actual, expected)
        
        return None

class Instructor_Prettytable_Test(unittest.TestCase):
    """ Test class for Instructor Pretty Table Function """

    def test_student_prettytable(self):
        """ Test function for Instructor Pretty Table  """

        expected = [['98765','Einstein, A','SFEN','SSW 567',4],
            ['98765','Einstein, A','SFEN','SSW 540',3],
            ['98764','Feynman, R','SFEN','SSW 564',3],
            ['98764','Feynman, R','SFEN','SSW 687',3],
            ['98764','Feynman, R','SFEN','CS 501',1],
            ['98764','Feynman, R','SFEN','CS 545',1],
            ['98763','Newton, I','SFEN','SSW 555',1],
            ['98763','Newton, I','SFEN','SSW 689',1],
            ['98760','Darwin, C','SYEN','SYS 800',1],
            ['98760','Darwin, C','SYEN','SYS 750',1],
            ['98760','Darwin, C','SYEN','SYS 611',2],
            ['98760','Darwin, C','SYEN','SYS 645',1]] 

        actual = [course for instructor in self.repo.instructors.values() for course in instructor.info()]
        self.assertEqual(actual, expected)

        return None

class Major_Prettytable_Test(unittest.TestCase):
    """ Test class for Major Pretty Table Function """

    def test_major_prettytable(self):
        """ Test function for Major Pretty Table  """


        expected = [['SFEN', ['CS 501','CS 545','SSW 540','SSW 555','SSW 564','SSW 567','SSW 687','SSW 689']],
            ['SYEN', ['SYS 611','SYS 645','SYS 750']]]

        actual = [major.info() for major in self.repo.majors.values()]
        self.assertEqual(actual, expected)

        return None

def query_instructors():
    """ Run Instructors Summary Table query """
 
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "810_hw11.db")
    db = sqlite3.connect(db_path)
    query = "select i.CWID, i.Name, i.Dept, g.Course, COUNT(*) as Students\
                FROM instructors i\
                    JOIN grades g\
                    ON i.CWID=g.Instructor_CWID\
                GROUP BY i.CWID, i.Name, i.Dept, g.Course"
 
    fields = ['CWID', 'Name', 'Dept', 'Course', 'Students']
    pt = PrettyTable(field_names=fields)
    print('Instructors Summary Table\n')
    for row in db.execute(query):
        pt.add_row(row)
    print(pt)
    
    return None

if __name__ == "__main__":
    query_instructors()
    unittest.main(exit=False, verbosity=2)
        

    