from tkinter import *
from connneci import *



h_font=('Helvetica bold',40)
b_font = ("Times", "14",)
b1_font = ("Times", "17",)



def search_submit(db,from_entry,to_entry,date_entry,modestr,l_out,bno_lable,bno_entry,bno_button):

    db.search(from_entry.get(),to_entry.get(),date_entry.get(),modestr,l_out)
    
    bno_lable.place(x=30,y=500)
    bno_entry.place(x=30,y=530) 
    bno_button.place(x=30,y=560)

def page_search(win,oldframe,modestr,db):

    functype = Frame(win,width=900,height=600)
    oldframe.forget()
    functype.tkraise()
    functype.pack()

    l_heading = Label(functype,text="Search",font = h_font)
    l_heading.place(x=0,y=0)

    Label(win, text="From:").place(x=30, y=130)
    from_entry = Entry(win)
    from_entry.place(x=100, y=130)

    Label(win, text="To:").place(x=30, y=160)
    to_entry = Entry(win)
    to_entry.place(x=100, y=160)

    Label(win, text="Date:").place(x=30, y=190)
    date_entry = Entry(win)
    date_entry.place(x=100, y=190)
    l_out = Message(win,text="",font = b1_font,anchor='w',width=800)
    
    
    bno_entry = Entry(win)
    bno_lable = Label(win,text="Choose Bno for Booking ",font = b1_font,anchor='w')
    bno_button = Button(win, text="Book",width=30,command=lambda:page_book(win,functype,modestr,from_entry.get(),to_entry.get(),"300",db,bno_entry.get()))

    # Button to submit the form
    submit_button = Button(win, text="Submit",command=lambda:search_submit(db,from_entry,to_entry,date_entry,modestr,l_out,bno_lable,bno_entry,bno_button))
    submit_button.place(x=120, y=230)
    
    l_out.place(x=30,y=260)

    pass


def button_book_handle(entry_nos,modestr,strt,dest,nos,uid,db,bno):

    db.insert_booking(entry_nos,modestr,strt,dest,nos,uid,bno)






def page_book(win,oldframe,modestr,strt,dest,uid,db,bno_number):

    functype = Frame(win,width=900,height=600)
    oldframe.forget()
    functype.tkraise()
    functype.pack()


    l_heading = Label(functype,text="BOOK",font = h_font)
    l_heading.place(x=0,y=0)


    Label(win, text="Passenger Name:").place(x=30, y=130)
    name_entry = Entry(win)
    name_entry.place(x=150, y=130)

    Label(win, text="Phone Number:").place(x=30, y=160)
    phone_entry = Entry(win)
    phone_entry.place(x=150, y=160)

    Label(win, text="Age:").place(x=30, y=190)
    age_entry = Entry(win)
    age_entry.place(x=150, y=190)

    Label(win, text="Number of Tickets:").place(x=30, y=220)
    tickets_entry = Entry(win)
    tickets_entry.place(x=150, y=220)

    # Button to book tickets
    book_button = Button(win, text="Book Tickets",command=lambda : button_book_handle(tickets_entry,modestr,strt,dest,tickets_entry.get(),uid,db,bno_number))
    book_button.place(x=150, y=260)


   

    pass





