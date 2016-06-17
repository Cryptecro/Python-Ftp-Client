#Created By:Zachary Sylvester, Python FTP GUI
from Tkinter import *
import sys
from ftplib import FTP

root = Tk()
root.title("FTP_Client")
root.geometry('400x400')
def Ftpad():
	ftp = ftpt.get
	user = usert.get
	pas = past.get
connected = 0
if connected == 1:
	def other():
		frame = Tk()
		frame.title("Connected")
		frame.geometry('400x400')
		labelCd = Label(frame, text="cd")
else:

 	

	ip = StringVar()
	user = StringVar
	pas = StringVar

	label_1 = Label(root, text="IP_Address")#Entry text fields for info
	label_2 = Label(root, text="Username")
	label_3 = Label(root, text="Password")

	entry_1 = Entry(root,textvariable=ip) 
	entry_2 = Entry(root,textvariable=user)
	entry_3 = Entry(root,textvariable=pas)

	label_1.grid(row=0, sticky=E) #IP address text
	label_2.grid(row=1, sticky=E) #User text
	label_3.grid(row=2,	sticky=E) #password text

	entry_1.grid(row=0, column=1) #Styleing for entry
	entry_2.grid(row=1, column=1) 
	entry_3.grid(row=2, column=1)

	button1 = Button(root,text="Submit")


	root.mainloop()
