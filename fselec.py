from tkinter import *
from connneci import *
import fcancel
import fsearch

h_font=('Helvetica bold',40)
b_font = ("Times", "14",)

def page_funcselect(win,oldframe,modestr,db):

    functype = Frame(win,width=900,height=600)
    oldframe.forget()
    functype.tkraise()

    functype.pack()

    l_heading = Label(functype,text="Function Select ",font = h_font)
    l_heading.place(x=0,y=0)

    imgbus= PhotoImage(file='bus.png')
    imgtrain= PhotoImage(file='train.png')
    imgflight= PhotoImage(file='flight.png')


    bb= Button(functype,text = "BOOK" ,command= lambda : fsearch.page_search(win,functype,modestr,db),  width = 20,height=10)
    bt= Button(functype,text = "CANCEL" ,command = lambda:fcancel.page_cancel(win,db,functype,modestr) ,width = 20,height=10)
    print("hiiii")


    bb.place(x=200,y=200)
    bt.place(x=450,y=200)
   

    pass





