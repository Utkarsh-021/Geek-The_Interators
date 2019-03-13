from flask import Flask,request,render_template
import pymysql as pm
mysql=MySQL()
app=Flask(__name__)
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='123'
app.config['MYSQL_DATABASE_DB']='honda'
app.config['MYSQL_DATABASE_host']='localhost'
app.config['MYSQL_DATABASE_PORT']=3306
mysql.init_app(app)

@app.route('/',methods=['POST'])
def get_data():
 return render_template("sample.html")
if request.method=='POST':
     employeeid=request.form['employeeid']
     employeename=request.form['employeename']
     dob=request.form['dob']
     salary= request.form['salary']
     connection = mysql.get_db()
     cursor = connection.cursor()
     query="INSERT INTO names_tbl(employeeid,employeename,dob,salary) VALUES(employeeid,employeename,dob,salary)"
     cursor.execute(query,(employeeid,employeename,dob,salary))
     connection.commit()
     return "nothing fucked"
else:
    return("something fucked up")
