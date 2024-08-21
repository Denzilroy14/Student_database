'''Mini project-1(STUDENT DATABASE)

Desc:-Python mini web student database to collect info
about a student and save it in the
data base using flask and sqlite3

Date of publish:-16/08/24

FULL COPYRIGHTS RESERVED @ www.github.com//Denzilroy'''
from flask import*
import sqlite3
app=Flask(__name__)
@app.route('/')
def main():
    return render_template('student_page.html')
connect=sqlite3.connect('studentdb.db')
connect.execute('CREATE TABLE IF NOT EXISTS students(student_name TEXT,student_age INTEGER,student_contact TEXT,student_email TEXT,sub1 TEXT,sub2 TEXT,sub3 TEXT,sub4 TEXT,sub5 TEXT,sub6 TEXT,mark1 INTEGER,mark2 INTEGER,mark3 INTEGER,mark4 INTEGER,mark5 INTEGER,mark6 INTEGER)')
@app.route('/details',methods=['GET','POST'])
def details():
    if request.method=='POST':
        name=request.form['studentname']
        age=request.form['studentage']
        contact=request.form['studentcontact']
        email=request.form['studentmail']
        s1=request.form['sub1']
        m1=request.form['mark1']
        s2=request.form['sub2']
        m2=request.form['mark2']
        s3=request.form['sub3']
        m3=request.form['mark3']
        s4=request.form['sub4']
        m4=request.form['mark4']
        s5=request.form['sub5']
        m5=request.form['mark5']
        s6=request.form['sub6']
        m6=request.form['mark6']
        with sqlite3.connect('studentdb.db')as conn:
            curr=conn.cursor()
            curr.execute('INSERT INTO students(student_name,student_age,student_contact,student_email,sub1,sub2,sub3,sub4,sub5,sub6,mark1,mark2,mark3,mark4,mark5,mark6)VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(name,age,contact,email,s1,s2,s3,s4,s5,s6,m1,m2,m3,m4,m5,m6))
            conn.commit()
            return "<html><body><h1>Details uploaded successfully</h1></body></html>"
        return render_template('viewdetails.html')
    else:
        return render_template('details.html')
@app.route('/viewdetails')
def viewdetails():
    with sqlite3.connect('studentdb.db')as file:
        cursor=file.cursor()
        cursor.execute('SELECT * FROM students')
        details=cursor.fetchall()
    return render_template('viewdetails.html',data=details)
if __name__=='__main__':
    app.run(debug=True)
















            
