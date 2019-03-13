from flask import Flask,render_template,request
import pymysql as ps




conn=ps.connect(host='localhost',port=3306,user='root',password='123',db='hackathon')
sql="select Remedy1,Remedy2 from remedies where disease='common cold'"
print("connection established")


try:
    cur=conn.cursor()
    cur.execute(sql)
    for A in cur:
        print(A)

except:
    print()