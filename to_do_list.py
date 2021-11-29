from tkinter import *
from tkinter.scrolledtext import ScrolledText

bgc = "#751aff"
root = Tk()
root.title("To Do List ")
root.geometry("500x400")
root.config(bg = bgc)

def btn():
    data = ScrolledText(root, state='disabled',bd=1)
    data.place(relx=0.005,rely=0.15,width=400,height=300)
    frame = Frame(data)
    text.window_create('1.0', window=frame)

main_label = Label(root,text="To Do ... !!",font=(" ",20,"bold"),fg="white",bg=bgc)
main_label.place(relx=0.35,rely=0.001,width=150,height=50)

lbl = Label(root,text="Enter Task = ",font=(" ",10,"bold"),fg="white",bg=bgc)
lbl.place(relx=0.001,rely=0.13)

enty = Entry(root,bd=1)
enty.place(relx=0.17,rely=0.13,width=200,height=20)

btn = Button(root,text=" Add ")
btn.place(relx=0.60,rely=0.13,height=23)



root.mainloop()
