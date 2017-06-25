from tkinter import *
import mysql.connector
import hashlib
from tkinter import messagebox
###############################################
####              MYSQL CODE              #####
###############################################

conn = mysql.connector.connect(user='Andrew', password='andy', database='test', host='127.0.0.1', port='3306')
cursor = conn.cursor()

def reset():
    StaffVariable.set("")
    PasswordVariable.set("")
    NewPasswordVariable.set("")
    ConfirmedPasswordVariable.set("")

# Encrypt Confirmed New Password.
def newPassConfcrypt():
    pent=ConfirmPassEntry.get()
    pent=pent.encode('utf8')
    pword=hashlib.sha512()
    pword.update(pent)
    password=pword.hexdigest()
    print(pword)
    return password


# Encrypt New password
def newPasscrypt():
    pent=NewPassEntry.get()
    pent=pent.encode('utf8')
    pword=hashlib.sha512()
    pword.update(pent)
    password=pword.hexdigest()
    print(pword)
    return password

#############################################################################################################
# This function {passencrypt()} reads password entered by user then compares it to the password in the db   #
# The password entered is encrypted and compared to the encrypted password stored in the db                 #
# The function returns a hashed password                                                                    #
#############################################################################################################
## Using sha512()
def passencrypt():
    pent=OldPassEntry.get()
    pent = pent.encode('utf8')
    pword = hashlib.sha512()
    pword.update(pent)
    password = pword.hexdigest()
    print(pword)
    return password

def changepass():
    uname=StaffEntry.get()
    andy=passencrypt()
    status = False
    newpassword=newPasscrypt()
    newconfirmedpassword=newPassConfcrypt()

    try:
        if uname != '':
            print(uname)
            status = True
        elif uname == '':
            print("Blank staff id")
            messagebox.showinfo("ERROR","STAFF ID FIELD CANNOT BE BLANK")
            status = False
    except:
        status = False

    try:
        if status == True:
            cursor.execute("SELECT staffid FROM users where staffid ='%s'" % (StaffEntry.get()))
            staffid = cursor.fetchone()
            staffidone = str(staffid[0])
            print(staffidone)

            if staffidone is not None:
                print("cursor null")
            if uname == staffid:
                status = True
            elif uname != staffidone:
                print("User does not exist.")
                messagebox.showinfo("ERROR", "USER DOES NOT EXISTS")
                status == False
    except:
        if staffid is None:
            messagebox.showinfo()
        status = False
        print("here")


    try:
        if status == True:
            if OldPassEntry.get() != '':
                print("Got existing  Password")
                status = True
            elif OldPassEntry.get() == '':
                print("Current Pass empty")
                messagebox.showinfo("Error", "Old password field cannot be empty!")
                status = False
    except:
        status = False

    try:
        if status == True:
            cursor.execute("SELECT password FROM users WHERE staffid = '%s'" % (StaffEntry.get()))
            password = cursor.fetchone()
            passWord = str(password[0])

            print("Got password")
            if andy == passWord:
                status = True
                print("Correct Password")
            elif andy != passWord:
                messagebox.showinfo("Error", "Old Password entered does not match the old password!")
                status = False
                print("More")
    except:
        status=False
        print("more")


    try:
        if status == True:
            if NewPassEntry.get() != '':
                print("Got new password")
                status = True
            elif NewPassEntry.get() == '':
                print("New pass not entered")
                messagebox.showinfo("Error", "New password field cannot be empty!")
                status = False
    except:
        status = False

    try:
        if status == True:
            if ConfirmPassEntry.get() != '':
                print("Got confirmed password")
                status = True
            elif ConfirmPassEntry.get() == '':
                print("Confirmed password not entered")
                messagebox.showinfo("Error", "Confirmed password field cannot be empty!")
                status = False
    except:
        status = False

    try:
        if status == True:
            if newpassword == newconfirmedpassword:
                print("Matching Passwords")
                status = True
            elif newpassword != newconfirmedpassword:
                print("Passwords do not match")
                status = False
                messagebox.showinfo("Error", "New and Confirmed do not match!")


    except:
        status = False
        print("No Changes made")

    try:
        if status == True:
            cursor.execute("UPDATE users SET password = '%s' WHERE staffid = '%s'" % (newconfirmedpassword, StaffEntry.get()))
            conn.commit()
            print("Password Changed")
            conn.close()

    except:
        status=False
        conn.rollback()
        print("No Change")

    try:
        if status == True:
            messagebox.showinfo("PASSWORD", "PASSWORD CHANGED")
    except:
        if status == False:
            messagebox.showinfo("PASSWORD", "PASSWORD NOT CHANGED")
    #reset()



###############################################
####              INTERFACE               #####
###############################################
root=Tk()

StaffVariable=StringVar()
PasswordVariable=StringVar()
NewPasswordVariable=StringVar()
ConfirmedPasswordVariable=StringVar()


root.geometry("1000x700+0+0")

Frame2=Frame(root,bg='Green',width=1000,height=700,bd=4,relief='ridge')
Frame2.pack()

TopLabelName=Label(Frame2,text="Change Password",bg='Green',font=('times',14,'italic'),fg='white')
TopLabelName.place(x=400,y=0)


NameLabel=Label(Frame2,bg='green',text="STAFF ID",fg='white',font=('times',14,'italic'))
NameLabel.place(x=50,y=50)

OldPassLabel=Label(Frame2,text="Old Password",bg='Green',font=('times',14,'italic'),fg='white')
OldPassLabel.place(x=50,y=150)

NewPassLabel=Label(Frame2,text="New Password",bg='Green',font=('times',14,'italic'),fg='white')
NewPassLabel.place(x=50,y=250)

ConfirmPassLabel=Label(Frame2,text="Confirm Password",bg='Green',font=('times',14,'italic'),fg='white')
ConfirmPassLabel.place(x=50,y=350)


StaffEntry=Entry(Frame2,font=('times',14,'italic'),fg='black',width=50,textvariable=StaffVariable)
StaffEntry.place(x=250,y=50)

OldPassEntry=Entry(Frame2,font=('times',14,'italic'),fg='black',width=50,textvariable=PasswordVariable,show='*')
OldPassEntry.place(x=250,y=150)

NewPassEntry=Entry(Frame2,font=('times',14,'italic'),fg='black',width=50,textvariable=NewPasswordVariable,show='*')
NewPassEntry.place(x=250,y=250)

ConfirmPassEntry=Entry(Frame2,font=('times',14,'italic'),fg='black',width=50,textvariable=ConfirmedPasswordVariable,show='*')
ConfirmPassEntry.place(x=250,y=350)

SubmitButton=Button(Frame2,text="Submit",font=('times',14,'italic'),fg='Green',bd=2,relief='ridge',command=changepass)
SubmitButton.place(x=900,y=550)



root.mainloop()
