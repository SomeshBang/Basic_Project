from tkinter import *
import time
import datetime

#-----------Basic-----------
root = Tk()
root.title("Advance Clock")
root.geometry("1000x250+20+20")
root.config(bg="black")
root.maxsize(width = 1000, height=250)
fnt = "{Georgia} 18"
fnt1 = "{Century} 100"

#-----------Variables----------
t = StringVar()
d = StringVar()
sec= -1
minute=0
hour =0
runnner = False
ss=StringVar()
mm=StringVar()
hh=StringVar()
bgg="black"
fgg = "#7626FF"

#------Quit-------
def q():
    root.destroy()
#------------Stopwatch------------
def stopwatch():
    ss.set("00")
    mm.set("00")
    hh.set("00")
    def back():  #----------Back Button---------
        back_btn.destroy()
        f.destroy()

    f = Frame(root,bg=bgg)
    f.place(relx=0.0,rely=0.0,width=1000,height=1000)
    back_btn = Button(f,text="← Back",font=("Georgia",10),state="normal",bg="black",fg="red",command = back)
    back_btn.place(x=1,y=1,width=65,height=30)

    def stopwatch_count(): #--------(Starting count)------------
        global sec
        global minute
        global hour
        global runnner

        if runnner :
            sec=int(sec)+1
            if int(sec) < 60:
                ss.set(sec)
            elif int(sec)==60:
                ss.set("00")
                minute=int(minute)+1
                mm.set(minute)
                if int(minute)==60:
                    mm.set("00")
                    hour=int(hour)+1
                    hh.set(hour)
                    minute = 0
            else:
                sec = 1
                ss.set(sec)
            second_lb.after(1000,stopwatch_count)

    def start(): #-----Start------
        global runnner
        runnner = True
        start_btn['state']="disabled"
        stop_btn['state']="normal"
        rest_btn['state']="normal"
        stopwatch_count()

    def stp(): #-----Stop------
        global runnner
        runnner = False
        start_btn['state']="normal"
        stop_btn['state']="disabled"
        rest_btn['state']="normal"
        stopwatch_count()

    def rest():  #-----Reset------
        global sec
        global minute
        global hour
        global runnner
        ss.set("00")
        mm.set("00")
        hh.set("00")
        sec = 0
        minute = 0
        hour = 0
        start_btn['state']="normal"


    start_btn = Button(f,text="Start",command=start,bg="black",fg="cyan",font=("Georgia",13))
    start_btn.place(relx=0.85,rely=0.03,width=120,height=35)
    stop_btn = Button(f,text="Stop",command=stp,state="disabled",bg="black",fg="cyan",font=("Georgia",13))
    stop_btn.place(relx=0.85,rely=0.07,width=120,height=35)
    rest_btn = Button(f,text="Reset",command=rest,state="disabled",bg="black",fg="cyan",font=("Georgia",13))
    rest_btn.place(relx=0.85,rely=0.11,width=120,height=35)

    second_lb = Label(f,textvariable=ss,font = fnt1,fg=fgg,bg=bgg)
    second_lb.place(relx=0.60,rely=0.005)
    minute_lb = Label(f,textvariable=mm,font = fnt1,fg=fgg,bg=bgg)
    minute_lb.place(relx=0.40,rely=0.005)
    hour_lb = Label(f,textvariable=hh,font = fnt1,fg=fgg,bg=bgg)
    hour_lb.place(relx=0.20,rely=0.005)

    #------Labels------
    
    hour_label = Label(f,text="Hour",font=("Candara",12),fg=fgg,bg=bgg).place(x=260,y=145)
    minute__label = Label(f,text="Minute",font=("Candara",12),fg=fgg,bg=bgg).place(x=450,y=145)
    second_label = Label(f,text="Second",font=("Candara",12),fg=fgg,bg=bgg).place(x=650,y=145)
    dot_label = Label(f,text=".",font=("Candara",50),fg=fgg,bg=bgg).place(x=570,y=65)
    dobdot_lab = Label(f,text=":",font=("Candara",50),fg=fgg,bg=bgg).place(x=360,y=50)



#-------------Clock--------------
def clock():
    tm = datetime.datetime.now()
    tme = tm.strftime("%I : %M : %S  %p")
    dt = tm.strftime(" %d  %B  %Y           %A")
    t.set(tme)
    d.set(dt)
    root.after(1000,clock)

dat= Label(root,textvariable=d,bg=bgg,fg=fgg,font =("arial",30,"bold"))
dat.place(relx=0.001,rely=0.03)
tim= Label(root,textvariable=t,bg=bgg,fg=fgg,font =("arial",80,"bold"))
tim.place(relx=0.001,rely=0.3)

stopwatch_btn = Button(root,text="Stopwatch",font=fnt,bg="black",fg="cyan",command=stopwatch)
stopwatch_btn.place(x=840,y=10,width=150,height=40)

quit_btn = Button(root,text="Quit",font=fnt,bg="black",fg="red",command=q)
quit_btn.place(x=840,y=180,width=150,height=40)

clock()
root.mainloop()
