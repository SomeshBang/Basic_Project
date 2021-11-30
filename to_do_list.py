from tkinter import *
from tkinter.scrolledtext import ScrolledText

bgc = "#751aff"
root = Tk()
root.title("To Do List ")
root.geometry("500x400")
root.config(bg = bgc)

def dis():
    global frame
    data = ScrolledText(root, state='disabled',bd=2,bg=bgc)
    data.place(relx=0.001,rely=0.23,width=496,height=300)
    frame = Frame(data)
    data.window_create('1.0', window=frame)

r=1
def taskadded():
    global r
    t = txt.get()
    lb = Label(frame,text=t)
    lb.grid(row=r,column=1,sticky=W)
    btncomp = Button(frame,text="Completed")
    btncomp.grid(row=r,column=2)
    btndel = Button(frame,text="Delete")
    btndel.grid(row=r,column=3)
    r+=1


txt = StringVar()
main_label = Label(root,text="To Do ... !!",font=(" ",20,"bold"),fg="white",bg=bgc)
main_label.place(relx=0.35,rely=0.001,width=150,height=50)

lbl = Label(root,text="Enter Task = ",font=(" ",10,"bold"),fg="white",bg=bgc)
lbl.place(relx=0.001,rely=0.13)

enty = Entry(root,textvariable=txt,bd=1)
enty.place(relx=0.17,rely=0.13,width=200,height=20)

btn = Button(root,text=" Add ",command=taskadded)
btn.place(relx=0.60,rely=0.13,height=23)
dis()



root.mainloop()
