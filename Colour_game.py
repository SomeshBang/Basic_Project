from tkinter import *
import random

root = Tk()
root.title("Colour Game")
root.geometry("640x300")

main_label = Label(root,text="Click the colour you see ...! ",font=("Arial",15,"bold"))
main_label.place(relx=0.3,rely=0.03)

lst = ["Red","Yellow","Blue","Black","Aqua","Green","Purple"]

tv = StringVar()
sr = IntVar()
i = 0

def start():
    global lst
    global color
    global txt


    btn.after(1000, btn.destroy())
    color = random.choice(lst)
    main_txt = random.choice(lst)
    tv.set(main_txt)
    color = color.lower()
    txt = Label(root,textvariable=tv,font=("Arial",30,"bold"),foreground=color,borderwidth=3,relief="raised")
    txt.place(relx=0.4,rely=0.3)

def check(colo):
    global txt
    global btn
    global btne
    global i
    global sr

    scrtxt = Label(root,text="Score:",font=("Arial",15,"bold"),foreground="red")
    scrtxt.place(relx=0.05,rely=0.18)
    scr = Label(root,textvariable=sr,font=("Arial",15,"bold"),foreground="red")
    scr.place(relx=0.05,rely=0.26)

    if colo == color:
        i+=1
        sr.set(i)
        start()
    else:
        over()

def over():
    global i
    global lbl 
    global btne
    global txt

    try:
        txt.after(1000, txt.destroy())
    except:
        pass
    btn1.config(state = DISABLED)
    btn2.config(state = DISABLED)
    btn3.config(state = DISABLED)
    btn4.config(state = DISABLED)
    btn5.config(state = DISABLED)
    btn6.config(state = DISABLED)
    btn7.config(state = DISABLED)
    
    lbl = Label(root,text="Game Over ....!",font =("arial",20,"bold"),foreground="red")
    lbl.place(relx=0.35,rely=0.2)
    btn = Button(root,text = "Start", font = f,foreground="green",command = startnew)
    btn.place(relx=0.40,rely=0.35)
    btne = Button(root,text = "Exit", font = f,foreground="red",command = root.destroy)
    btne.place(relx=0.50,rely=0.35)

def startnew():
    global btn
    global btne
    global i
    global sr
    
    i = 0
    sr.set(i)
    lbl.after(1000,lbl.destroy())
    btn1.config(state = NORMAL)
    btn2.config(state = NORMAL)
    btn3.config(state = NORMAL)
    btn4.config(state = NORMAL)
    btn5.config(state = NORMAL)
    btn6.config(state = NORMAL)
    btn7.config(state = NORMAL)
    btn.after(1000, btn.destroy())
    btne.after(1000, btne.destroy())
    start()

f = "{Arial} 12"

btn = Button(root,text = "Start", font = f,foreground="green",command = start)
btn.place(relx=0.45,rely=0.3)

btn1 = Button(root,text="Red",font = f, command=lambda:check("red"))
btn1.place(relx=0.01,rely=0.78,width=90,height=40)

btn2 = Button(root,text="Yellow",font = f, command=lambda:check("yellow"))
btn2.place(relx=0.15,rely=0.78,width=90,height=40)

btn3 = Button(root,text="Blue",font = f, command=lambda:check("blue"))
btn3.place(relx=0.29,rely=0.78,width=90,height=40)

btn4 = Button(root,text="Black",font = f, command=lambda:check("black"))
btn4.place(relx=0.432,rely=0.78,width=90,height=40)

btn5 = Button(root,text="Aqua",font = f, command=lambda:check("aqua"))
btn5.place(relx=0.572,rely=0.78,width=90,height=40)

btn6 = Button(root,text="Green",font = f, command=lambda:check("green"))
btn6.place(relx=0.713,rely=0.78,width=90,height=40)

btn7 = Button(root,text="Purple",font = f, command=lambda:check("purple"))
btn7.place(relx=0.855,rely=0.78,width=90,height=40)

root.mainloop()