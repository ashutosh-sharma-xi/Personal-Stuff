from tkinter import *

def show():
	if robo_value.get() == 1:
		name = (f'your name is {name_value.get()}')
		pas = (f'your password is {pass_value.get()}')
		outlbl = Label(text= f'{name} {pas}')
		outlbl.grid(row=4,column=0)

	elif robo_value.get() == 0:
		outlbl = Label(text= 'Only Humans can enter input')
		outlbl.grid(row=4,column=0)


root = Tk()
root.geometry('655x400')

#==============
user = Label(root,text='USERNAME')
password = Label(root,text='PASSWORD')
user.grid()
password.grid(row=1)

#============

name_value = StringVar()
pass_value = StringVar()
robo_value = IntVar()

userentry = Entry(root,textvariable=name_value)
passentry = Entry(root,textvariable=pass_value)
robo_entry = Checkbutton(root,text = 'I am not a robot: ',variable= robo_value)

userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)
robo_entry.grid(row=3,column=1)

#=================

get = Button(text = 'get', command=show)
get.grid(row=4,column=2)

root.mainloop()







#   C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.10\\




