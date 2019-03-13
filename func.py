import pymysql as ps


def create_table():
    try:
        conn = ps.connect(host='localhost', port=3306, user='root', password='123', db='barco_hack')
        cmd = conn.cursor()
        q = "create table patient(fname varchar(45),lname varchar(45),email varchar(45),gender varchar(10),dob date,blood_group varchar(45),mobile numeric(10),address varchar(100),city varchar(30),state varchar(25))"
        cmd.execute(q)
        print("Table Created...")
        conn.commit()
        conn.close()
    except:
        print("Table Already Created....")

def insert_data(pfn,pln,email,gender,bdate,bg,mn,a,s,c):
    try:
        conn = ps.connect(host='localhost', port=3306, user='root', password='123', db='barco_hack')
        cmd = conn.cursor()
        q = "insert into patient values('{}','{}','{}','{}','{}','{}',{},'{}','{}','{}')".format(pfn, pln, email,gender,bdate,bg,mn,a,s,c)
        cmd.execute(q)
        conn.commit()
        conn.close()
    except:
        print("fail to submit record")

def search_in_data(abc):
    try:
        conn = ps.connect(host='localhost', port=3306, user='root', password='123', db='barco_hack')
        cmd = conn.cursor()
        q = "select * from patient where mobileno=%s "


        cmd.execute(q,(abc))
        conn.commit()
        conn.close()
        return cmd
    except:
        print("fail to submit record")




