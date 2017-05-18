# @AUTHOR ANDY

from tkinter import *
from tkinter import messagebox
import datetime
from datetime import time
import time
import mysql
import mysql.connector
import hashlib

##############################################
####           MYSQL CODE                #####
##############################################
conn = mysql.connector.connect(user='Andrew', password='andy', database='test', host='127.0.0.1', port='3306')
cursor = conn.cursor()


#############################################################################################################
# This function {passencrypt()} reads password entered by user then compares it to the password in the db   #
# The password entered is encrypted and compared to the encrypted password stored in the db                 #
# The function returns a hashed password                                                                    #
#############################################################################################################


## Using sha512()
def passencrypt():
    pent=PasswordEntry.get()
    pent = pent.encode('utf8')
    pword = hashlib.sha512()
    pword.update(pent)
    password = pword.hexdigest()
    print(pword)
    return password

def reset():
    NameVariable.set("")
    PasswordVariable.set("")


def authentication():
    uname = NameEntry.get()
    pword = PasswordEntry.get()
    andy = passencrypt()

    status = False
    try:
        cursor.execute("SELECT staffid FROM users where staffid ='%s'" % (NameEntry.get()))
        staffid = cursor.fetchone()
        staffid = str(staffid[0])
        print(staffid)

        if staffid is not None:
            print("cursor null")

            if uname == staffid:
                status = True

        cursor.execute("SELECT password FROM users WHERE staffid = '%s'" % (NameEntry.get()))
        password = cursor.fetchone()
        passWord = str(password[0])

        if status == True:
            print("Got password")
            if andy != passWord:
                status = False
                print("Wrong Password")
    except:
        status = False
        print("here")

    if status == True:
        messagebox.showinfo("LOGIN", "Login Successful.")
    else:
        messagebox.showinfo("LOGIN", "WRONG ID / PASSWORD")
    reset()


###############################################
####              LOGIN PAGE              #####
###############################################

root = Tk()
root.title("Egerton University Mortuary Management System")
root.geometry("1000x700+0+0")
Date1 = StringVar()
Date1.set(time.strftime("%d/%m/%Y"))

NameVariable = StringVar()
PasswordVariable = StringVar()

TopFrame = Frame(root, width=1000, height=100, bd=8, bg='green', relief='raise')
TopFrame.pack(side=TOP)

MiddleFrame = Frame(root, width=1001, height=600, bd=8, bg='green', relief='ridge')
MiddleFrame.pack(side=LEFT, expand=True)

TopMarking = Label(MiddleFrame, text="Egerton University Mortuary Management System", width=38, bg='Green',
                   font=('times', 18, 'italic'), fg='white', bd=4, relief='ridge')
TopMarking.place(x=250, y=0)

DateLabel = Entry(MiddleFrame, width=10, font=('times', 18, 'italic'), textvariable=Date1, bg='Green', bd=4, fg='white',
                  relief='ridge')
DateLabel.place(x=854, y=0)

Name = Label(MiddleFrame, text="Staff Number", width=10, bg='Green', font=('times', 14, 'italic'), fg='white')
Name.place(x=230, y=150)

Password = Label(MiddleFrame, text="Password", width=10, bg='Green', font=('times', 14, 'italic'), fg='white')
Password.place(x=230, y=200)

NameEntry = Entry(MiddleFrame, width=30, font=('times', 14, 'italic'), textvariable=NameVariable, fg='black')
NameEntry.place(x=350, y=150)

PasswordEntry = Entry(MiddleFrame, width=30, font=('times', 14, 'italic'), textvariable=PasswordVariable, fg='black',
                      show="*")
PasswordEntry.place(x=350, y=200)

LogInButton = Button(MiddleFrame, width=20, text="Log In", font=('times', 14, 'italic'), bg='Green', fg='white',
                     relief='ridge',
                     command=authentication)
LogInButton.place(x=400, y=250)

LogInButton = Button(MiddleFrame, width=20, text="Forgot Password", font=('times', 14, 'italic'), bg='Green',
                     fg='white', relief='ridge')
LogInButton.place(x=400, y=300)

BottomMarking = Label(MiddleFrame, text="Transforming Lives Through Quality Education", width=38, bg='Green',
                      font=('times', 22, 'italic'), fg='bisque2')
BottomMarking.place(x=200, y=450)

image1 = PhotoImage(file="logo.gif")

TopLabel = Label(TopFrame, image=image1)
TopLabel.pack(side='top', fill='both', expand='yes')

root.mainloop()
