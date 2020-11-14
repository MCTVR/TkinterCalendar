from tkinter import *
import calendar
from datetime import datetime
import time

root = Tk()
root.title("Calendar")
root.geometry("450x250")
root.resizable(0,0)
root.configure(background='white')

def show():
    a = int(spin1.get())
    b = int(spin2.get())
    cal = calendar.month(b,a)
    txt.delete(0.0,END)
    txt.insert(INSERT,cal)

def shownowtime():
    dt = datetime.today()
    spin1.delete(0,END)
    spin2.delete(0,END)
    spin1.insert(INSERT,int(dt.month))
    spin2.insert(INSERT,int(dt.year))
    show()

def tick():
    global timenow
    newtime=time.strftime('%H:%M:%S')
    if newtime != timenow:
        timenow= newtime
        clock.config(text=timenow)
    clock.after(200,tick)

lb11 = Label(root,text="Month",font=('arial',9,'bold')).place(x=5,y=0)

lb12 = Label(root,text="Year",font=('arial',9,'bold')).place(x=100,y=0)

spin1 = Spinbox(root,values=(1,2,3,4,5,6,7,8,9,10,11,12),width=4)
spin1.place(x=40,y=0)

spin2 = Spinbox(root,from_=1999,to_= 2112,width=4)
spin2.place(x=130,y=0)

btn = Button(root,text="Show",font=('helvetica',15,'bold', ), fg="blue", command=show).place(x=30,y=30)
btn2 = Button(root,text="Show date now",font=('helvetica',15,'bold'),fg="royalblue", command=shownowtime).place(x=80,y=30)

txt = Text(root,width=30,height=10)
txt.place(x=1,y=65)

timenow = ' '

clock = Label(root,font=('helvetica',40),fg="red")
clock.place(x=280,y=35)

dtt = datetime.today()
Label(root, text=dtt.strftime("%d-%m-%Y"), font=('helvetica',43), fg="#424ef5").place(x=220,y=90)

Label(root, text="MCTVR V1.1", font=('Helvetica',15,'italic','bold'), fg="#42f5e6").place(x=5,y=220)

tick()
mainloop()
root.mainloop()
