from tkinter import *
from tkinter import font
from tkinter.scrolledtext import ScrolledText

root = Tk()
root.title("Font of Tkinter")
root.geometry("1180x700")
fnt = font.families()
r=1
c=1

text = ScrolledText(root, state='disabled',bg="white")
text.place(relx=0.001,rely=0.001,width=1180,height=700)
frame = Frame(text,bg="white")
text.window_create('1.0', window=frame)

for i in fnt:
    if r>100:
        r=1
        c+=1

    lb = Label(frame,text="12345 Font check  = "+i,font=(i,10),bg="white")
    lb.grid(row=r,column=c)
    r+=1
root.mainloop()