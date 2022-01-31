from tkinter import *
from PIL import Image,ImageTk
import random
from time import sleep

root = Tk()
root.title("Dice Simulator")
root.geometry("520x420")
root.configure(bg="#FF7077")

dice = ["d1.png","d2.png","d3.png","d4.png","d5.png","d6.png"]

lbl = Label(root,text="Dice Simulator",font=("Harlow solid italic",20),bg="#FF7077",fg="#2009E9")
lbl.pack(expand=True)

img = ImageTk.PhotoImage(Image.open(random.choice(dice)))
lblimg = Label(root,image=img,bg="#FF7077")
lblimg.image = img
lblimg.pack(expand=True)

def roll():
    img = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    lblimg.configure(image=img)
    lblimg.image = img

btn = Button(root,text="Roll the Dice",font=("Calibri",15) ,command= roll,fg="#2009E9",bg="#F9ABAE")
btn.pack(ipadx=80,ipady=10,expand=True)

root.mainloop()