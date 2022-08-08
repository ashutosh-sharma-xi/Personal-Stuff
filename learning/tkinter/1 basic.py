from tkinter import *
from PIL import Image,ImageTk

gui_root = Tk() # firstly we need to create an instance of Tk() class
# all code is here

gui_root.geometry('600x400')
gui_root.title('A.P.J Abdul Kalam')
#gui_root.maxsize(1200,800)
gui_root.minsize(600,300)

# for jpg images ( if there is png file you just have to pass it in image in Label method as Label(image = img_png ) and then pack it)
img_jpg = Image.open('C:\\Users\\Administrator\\Desktop\\aa.jpg')
img_png = ImageTk.PhotoImage(img_jpg)


# label and its attributes 
# font1 : sets the font
# 1: font = ( 'Ariel 19 bold')
# 2: font = ('ariel',19,'bold')
# text : sets the text
# bd : background
# fg: foreground
# padx : x padding
# pady : y padding
# relief : border styling SUNKEN, GROOVE , RIDGE, RAISED


Design = Label(text = '''Avul Pakir Jainulabdeen Abdul Kalam was an Indian aerospace scientist \nwho served as the 11th president of India from 2002 to 2007. He was born and \nraised in Rameswaram, Tamil Nadu and studied physics and aerospace engineering.''' , bg= '#abc123', font = 'TimesNewRoman 18 bold',
	fg = 'white', padx = 80,pady = 50,relief = GROOVE, borderwidth = 5
	)

# important pack() attributes
#Design.pack(side=BOTTOM, anchor ="sw", fill=X)
Design.pack(side=LEFT, fill=X, padx=14, pady=14)


gui_root.mainloop() # this is the last method after the logic where it remembers all the code and execute it

