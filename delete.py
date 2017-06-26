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
        cursor.execute("SELECT staffid FROM users where staffid ='%s'" % (StaffEntry.get()))
        staffid = cursor.fetchone()
        staffidone = str(staffid[0])
        print(staffidone)
        if staffid is not None:
            messagebox.showinfo("SUCCESS", "USER EXISTS")
            status = True
        else:
            messagebox.showinfo("ERROR","USER DOES NOT EXIST")
            status = False
    except:
        status=False

    try:
        if status == True:
            cursor.execute("DELETE FROM users WHERE staffid = '%s'" % (StaffEntry.get()))
            conn.commit()
            print("User Deleted")
            status = True
    except:
        conn.rollback()
        print("User not deleted")
        status=False
    if status == True
        messagebox.showinfo()


root=Tk()

StaffVariable=StringVar()
PasswordVariable=StringVar()
NewPasswordVariable=StringVar()
ConfirmedPasswordVariable=StringVar()


root.geometry("1366x768+0+0")

ChangePassFrame=Frame(root, bg='Green', width=1366, height=768, bd=4, relief='ridge')
ChangePassFrame.pack()

TopLabelName=Label(ChangePassFrame, text="Change Password", bg='Green', font=('times', 14, 'italic'), fg='white')
TopLabelName.place(x=400,y=0)

StaffEntry=Entry(ChangePassFrame, font=('times', 14, 'italic'), fg='black', width=50, textvariable=StaffVariable)
StaffEntry.place(x=250,y=50)


SubmitButton=Button(ChangePassFrame, text="Submit", font=('times', 14, 'italic'), fg='Green', bd=2, relief='ridge', command=delete())
SubmitButton.place(x=900,y=550)



root.mainloop()