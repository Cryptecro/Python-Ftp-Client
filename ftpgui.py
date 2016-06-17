#Created By:Zachary Sylvester, Python FTP GUI
from Tkinter import *
import time
from ftplib import FTP
import os
root = Tk()
root.title("FTP_Client")
root.geometry('400x400')
def Ftpad():
	ftp = ftpt.get
	user = usert.get
	pas = past.get

connected = 0

def test():
	#print lol
	ftp = FTP('ftp.debian.org')
	print ("Checking ip")
	ftp.login
	print ("Checking Login User")
	ftp.login()
	print ("Logged In")
	ftp.retrlines('LIST')
 	

ip = StringVar()
user = StringVar()
pas = StringVar()

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

button1 = Button(root,text="Submit",command = test)

button1.grid(row=3, column=0)




root.mainloop()
