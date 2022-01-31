from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox

bgc = "#751aff"
root = Tk()
root.title("To Do List ")
root.geometry("730x460")
root.maxsize(width = 730, height = 460)
root.minsize(width = 730, height = 460)
root.config(bg = bgc)

def dis():
    global frame
    data = ScrolledText(root, state='disabled',bd=2,bg=bgc)
    data.place(relx=0.001,rely=0.23,width=730,height=350)
    frame = Frame(data)
    data.window_create('1.0', window=frame)

r=1
def taskadded():
    global r

    def done(stat):
        if stat == 0:
            messagebox.showinfo("Notification","Congratulations ....You did it ..!!")
        else:
            messagebox.showinfo("Notification","Keep tring ...!!")
        lb.after(1, lb.destroy())
        btncomp.after(1, btncomp.destroy())
        btndel.after(1, btndel.destroy())

    t = txt.get()
    if len(t) > 5:
        lb = Label(frame,text=t[:100])
        lb.grid(row=r,column=1,sticky=W)
        btncomp = Button(frame,text="Completed",command = lambda:done(0))
        btncomp.grid(row=r,column=2)
        btndel = Button(frame,text="Delete",command = lambda:done(1))
        btndel.grid(row=r,column=3)
        r+=1
    else:
        pass

txt = StringVar()
main_label = Label(root,text="To Do ... !!",font=(" ",20,"bold"),fg="white",bg=bgc)
main_label.place(relx=0.35,rely=0.001,width=150,height=50)

lbl = Label(root,text="Enter Task = ",font=(" ",13,"bold"),fg="white",bg=bgc)
lbl.place(relx=0.001,rely=0.13)

enty = Entry(root,textvariable=txt,bd=1,font = ("Arial",13))
enty.place(relx=0.15,rely=0.13,width=495,height=27)

btn = Button(root,text=" ADD ",font = ("Arial",10,"bold"),fg="blue", command=taskadded)
btn.place(relx=0.85,rely=0.13,height=27,width = 80)
dis()

root.mainloop()