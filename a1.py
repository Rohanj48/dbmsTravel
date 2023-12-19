
from tkinter import *
import mysql.connector
from connneci import *
import tksheet as tw


import fselec


db = cnnc()

h_font=('Helvetica bold',40)
b_font = ("Times", "14",)

win = Tk()

win.call("source","azure.tcl")
win.call("set_theme","dark")


win.title("AgenCY")
win.geometry("900x600")



## type Page Select

def page_typefind():

    fr_type = Frame(win,width=900,height=600)
    fr_type.tkraise()
    fr_type.pack()

    l_heading = Label(fr_type,text="Mode of Transport",font = h_font)
    l_heading.place(x=0,y=0)

    imgbus= PhotoImage(file='bus.png')
    imgtrain= PhotoImage(file='train.png')
    imgflight= PhotoImage(file='flight.png')

    bb= Button(fr_type,text = "bus" ,command = lambda : fselec.page_funcselect(win,fr_type,"bus",db) ,width = 10,height=10)
    bt= Button(fr_type,text = "train" ,command = lambda : fselec.page_funcselect(win,fr_type,"train",db) ,width = 10,height=10)
    bf= Button(fr_type,text = "flight" ,command = lambda : fselec.page_funcselect(win,fr_type,"flight",db),width = 10,height=10)


    bb.place(x=200,y=200)
    bt.place(x=300,y=200)
    bf.place(x=400,y=200)





    pass


## page selecet finish

#on another filee

##

def riderfunc(del_entry,res_label):
    ## no idea why python works like this but rquired to udatea lable values along with button updates
    db.rem_bookings(del_entry.get())
    res_label.configure(text=db.cancelstr)
    res_label.place(x=10,y=490)

def page_cancel():

    ## first show his bookings and let him choose booking id
    ## delete based on booking id 

    fr_cancel = Frame(win,width=900,height=600)
    fr_cancel.tkraise()
    bookstr = db.get_bookings()

    l_heading = Label(fr_cancel,text="Booking",font = h_font)
    l_b1 = Label(fr_cancel,text="Your Bookings -- ",font = b_font)
    #l_bookings = Label(fr_cancel,text=bookstr,font = b_font)


    l_heading.place(x=0,y=0)
    l_b1.place(x=50,y=100)
    #l_bookings.place(x=50,y=150)
    fr_cancel.pack()

    table = tw.Sheet(fr_cancel,width=900,height= 200)
    table.headers(['user_id', 'B_id', 'numberseats', 'souce', 'dest'])
    table.column_width(column=0, width=150, only_set_if_too_small=False)
    table.column_width(column=1, width=150, only_set_if_too_small=False)
    table.column_width(column=2, width=150, only_set_if_too_small=False)
    table.column_width(column=3, width=150, only_set_if_too_small=False)
    table.column_width(column=4, width=150, only_set_if_too_small=False)
    
    table.enable_bindings('all')
    table.disable_bindings(
        ['rc_insert_column', 'rc_delete_column', 'edit_cell', 'delete', 'paste', 'cut', 'rc_delete_row',
         'rc_insert_row'])

    for row in bookstr:
         table.insert_row(values=row, idx='end', add_columns=False)   
    table.place(x=0,y=150)

    del_label = Label(fr_cancel,text="Enter Bid to delete ",font = b_font) 
    del_entry = Entry(fr_cancel ,width=20 )
    res_label = Label(fr_cancel,text="-",font = b_font) 
    

    b_cancel  = Button(fr_cancel,text="Cancel",width=20,command = lambda : riderfunc(del_entry,res_label))
    res_label.configure(text=db.cancelstr)
    del_label.place(x=10,y=400)
    del_entry.place(x=10,y=430)
    b_cancel.place(x=10,y=460)
    res_label.place(x=10,y=490)

    pass



def btfunc_login():
    var = db.validate_user(e_passsword,e_username,l_status,page_typefind)
    if var == 1:
        page_typefind()
bg_image = PhotoImage(file = "bg.png")


canvas1 = Canvas( win, width = 900, height = 600) 
  
#canvas1.pack(fill = "both", expand = True) 
  
# Display image 

#canvas1.create_image( 0, 0, image = bg_image, anchor = "nw")

l_heading = Label(win,text="Travel Management System",font = h_font)

l_username = Label(win,text="Username",font = b_font)
l_password = Label(win,text="Password",font = b_font)
l_ex = Label(win,text="'To Explore is to Live' ",font = ("Times", "24", "bold italic") )

l_status = Label(win,text="",font = b_font)

e_username = Entry(win,width=20 )
e_passsword = Entry(win,width=20 )
e_passsword.insert(0,"abc")
e_username.insert(0,"amit")

b_submit = Button(win,text="Submit",width=20,command=btfunc_login)

l_heading.place(x=90,y=3)

l_username.place(x=300,y=100)
e_username.place(x=400,y=100)

l_password.place(x=300,y=150)
e_passsword.place(x=400,y=150)

l_status.place(x=400,y=230)
b_submit.place(x=400,y=200)

l_ex.place(x=300,y=300)

win.mainloop()





