from tkinter import *
# from tkinter import messagebox

# root = Tk()
# root.geometry("300x200")

# w = Label(root, text ='GeeksForGeeks', font = "50")
# w.pack()

# messagebox.showinfo("showinfo", "Information")

# messagebox.showwarning("showwarning", "Warning")

# messagebox.showerror("showerror", "Error")

# messagebox.askquestion("askquestion", "Are you sure?")

# messagebox.askokcancel("askokcancel", "Want to continue?")

# messagebox.askyesno("askyesno", "Find the value?")


# messagebox.askretrycancel("askretrycancel", "Try again?")

# root.mainloop()



#---------------------------------------

'''root = Tk()

def gmtry():
    root.geometry(f'{ent2_value.get()}x{ent1_value.get()}')

lbl1 = Label(root,text= 'enter height')
lbl1.grid(row=0,column=0)

lbl2 = Label(root,text= 'enter width')
lbl2.grid(row=1,column=0)

ent1_value = IntVar()
ent2_value = IntVar()

ent1 = Entry(root , textvariable = ent1_value)
ent2 = Entry(root,  textvariable= ent2_value)
ent1.grid(row=0,column=1)
ent2.grid(row=1,column=1)

btn = Button(root,text='get', command= gmtry)
btn.grid(row=3,column=1)

root.mainloop()

'''

#-------------------------
'''from tkinter import *
import webbrowser

def on_url_click(event):
    selected = event.widget.nearest(event.y) # find the index near the mouse click position
    url = event.widget.get(selected)
    webbrowser.open(url) # open the URL using default browser

root = Tk()

urllist = Listbox(root, width=80, height=20)
urllist.pack()
urllist.bind('<Button-1>', on_url_click)

# insert some URLs
for url in ('http://www.google.com', 'http://www.reddit.com', 'http://www.stackoverflow.com'):
    urllist.insert(END, url)

root.mainloop()

'''
# import webbrowser
# webbrowser.open('www.google.com')




import urllib.request
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False

        
# test
if connect() == True:
    print('Connect')

elif connect() == False:
    print('Not Connected')



from tkinter import *
from tkinter import messagebox
import webbrowser
import mysql.connector

root = Tk()
#root.geometry('650x1000')
root.title('SIGNUP FORM')


 

#----------FUNCTIONS--------------
def submit():
    if ind_value.get() == 1:
        file = open('user_data.txt','a')
        file.write(f'\n{fname_value.get(),lname_value.get(),class_value.get(),school_value.get(),city_value.get(),hobby_value.get()}')
        file.close()

        connection = mysql.connector.connect(host='bft9gal92edm7sqwlrxp-mysql.services.clever-cloud.com',
                                         database='bft9gal92edm7sqwlrxp',
                                         user='ulysr3zv2q6ocgbr',
                                         password='GbYRvnYn9AQO4JcIJZ5k')
        cursor = connection.cursor()
        query ="show tables"
        cursor.execute(query)
        record = cursor.fetchmany()
        print(record)



        messagebox.showinfo("Successfully registered", "Successfully registered! Login to continue")
    elif ind_value.get() == 0:
        messagebox.showerror('Error','oops! Something went wrong. Please try again')




import urllib.request
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False
# test
print( "connected" if connect() else "no internet!" )









def enter_key(event):
    messagebox.showinfo("Query", "This form is made by Ashutosh, \nplease enter correct details in the fields.")

def devs():
    messagebox.showinfo("developer", "This project is being made by Ashutosh, \ncurrently under developement")

def login():
    messagebox.showinfo("Sorry", "Currently i am working on it, try something else")


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

frm1 = Frame(root,bg='#5c7aab',padx=150,pady=120)
frm1.pack(pady=20,anchor ='center')



#-----labels--------
lbl1 = Label(frm1,text = 'FIRSTNAME',padx=10,bg='black',fg='red',font=('Helvetica 10 '))
lbl1.grid(row=0,column=0,pady= 20)

lbl2 = Label(frm1,text = 'LASTNAME',padx=10,bg='black',fg='red',font=('Helvetica 10 '))
lbl2.grid(row=1,column=0,pady= 20)

lbl3 = Label(frm1,text = 'CLASS',padx=23,bg='black',fg='red',font=('Helvetica 10 '))
lbl3.grid(row=2,column=0,pady= 20)

lbl4 = Label(frm1,text = 'SCHOOL',padx=17,bg='black',fg='red',font=('Helvetica 10 '))
lbl4.grid(row=3,column=0,pady= 20)

lbl5 = Label(frm1,text = 'CITY',padx=28,bg='black',fg='red',font=('Helvetica 10 '))
lbl5.grid(row=4,column=0,pady= 20)

lbl6 = Label(frm1,text = 'HOBBY',padx=20,bg='black',fg='red',font=('Helvetica 10 '))
lbl6.grid(row=5,column=0,pady= 20)

#--------menubar------------

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
fname_value= StringVar()
lname_value= StringVar()
class_value= StringVar()
school_value= StringVar()
city_value= StringVar()
hobby_value= StringVar()
ind_value = IntVar()




#-----Entry-----------
fname_entry = Entry(frm1,textvariable= fname_value)
lname_entry = Entry(frm1,textvariable= lname_value)
class_entry = Entry(frm1,textvariable= class_value)
school_entry = Entry(frm1,textvariable= school_value)
city_entry = Entry(frm1,textvariable= city_value)
hobby_entry = Entry(frm1,textvariable= hobby_value)
ind_entry = Checkbutton(frm1,text = 'I assure that this information is correct',variable= ind_value,padx=10,bg='white',fg='#081033',font=('Helvetica 10 italic '))

fname_entry.grid(row=0,column =2)
lname_entry.grid(row=1,column =2)
class_entry.grid(row=2,column =2)
school_entry.grid(row=3,column =2)
city_entry.grid(row=4,column =2)
hobby_entry.grid(row=5,column =2)
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





























