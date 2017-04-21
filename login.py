import tkinter as tkinter
from tkinter import *
import time
import datetime

root=Tk()
root.title("Log In Page")

root.geometry("1000x700+0+0")
Date1=StringVar()
Date1.set(time.strftime("%d/%m/%Y"))

TopFrame=Frame(root,width=1000,height=100,bd=8,bg='green',relief='raise')
TopFrame.pack(side=TOP)

#MiddleFrame=Frame(root,width=1000,height=50,bd=8,bg='green',relief='ridge')
#MiddleFrame.pack(side=)


MiddleFrame=Frame(root,width=1001,height=600,bd=8,bg='green',relief='ridge')
MiddleFrame.pack(side=LEFT,expand=True)

TopMarking=Label(MiddleFrame,text="Egerton University Mortuary Management System",width=38,bg='Green',font=('times',18,'italic'),fg='white',bd=4,relief='ridge')
TopMarking.place(x=250,y=0)

DateLabel=Entry(MiddleFrame,width=10,font=('times',18,'italic'),bg='Green',bd=4,fg='white',textvariable=Date1,relief='ridge')
DateLabel.place(x=854,y=0)

Name=Label(MiddleFrame,text="Staff Number",width=10,bg='Green',font=('times',14,'italic'),fg='white')
Name.place(x=230,y=150)

Password=Label(MiddleFrame,text="Password",width=10,bg='Green',font=('times',14,'italic'),fg='white')
Password.place(x=230,y=200) 

NameEntry=Entry(MiddleFrame,width=30,font=('times',14,'italic'),fg='black')
NameEntry.place(x=350,y=150)

PasswordEntry=Entry(MiddleFrame,width=30,font=('times',14,'italic'),fg='black',show="*")
PasswordEntry.place(x=350,y=200) 

LogInButton=Button(MiddleFrame,width=20,text="Log In",font=('times',14,'italic'),bg='Green',fg='white',relief='ridge')
LogInButton.place(x=680,y=250)

LogInButton=Button(MiddleFrame,width=20,text="Forgot Password",font=('times',14,'italic'),bg='Green',fg='white',relief='ridge')
LogInButton.place(x=680,y=300)

BottomMarking=Label(MiddleFrame,text="Transforming Lives Through Quality Education",width=38,bg='Green',font=('times',22,'italic'),fg='bisque2')
BottomMarking.place(x=200,y=450)

image1=PhotoImage(file="logo.gif")

TopLabel=Label(TopFrame,image=image1)
TopLabel.pack(side='top',fill='both',expand='yes')

root.mainloop()
