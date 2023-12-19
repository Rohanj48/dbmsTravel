import mysql.connector
from tkinter import *



b_font = ("Times", "17",)


class cnnc:
    host="localhost"
    user="user"
    password="password"
    database="Agency"
    rowc = 0
    cancelstr="--"    
    searchstr=""


    def __init__(self):
        self.db= mysql.connector.connect(
            host='localhost',
            user='root',
            password='tiger',
            database='Agency'
        )

    def validate_user(self,entpass,entuser,l,next_page) -> int:

        pstr = entpass.get()
        ustr = entuser.get()
        ustr = ustr.lstrip()
        ustr = ustr.rstrip()
        pstr = pstr.strip()
        qry = "select * from cust where name='"+ustr+"';"
        cur = self.db.cursor()
        cur.execute(qry)

        row = cur.fetchone()

        if row!=None:
            if (row[1]==pstr):
                l.configure(text = "   Validated")
                return 1
            else:
                l.configure(text = "Not Validated")
                return 0

        cur.close()




    def insert(self):
        str = ""
        cur = self.db.cursor()
        cur.execute(str)
        cur.close()
    
    def get_bookings(self) -> tuple:

        outstr = "User\tB_id\tfrom\tto\n"
        cur = self.db.cursor()
        cur.execute("select * from booking ;")
        li = []

        rows = cur.fetchall()

        for row in rows:
            li.append(row)

        cur.close()
        return li
    
    def rem_bookings(self,bid:str):
        bid = bid.lstrip()
        bid = bid.rstrip()
        qry = "delete from booking where booking_id="+bid+";"
        print(qry)
        cur = self.db.cursor()
        
        cur.execute(qry)
        self.db.commit()
        self.rowc = cur.rowcount
        cur.close()

        if self.rowc==0:
            self.cancelstr = "Bid INVALID"
        else :
            self.cancelstr = "Your Booking has been cancelled"
        print(self.cancelstr)

    def search(self,fromstr,tostr,datestr,modestr,lble)->str:
        str = "select * from {t1} where start = '{t2}' and dest = '{t3}' and day = '{t4}'".format(t1=modestr,t2=fromstr,t3=tostr,t4=datestr)
        print(str)
        cur = self.db.cursor()
        cur.execute(str)
        outstr=""
        rows = cur.fetchall()
        for row in rows:
            if row!=NONE:
                outstr += "No:{0}:\t Name {1} \ton {2} \t Seats Left: {3}".format(row[0],row[1],row[5],row[4])
                outstr+="\n"
                print(row)
        cur.close()
        lble.configure(text = outstr)



    