from flask import Flask,render_template,request
import pymysql as ps
import func as ort
import speech_recognition as sr
import jsonify

r=sr.Recognizer()

try:
 conn=ps.connect(host='localhost',port=3306,user='root',password='123',db='hackathon')
 cmd=conn.cursor()
 q="create table patient(person_fname varchar(45),person_lname varchar(45),person_email varchar(45),person_gender varchar(10),person_date date,person_blood varchar(5),person_mobile numeric(10),person_address varchar(45),person_state varchar(25),person_city varchar(20))"
 cmd.execute(q)
 print("Table Created...")
 conn.commit()
except:
 print("Table Already Created....")

app=Flask(__name__)


ort.create_table()
@app.route("/", methods = ['GET','POST'])
def slide():
    if(request.method=="POST"):


        ufname = request.form.get('ufname')
        ulname = request.form.get('ulname')
        email = request.form.get('email')
        gender = request.form.get('gender')
        bdate = request.form.get('bdate')
        blood = request.form.get('blood')
        mobileno = request.form.get('mobileno')
        address = request.form.get('address')
        ustate = request.form.get('ustate')
        ucity = request.form.get('ucity')


        try:

            q = "insert into patient values('{}','{}','{}','{}','{}','{}',{},'{}','{}','{}')".format(ufname,ulname,email,gender,bdate,blood,mobileno,address,ustate,ucity)
            print(q)
            cmd.execute(q)
            print("Record Submitted")
            conn.commit()
            conn.close()
        except:
            print("Fail to Submit Record...")


    return render_template("slide.html")

@app.route("/map.html")
def map():
    return render_template("map.html")

@app.route("/myReport.html")
def myReport():
    return render_template("myReport.html")

@app.route("/profile.html")
def profile():

    return render_template("profile.html")

@app.route("/appointment.html")
def appointment():
    return render_template("appointment.html")


app.run(debug="true")