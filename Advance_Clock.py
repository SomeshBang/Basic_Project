from tkinter import *
import time
import datetime

#-----------Basic-----------
root = Tk()
root.title("Clock")
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

clock()
root.mainloop()




# System
# Terminal
# Fixedsys
# Modern
# Roman
# Script
# Courier
# MS Serif
# MS Sans Serif
# Small Fonts
# Bell Gothic Std Black
# Bell Gothic Std Light
# Eccentric Std
# Stencil Std
# Tekton Pro
# Tekton Pro Cond
# Tekton Pro Ext
# Trajan Pro
# Rosewood Std Regular
# Prestige Elite Std
# Poplar Std
# Orator Std
# OCR A Std
# Nueva Std Cond
# Minion Pro SmBd
# Minion Pro Med
# Minion Pro Cond
# Mesquite Std
# Lithos Pro Regular
# Kozuka Mincho Pro R
# @Kozuka Mincho Pro R
# Kozuka Mincho Pro M
# @Kozuka Mincho Pro M
# Kozuka Mincho Pro L
# @Kozuka Mincho Pro L
# Kozuka Mincho Pro H
# @Kozuka Mincho Pro H
# Kozuka Mincho Pro EL
# @Kozuka Mincho Pro EL
# Kozuka Mincho Pro B
# @Kozuka Mincho Pro B
# Kozuka Gothic Pro R
# @Kozuka Gothic Pro R
# Kozuka Gothic Pro M
# @Kozuka Gothic Pro M
# Kozuka Gothic Pro L
# @Kozuka Gothic Pro L
# Kozuka Gothic Pro H
# @Kozuka Gothic Pro H
# Kozuka Gothic Pro EL
# @Kozuka Gothic Pro EL
# Kozuka Gothic Pro B
# @Kozuka Gothic Pro B
# Hobo Std
# Giddyup Std
# Cooper Std Black
# Charlemagne Std
# Chaparral Pro
# Brush Script Std
# Blackoak Std
# Birch Std
# Adobe Garamond Pro
# Adobe Garamond Pro Bold
# Adobe Kaiti Std R
# @Adobe Kaiti Std R
# Adobe Heiti Std R
# @Adobe Heiti Std R
# Adobe Fangsong Std R
# @Adobe Fangsong Std R
# Adobe Caslon Pro
# Adobe Caslon Pro Bold
# Adobe Arabic
# Adobe Devanagari
# Adobe Hebrew
# Adobe Ming Std L
# @Adobe Ming Std L
# Adobe Myungjo Std M
# @Adobe Myungjo Std M
# Adobe Song Std L
# @Adobe Song Std L
# Kozuka Gothic Pr6N B
# @Kozuka Gothic Pr6N B
# Kozuka Gothic Pr6N EL
# @Kozuka Gothic Pr6N EL
# Kozuka Gothic Pr6N H
# @Kozuka Gothic Pr6N H
# Kozuka Gothic Pr6N L
# @Kozuka Gothic Pr6N L
# Kozuka Gothic Pr6N M
# @Kozuka Gothic Pr6N M
# Kozuka Gothic Pr6N R
# @Kozuka Gothic Pr6N R
# Kozuka Mincho Pr6N B
# @Kozuka Mincho Pr6N B
# Kozuka Mincho Pr6N EL
# @Kozuka Mincho Pr6N EL
# Kozuka Mincho Pr6N H
# @Kozuka Mincho Pr6N H
# Kozuka Mincho Pr6N L
# @Kozuka Mincho Pr6N L
# Kozuka Mincho Pr6N M
# @Kozuka Mincho Pr6N M
# Kozuka Mincho Pr6N R
# @Kozuka Mincho Pr6N R
# Letter Gothic Std
# Minion Pro
# Myriad Hebrew
# Myriad Pro
# Myriad Pro Cond
# Myriad Pro Light
# Rosewood Std Fill
# Marlett
# Arial
# Arabic Transparent
# Arial Baltic
# Arial CE
# Arial CYR
# Arial Greek
# Arial TUR
# Batang
# @Batang
# BatangChe
# @BatangChe
# Gungsuh
# @Gungsuh
# GungsuhChe
# @GungsuhChe
# Courier New
# Courier New Baltic
# Courier New CE
# Courier New CYR
# Courier New Greek
# Courier New TUR
# DaunPenh
# DokChampa
# Estrangelo Edessa
# Euphemia
# Gautami
# Vani
# Gulim
# @Gulim
# GulimChe
# @GulimChe
# Dotum
# @Dotum
# DotumChe
# @DotumChe
# Impact
# Iskoola Pota
# Kalinga
# Kartika
# Khmer UI
# Lao UI
# Latha
# Lucida Console
# Malgun Gothic
# @Malgun Gothic
# Mangal
# Meiryo
# @Meiryo
# Meiryo UI
# @Meiryo UI
# Microsoft Himalaya
# Microsoft JhengHei
# @Microsoft JhengHei
# Microsoft YaHei
# @Microsoft YaHei
# MingLiU
# @MingLiU
# PMingLiU
# @PMingLiU
# MingLiU_HKSCS
# @MingLiU_HKSCS
# MingLiU-ExtB
# @MingLiU-ExtB
# PMingLiU-ExtB
# @PMingLiU-ExtB
# MingLiU_HKSCS-ExtB
# @MingLiU_HKSCS-ExtB
# Mongolian Baiti
# MS Gothic
# @MS Gothic
# MS PGothic
# @MS PGothic
# MS UI Gothic
# @MS UI Gothic
# MS Mincho
# @MS Mincho
# MS PMincho
# @MS PMincho
# MV Boli
# Microsoft New Tai Lue
# Nyala
# Microsoft PhagsPa
# Plantagenet Cherokee
# Raavi
# Segoe Script
# Segoe UI
# Segoe UI Semibold
# Segoe UI Light
# Segoe UI Symbol
# Shruti
# SimSun
# @SimSun
# NSimSun
# @NSimSun
# SimSun-ExtB
# @SimSun-ExtB
# Sylfaen
# Microsoft Tai Le
# Times New Roman
# Times New Roman Baltic
# Times New Roman CE
# Times New Roman CYR
# Times New Roman Greek
# Times New Roman TUR
# Tunga
# Vrinda
# Shonar Bangla
# Microsoft Yi Baiti
# Tahoma
# Microsoft Sans Serif
# Angsana New
# Aparajita
# Cordia New
# Ebrima
# Gisha
# Kokila
# Leelawadee
# Microsoft Uighur
# MoolBoran
# Symbol
# Utsaah
# Vijaya
# Wingdings
# Andalus
# Arabic Typesetting
# Simplified Arabic
# Simplified Arabic Fixed
# Sakkal Majalla
# Traditional Arabic
# Aharoni
# David
# FrankRuehl
# Levenim MT
# Miriam
# Miriam Fixed
# Narkisim
# Rod
# FangSong
# @FangSong
# SimHei
# @SimHei
# KaiTi
# @KaiTi
# AngsanaUPC
# Browallia New
# BrowalliaUPC
# CordiaUPC
# DilleniaUPC
# EucrosiaUPC
# FreesiaUPC
# IrisUPC
# JasmineUPC
# KodchiangUPC
# LilyUPC
# DFKai-SB
# @DFKai-SB
# Lucida Sans Unicode
# Arial Black
# Calibri
# Cambria
# Cambria Math
# Candara
# Comic Sans MS
# Consolas
# Constantia
# Corbel
# Franklin Gothic Medium
# Gabriola
# Georgia
# Palatino Linotype
# Segoe Print
# Trebuchet MS
# Verdana
# Webdings
# Haettenschweiler
# MS Outlook
# Book Antiqua
# Century Gothic
# Bookshelf Symbol 7
# MS Reference Sans Serif
# MS Reference Specialty
# Bradley Hand ITC
# Freestyle Script
# French Script MT
# Juice ITC
# Kristen ITC
# Lucida Handwriting
# Mistral
# Papyrus
# Pristina
# Tempus Sans ITC
# Garamond
# Monotype Corsiva
# Agency FB
# Arial Rounded MT Bold
# Blackadder ITC
# Bodoni MT
# Bodoni MT Black
# Bodoni MT Condensed
# Bookman Old Style
# Calisto MT
# Castellar
# Century Schoolbook
# Copperplate Gothic Bold
# Copperplate Gothic Light
# Curlz MT
# Edwardian Script ITC
# Elephant
# Engravers MT
# Eras Bold ITC
# Eras Demi ITC
# Eras Light ITC
# Eras Medium ITC
# Felix Titling
# Forte
# Franklin Gothic Book
# Franklin Gothic Demi
# Franklin Gothic Demi Cond
# Franklin Gothic Heavy
# Franklin Gothic Medium Cond
# Gigi
# Gill Sans MT
# Gill Sans MT Condensed
# Gill Sans Ultra Bold
# Gill Sans Ultra Bold Condensed
# Gill Sans MT Ext Condensed Bold
# Gloucester MT Extra Condensed
# Goudy Old Style
# Goudy Stout
# Imprint MT Shadow
# Lucida Sans
# Lucida Sans Typewriter
# Maiandra GD
# OCR A Extended
# Palace Script MT
# Perpetua
# Perpetua Titling MT
# Rage Italic
# Rockwell
# Rockwell Condensed
# Rockwell Extra Bold
# Script MT Bold
# Tw Cen MT
# Tw Cen MT Condensed
# Tw Cen MT Condensed Extra Bold
# Algerian
# Baskerville Old Face
# Bauhaus 93
# Bell MT
# Berlin Sans FB
# Berlin Sans FB Demi
# Bernard MT Condensed
# Bodoni MT Poster Compressed
# Britannic Bold
# Broadway
# Brush Script MT
# Californian FB
# Centaur
# Chiller
# Colonna MT
# Cooper Black
# Footlight MT Light
# Harlow Solid Italic
# Harrington
# High Tower Text
# Jokerman
# Kunstler Script
# Lucida Bright
# Lucida Calligraphy
# Lucida Fax
# Magneto
# Matura MT Script Capitals
# Modern No. 20
# Niagara Engraved
# Niagara Solid
# Old English Text MT
# Onyx
# Parchment
# Playbill
# Poor Richard
# Ravie
# Informal Roman
# Showcard Gothic
# Snap ITC
# Stencil
# Viner Hand ITC
# Vivaldi
# Vladimir Script
# Wide Latin
# Century
# Wingdings 2
# Wingdings 3
# Arial Unicode MS
# @Arial Unicode MS
# Arial Narrow
# Rupee Foradian
# Rupee
# DevLys 010
# Calibri Light
# Monoton
# Ubuntu Medium
# Ubuntu
# Ubuntu Light
# Yatra One
# HelvLight
# Lato
# Great Vibes