from tkinter import *
import mysql.connector
from tkinter import messagebox

try:
    conn = mysql.connector.connect(user='Andrew', password='andy', database='test', host='127.0.0.1', port='3306')
    cursor = conn.cursor()
except:
    raise ValueError("Contact System Admin. Database Offline")


def delete():
    status = False
    try:
        if StaffEntry.get() != "":
            status = True
        elif StaffEntry.get() == "":
            messagebox.showinfo("ERROR","STAFF ID FIELD CANNOT BE EMPTY")
            status=False
    except:
        status=False
    try:
        cursor.execute("SELECT staffid FROM users where staffid ='%s'" % (StaffEntry.get()))
        staffid = cursor.fetchone()

        if staffid is not None:
            print("User exists")
            status = True
        else:
            messagebox.showinfo("ERROR","USER DOES NOT EXIST")
            status = False
    except:
        status=False

    try:
        if status == True:
            cursor.execute("SELECT enum FROM users WHERE staffid = '%s'"% (StaffEntry.get()))
            enm=cursor.fetchone()
            enm=str(enm[0])
            if enm == 'Y':
                messagebox.showinfo("ERROR","ADMIN CANNOT BE DELETED")
                status = False
            elif enm == 'N':
                print("Normal user")
                status = True
    except:
        status = False



    try:
        if status == True:
            cursor.execute("DELETE FROM users WHERE staffid = '%s'" % (StaffEntry.get()))
            conn.commit()
            messagebox.showinfo("SUCCESS", "USER DELETED")
            print("User Deleted")
    except:
        if status == False:
            conn.rollback()
            print("User not deleted")
            messagebox.showinfo("Error", "User was not deleted")



root=Tk()

StaffVariable=StringVar()
PasswordVariable=StringVar()
NewPasswordVariable=StringVar()
ConfirmedPasswordVariable=StringVar()


root.geometry("1366x768+0+0")

ChangePassFrame=Frame(root, bg='Green', width=1366, height=768, bd=4, relief='ridge')
ChangePassFrame.pack()

TopLabelName=Label(ChangePassFrame, text="DELETE USER", bg='Green', font=('times', 18, 'italic'), fg='white')
TopLabelName.place(x=400,y=200)

NameLabel=Label(ChangePassFrame, bg='green', text="STAFF ID", fg='white', font=('times', 14, 'italic'))
NameLabel.place(x=50,y=300)

StaffEntry=Entry(ChangePassFrame, font=('times', 14, 'italic'), fg='black', width=50, textvariable=StaffVariable)
StaffEntry.place(x=250,y=300)


SubmitButton=Button(ChangePassFrame, text="Submit", font=('times', 14, 'italic'), fg='Green', bd=2, relief='ridge', command=delete)
SubmitButton.place(x=700,y=400)



root.mainloop()