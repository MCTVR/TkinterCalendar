#import stuff
from tkinter import *
import calendar
from datetime import datetime
from datetime import date
import time

#config window
root = Tk()
root.title("Calendar")
root.geometry("500x250")
root.resizable(0,0)
root.configure(background='white')

#def stuff
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

def tick():
    global timenow
    newtime=time.strftime('%H:%M:%S')
    if newtime != timenow:
        timenow= newtime
        clock.config(text=timenow)
    clock.after(200,tick)

#GUI config
lb11 = Label(root,text="Month",font=('arial',9,'bold')).place(x=5,y=0)

lb12 = Label(root,text="Year",font=('arial',9,'bold')).place(x=100,y=0)

spin1 = Spinbox(root,values=(1,2,3,4,5,6,7,8,9,10,11,12),width=4)
spin1.place(x=40,y=0)

spin2 = Spinbox(root,from_=1999,to_= 2102,width=4)
spin2.place(x=130,y=0)

btn = Button(root,text="Show",font=('arial',15,'bold'),command=show).place(x=40,y=30)
btn2 = Button(root,text="Get date now",font=('arial',15,'bold'),command=shownowtime).place(x=100,y=30)

txt = Text(root,width=35,height=10)
txt.place(x=20,y=65)

timenow = ' '

clock = Label(root,font=('arial',25))

clock.pack()

dtt = datetime.today()
Label(root, text=dtt.strftime("%d-%m-%Y"), font=('arial',45)).place(x=200,y=30)

Label(root, text="Made By Master Creeper", font=('Helvetica',15,'italic','bold')).place(x=5,y=220)

#end
tick()
mainloop()
root.mainloop()
root.mainloop()

#Made By Master Creeper