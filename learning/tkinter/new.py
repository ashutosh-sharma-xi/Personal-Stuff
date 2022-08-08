from tkinter import *
from PIL import Image,ImageTk
import sys

head = 'INTRODUCTION'
name = 'Tkinter'
about = "Hey! my name is ashutosh sharma\nThis is a Tkinter tutorial\n Tkinter is Python's de-facto standard \nGUI (Graphical User Interface) package. \nIt is a thin object-oriented layer \non top of Tcl/Tk. Tkinter is not \nthe only GuiProgramming toolkit for Python."

def tell_more():
	lbl_about = Label(frm3,text=about, bg='black',fg= 'orange',font = ('TimesNewRoman 15 bold' ))
	lbl_about.pack(fill = X,side=BOTTOM, anchor = 'center')

def quit():
	sys.exit()

ui = Tk()

ui.geometry('1100x600')
ui.title('learning framing')

#=====FRAMES=====
frm2= Frame(ui,borderwidth=6,relief=RIDGE,bg='#ffe042')
frm2.pack(side=TOP)

frm1 = Frame(ui,borderwidth=5,relief=RIDGE,bg='#ffe042')
frm1.pack(fill=Y,side=LEFT)

frm3 = Frame(ui,borderwidth=6,relief=RIDGE,bg="black")
frm3.pack(fill = Y ,side=RIGHT)

#=====labels=====
lbl= Label(frm1,text=name,bg='#ffe042',fg='black',font=('TimesNewRoman 18 italic'))
lbl.pack(pady=100)

lbl = Label(frm2,text=head,bg='#ffe042',fg='#e71989',font=('TimesNewRoman 20 bold' ),padx=720)
lbl.pack(padx=40)

lbl1 = Label(frm3,text='To know more click on tell more',bg='blue',fg='white',font=('TimesNewRoman 20 bold' ),padx=720)
lbl1.pack(side = TOP)

btn1 = Button(frm3,text = 'EXIT',fg='red',bg='black',font=('TimesNewRoman 15 bold' ),command=quit)
btn1.pack(side = RIGHT,padx=80)

btn2 = Button(frm3,text = 'TELL MORE',fg='red',bg='black',font=('TimesNewRoman 15 bold' ),command=tell_more)
btn2.pack(side = LEFT,padx=80)



ui.mainloop()










