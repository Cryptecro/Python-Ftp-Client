#Created By:Zachary Sylvester, Python FTP GUI
from Tkinter import *
import sys

root = Tk()
root.title("FTP_Client")
root.geometry('400x400')
def connect(event):
	print("Connecting to Server")
def close(event):
	print("Bye!!")

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

root.mainloop()
