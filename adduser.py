# ADD NEW USER ##

from tkinter import *
from tkinter import messagebox
import mysql.connector
import hashlib

###############################################
####              MYSQL CODE              #####
###############################################

conn = mysql.connector.connect(user='Andrew', password='andy', database='test', host='127.0.0.1', port='3306')
cursor = conn.cursor()


def reset():
    NameVariable.set("")
    PasswordVariable.set("")
    EmailVariable.set("")
    StaffVariable.set("")
    ConfPasswordVariable.set("")

# Encrypt New password
def newPasscrypt():
    pent=PasswordEntry.get()
    pent=pent.encode('utf8')
    pword=hashlib.sha512()
    pword.update(pent)
    password=pword.hexdigest()

    return password


# Encrypt Confirmed Password
def newPassConfcrypt():
    pent=ConfirmPasswordEntry.get()
    pent=pent.encode('utf8')
    pword=hashlib.sha512()
    pword.update(pent)
    password=pword.hexdigest()

    return password


def addUser():
    status = False
    global staffid
    npass=newPasscrypt()
    ncpass=newPassConfcrypt()
    sget = StaffIDEntry.get()
    nget=NameEntry.get()
    pget=PasswordEntry.get()
    cpget=ConfirmPasswordEntry.get()
    eget=EmailEntry.get()

    try:
        if sget != "":
            print(sget)
            status = True
        elif sget == "":
            print("Blank Name Field")
            messagebox.showinfo("ERROR", "STAFF ID CANNOT BE BLANK")
            status = False

    except:
        status = False

    try:
        if status == True:
            cursor.execute("SELECT staffid FROM users where staffid ='%s'" % (StaffIDEntry.get()))
            staffid = cursor.fetchone()
            if staffid is None:
                print("empty id")
                status = True
            elif staffid is not None:
                messagebox.showinfo("ERROR", "STAFF ID ALREADY EXIT")
                status = False
    except:
        messagebox.showinfo("ERROR","STAFF ID ALREADY EXISTS")
        status = False

    try:
        if status == True:
            if nget != '':
                print("Name Gotten")
                status = True
            elif nget == '':
                print("No Name")
                messagebox.showinfo("ERROR", "NAME FIELD CANNOT BE EMPTY")
                status = False
    except:
        status = False

    try:
        if status == True:
            if eget != "":
                print(eget)
                status = True

            elif eget == "":
                print("Blank Email Field")
                messagebox.showinfo("ERROR", "EMAIL FIELD CANNOT BE BLANK")
                status = False

    except:
        status = False

    try:
        if status == True:
            if pget != '':
                print(npass)
                status = True
            elif pget == '':
                print("No Password Entered")
                messagebox.showinfo("ERROR", "PASSWORD FIELD CANNOT BE EMPTY")
                status = False
    except:
        status = False

    try:
        if status == True:
            if cpget != '':
                print(ncpass)
                status = True
            elif cpget == '':
                print("Confirmed password not entered")
                messagebox.showinfo("ERROR", "CONFIRM PASSWORD FIELD CANNOT BE EMPTY")
                status = False
    except:
        status = False

    try:
        if status == True:
            if npass == ncpass:
                cursor.execute("""INSERT INTO users(staffid, 
                    name, password, email) 
                    VALUES('%s','%s','%s','%s')""" % (
                    sget, nget, ncpass, EmailEntry.get()))
                conn.commit()
                print("User Added")
                conn.close()
                print("Connection Closed")
                status = True
            elif npass != ncpass:
                messagebox.showinfo("ERROR", "PASSWORDS DO NOT MATCH")
                print("No changes committed to db")
                conn.rollback()
                status = False
    except:
        status = False

    try:
        if status == True:
            messagebox.showinfo("SUCCESS", "NEW USER ADDED")
    except:
        if status == False:
            messagebox.showinfo("ERROR", "USER NOT ADDED")
    #reset()

###############################################
####              INTERFACE               #####
###############################################
root=Tk()

NameVariable=StringVar()
PasswordVariable=StringVar()
EmailVariable=StringVar()
StaffVariable=StringVar()
ConfPasswordVariable=StringVar()

root.geometry("1000x700+0+0")
Frame1=Frame(root,bg='Green',width=1000,height=700,bd=4,relief='ridge')
Frame1.pack()
#------------------------------------------Labels--------------------------------------------------------
TopLabel=Label(Frame1,text="Add User",bg='Green',font=('times',14,'italic'),fg='white')
TopLabel.place(x=400,y=0)

StaffIDLabel=Label(Frame1,text="Staff ID",bg='Green',font=('times',14,'italic'),fg='white')
StaffIDLabel.place(x=50,y=50)

NameLabel=Label(Frame1,text="Name",bg='Green',font=('times',14,'italic'),fg='white')
NameLabel.place(x=50,y=150)

EmailLabel=Label(Frame1,text="Email",bg='Green',font=('times',14,'italic'),fg='white')
EmailLabel.place(x=50,y=250)

PasswordLabel=Label(Frame1,text="Password",bg='Green',font=('times',14,'italic'),fg='white')
PasswordLabel.place(x=50,y=350)

ConfirmPasswordLabel=Label(Frame1,text="Confirm Password",bg='Green',font=('times',14,'italic'),fg='white')
ConfirmPasswordLabel.place(x=50,y=450)

#------------------------------------------Entries----------------------------------------------------------
StaffIDEntry=Entry(Frame1,font=('times',14,'italic'),fg='black',width=50,textvariable=StaffVariable)
StaffIDEntry.place(x=250,y=50)

NameEntry=Entry(Frame1,font=('times',14,'italic'),fg='black',width=50,textvariable=NameVariable)
NameEntry.place(x=250,y=150)

EmailEntry=Entry(Frame1,font=('times',14,'italic'),fg='black',width=50,textvariable=EmailVariable)
EmailEntry.place(x=250,y=250)

PasswordEntry=Entry(Frame1,font=('times',14,'italic'),fg='black',width=50,textvariable=PasswordVariable,show='*')
PasswordEntry.place(x=250,y=350)

ConfirmPasswordEntry=Entry(Frame1,font=('times',14,'italic'),fg='black',width=50,textvariable=ConfPasswordVariable,show='*')
ConfirmPasswordEntry.place(x=250,y=450)

ButtonSubmit=Button(Frame1,text="Submit",font=('times',14,'italic'),fg='Green',bd=2,relief='ridge',command=addUser)
ButtonSubmit.place(x=900,y=550)

root.mainloop()