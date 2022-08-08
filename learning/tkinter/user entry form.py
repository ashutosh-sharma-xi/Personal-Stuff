from tkinter import *
from tkinter import messagebox
import webbrowser
import mysql.connector

root = Tk()
#root.geometry('650x1000')
root.title('SIGNUP FORM')


#----------FUNCTIONS----------


import urllib.request
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False

def submit():
	# test
	if connect() == True:

		if ind_value.get() == 1:
			# file = open('user_data.txt','a')
			# file.write(f'\n{fname_value.get(),lname_value.get(),class_value.get(),school_value.get(),city_value.get(),hobby_value.get()}')
			# file.close()

			from datetime import date
			d = (dob_value.get()).split('-')
			
			name = name_value.get()
			mobile = mobile_value.get()
			email = email_value.get() 
			dob = dob_value.get()
			city = city_value.get()
			profession = profession_value.get()
			username = email
			password = name[:4]+mobile[-4:]

			try:
				connection = mysql.connector.connect(host='bft9gal92edm7sqwlrxp-mysql.services.clever-cloud.com',
		                                         database='bft9gal92edm7sqwlrxp',
		                                         user='ulysr3zv2q6ocgbr',
		                                         password='GbYRvnYn9AQO4JcIJZ5k')
				cursor = connection.cursor()
				query = f"insert into USERS values ('{username}', '{password}', '{name}', '{mobile}', '{email}', {dob}, '{city}', '{profession}');"
				cursor.execute(query)
				connection.commit()
				messagebox.showinfo("Successfully registered, Login Credentials!",  f"\nuserid: {username} \npassword: {password} \nPlease Login to continue")

			except:
				messagebox.showerror('error','Unable to process request \nIt may be because of \n1: server issues \n2: similar email already exist ')



		elif ind_value.get() == 0:
			messagebox.showerror('Error','oops! Something went wrong. Please try again')
	    

	elif connect() == False:
	    messagebox.showerror('Network Error',"Not Connected to Internet")


def enter_key(event):
	messagebox.showinfo("Query", "This form is made by Ashutosh, \nplease enter correct details in the fields.")

def devs():
	messagebox.showinfo("developer", "This project is being made by Ashutosh, \ncurrently under developement")

def login():
	from sys import exit
	import login.py
	sys.exit()
	# messagebox.showinfo("Sorry", "Currently i am working on it, try something else")


def quit():
	from sys import exit
	exit()

def my_web():
	webbrowser.open('www.google.com') # open the URL using default browser

def applaud():
	webbrowser.open('https://payments.bharatpe.in/#/8562867f024a4d35a45dc46d1720fc58')


#-----------FRAME AND HEADERS--------------
head = Label(root,text='SIGN UP FOR NEW USER',fg= 'maroon',font=('Helvetica 20 bold'))
head.pack(side=TOP,anchor='center')

frm1 = Frame(root,bg='#5c7aab',padx=80,pady=120)
frm1.pack(pady=20,anchor ='center')



#-----labels--------
lbl1 = Label(frm1,text = 'NAME',padx=20,bg='black',fg='red',font=('Helvetica 10 '))
lbl1.grid(row=0,column=0,pady= 20)

lbl2 = Label(frm1,text = 'MOBILE',padx=16,bg='black',fg='red',font=('Helvetica 10 '))
lbl2.grid(row=1,column=0,pady= 20)

lbl3 = Label(frm1,text = 'EMAIL',padx=21,bg='black',fg='red',font=('Helvetica 10 '))
lbl3.grid(row=2,column=0,pady= 20)

lbl4 = Label(frm1,text = 'BIRTH DATE',padx=4,bg='black',fg='red',font=('Helvetica 10 '))
lbl4.grid(row=3,column=0,pady= 20)

lbl5 = Label(frm1,text = 'CITY',padx=28,bg='black',fg='red',font=('Helvetica 10 '))
lbl5.grid(row=4,column=0,pady= 20)

lbl6 = Label(frm1,text = 'PROFESSION',padx=2,bg='black',fg='red',font=('Helvetica 10 '))
lbl6.grid(row=5,column=0,pady= 20)

#--------menubar--------

menubar = Menu(root)

# first in menubar
m1 = Menu(menubar,tearoff=0)
m1.add_command(label='About',command=devs)
m1.add_separator()
m1.add_command(label='Contributers',command=devs)
m1.add_separator()
m1.add_command(label='Applaud',command=applaud)
m1.add_separator()
root.config(menu=menubar)
menubar.add_cascade(label='Developer',menu=m1) 

# second in menubar
menubar.add_command(label='Help',command=my_web)


#-----variable values------
name_value= StringVar()
mobile_value= StringVar()
email_value= StringVar()
dob_value= StringVar()
city_value= StringVar()
profession_value= StringVar()
ind_value = IntVar()


#-----Entry-----------
name_entry = Entry(frm1,textvariable= name_value)
name_entry.focus()  # used to focus the cursor onto here
name_entry.insert(0, "Ashutosh Sharma") # this works as a placeholder
mobile_entry = Entry(frm1,textvariable= mobile_value)
mobile_entry.insert(0, "9755249007")
email_entry = Entry(frm1,textvariable= email_value)
email_entry.insert(0, "ashutosh0626@gmail.com")
dob_entry = Entry(frm1,textvariable= dob_value)
dob_entry.insert(0, "yyyy-mm-dd")
city_entry = Entry(frm1,textvariable= city_value)
city_entry.insert(0, "Bhopal")
profession_entry = Entry(frm1,textvariable= profession_value)
profession_entry.insert(0, "Data Scientist")
ind_entry = Checkbutton(frm1,text = 'I assure that this information is correct',variable= ind_value,padx=10,bg='white',fg='#081033',font=('Helvetica 10 italic '))

name_entry.grid(row=0,column =2)
mobile_entry.grid(row=1,column =2)
email_entry.grid(row=2,column =2)
dob_entry.grid(row=3,column =2)
city_entry.grid(row=4,column =2)
profession_entry.grid(row=5,column =2)
ind_entry.grid(row=7,column =1,sticky='e')

#-------button-----------
login_btn = Button(frm1,text = 'LOGIN',command=login,bg='grey',fg='black',font=('Helvetica 12 bold '))
login_btn.grid(row=9,column=0,pady=20)

sub_btn = Button(frm1,text = 'SUBMIT',command=submit,bg='grey',fg='black',font=('Helvetica 12 bold '))
sub_btn.grid(row=9,column=1,pady=20)

quit_btn = Button(frm1,text = 'EXIT',command=quit,bg='grey',fg='black',font=('Helvetica 12 bold '))
quit_btn.grid(row=9,column=2,pady=20)


# ------- event handling ---------

root.bind('<Control-Shift-?>',enter_key )  


root.mainloop()

