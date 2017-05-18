from tkinter import *
from tkinter.ttk import Treeview
import time
import datetime
from tkinter import messagebox
import mysql.connector

root=Tk()
root.title("Log In Page")

root.geometry("1000x700+0+0")
root.resizable(0,0)
root.iconbitmap(default="morgue.ico")

cnx=mysql.connector.connect(user='root',host='127.0.0.1',database='bodies')
cursor=cnx.cursor(buffered=True)

Frame1=Frame(root,width=1000,height=700)
Frame1.pack()

Frame2=Frame(root,width=1000,height=700)
#Frame2.pack()

Frame3=Frame(root,width=1000,height=700)
#Frame3.pack()

Frame4=Frame(root,width=1000,height=700)
#Frame4.pack()

Frame5=Frame(root,width=1000,height=700)
#Frame4.pack()

#Frame5=Frame(root,width=1000,height=700)
#Frame5.pack()
BodyWash=IntVar()
BodyEmbalm=IntVar()
BodyVIP=IntVar()
BodyFlower=IntVar()
BodyOther=IntVar()
BodyCoffin=IntVar()
BodyHearse=IntVar()
BodyTent=IntVar()
BodyPostMortem=IntVar()
BodyWash.set(0)
BodyEmbalm.set(0)
BodyVIP.set(0)
BodyFlower.set(0)
BodyOther.set(0)
BodyCoffin.set(0)
BodyHearse.set(0)
BodyTent.set(0)
BodyPostMortem.set(0)
BodyWashingAmount=IntVar()
BodyEmbalmAmount=IntVar()
BodyVIPAmount=IntVar()
BodyFlowerAmount=IntVar()
BodyOtherAmount=IntVar()
BodyCoffinAmount=IntVar()
BodyHearseAmount=IntVar()
BodyTentAmount=IntVar()
BodyPostMortemAmount=IntVar()
BodyWashingAmount.set("0")
BodyEmbalmAmount.set("0")
BodyVIPAmount.set("0")
BodyFlowerAmount.set("0")
BodyOtherAmount.set("0")
BodyCoffinAmount.set("0")
BodyHearseAmount.set("0")
BodyTentAmount.set("0")
BodyPostMortemAmount.set("0")


def logout():
	Frame2.pack_forget()
	Frame3.pack_forget()
	Frame4.pack_forget()
	Frame1.pack()
	

def regsuccess():
   messagebox.showinfo("Registration Successful","Registration Succesful")

def forgotpassword():
	Frame1.pack_forget()
	Frame2.pack_forget()
	Frame3.pack()
	Frame4.pack_forget()
def registerbody():
	Frame1.pack_forget()
	Frame2.pack_forget()
	Frame3.pack_forget()
	Frame4.pack()


def viewrecords():
	Frame1.pack_forget()
	Frame2.pack_forget()
	Frame3.pack_forget()
	Frame4.pack_forget()
	Frame5.pack()

def optionspage():
    Frame1.pack_forget()
    Frame3.pack_forget()
    Frame4.pack_forget()
    Frame5.pack_forget()
    Frame2.pack()

def login():
    Frame1.pack_forget()
    Frame3.pack_forget()
    Frame4.pack_forget()
    Frame5.pack_forget()
    Frame2.pack()


def quit():
	root.quit()



class LogIn:
    
    Date1=StringVar()
    Date1.set(time.strftime("%Y/%m/%d"))

    Date1=StringVar()
    Date1.set(time.strftime("%Y/%m/%d"))

    TopFrame=Frame(Frame1,width=1000,height=100,bd=8,bg='green',relief='raise')
    TopFrame.pack(side=TOP)

    #MiddleFrame=Frame(root,width=1000,height=50,bd=8,bg='green',relief='ridge')
    #MiddleFrame.pack(side=)

    MiddleFrame=Frame(Frame1,width=1001,height=600,bd=8,bg='green',relief='ridge')
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
    #PasswordEntry.pack()

    BottomMarking=Label(MiddleFrame,text="Transforming Lives Through Quality Education",width=38,bg='Green',font=('times',22,'italic'),fg='bisque2')
    BottomMarking.place(x=200,y=450)

            
    image1=PhotoImage(file="logo.gif")
    TopLabel=Label(TopFrame,image=image1)
    TopLabel.pack(side='top',fill='both',expand='yes')

    LogInButton=Button(MiddleFrame,width=20,text="Log In",font=('times',14,'italic'),command=login,bg='Green',fg='white',relief='ridge')
    LogInButton.place(x=680,y=250)

    ForgotPasswordButton=Button(MiddleFrame,width=20,text="Forgot Password",font=('times',14,'italic'),command=forgotpassword,bg='Green',fg='white',relief='ridge')
    ForgotPasswordButton.place(x=680,y=300)


    #def login():
     #   if(NameEntry.get()=="Admin" and PasswordEntry.get()=="12345"):
      #      optionspage()
        #elif(NameEntry.get()!="Admin" and PasswordEntry.get()!="12345"):
         #   messagebox.showinfo("Warning","Incorrect UserName or Password")


    #def authe():
     #   cnx=mysql.connector.connect(user='root',host='127.0.0.1',database='bodies')
      #  cursor=cnx.cursor()

        #cursor.execute("SELECT staffid FROM users WHERE staffid='%s'" %(NameEntry.get()))
        #staffid=cursor.fetchone()
        #staffidgood=(str(staffid[0]))
        #print(str(staffid[0]))
        #cursor.close()
        #cnx.close()

        #cnx=mysql.connector.connect(user='root',host='127.0.0.1',database='bodies')
        #cursor=cnx.cursor()
        #cursor.execute("SELECT password FROM users WHERE password='%s'" %(PasswordEntry.get()))
        #password=cursor.fetchone()
        #passwordgood=(str(password[0]))
        #cnx.commit()
        #cursor.close()
        #cnx.close()

        #if((staffidgood==StaffEntry.get() and passwordgood==PasswordEntry.get())):
        #    print("Good")
        #    messagebox.showinfo("Registration Successful","Registration Succesful")

    

#from tkinter import *

#root=Tk()

#root.geometry("1000x700+0+0")
class Welcome():

 root.title("Welcome Page")

 TopFrame=Frame(Frame2,width=1000,height=100,bg='Green',bd=8,relief='ridge')
 TopFrame.pack(side=TOP)

 image1=PhotoImage(file="logo.gif")

 TopLabel=Label(TopFrame,image=image1)
 TopLabel.pack(side='top',fill='both',expand='yes')

 InTop=Frame(TopFrame,width=1000,height=100,bg='Green',bd=4,relief='ridge')
 InTop.pack(side=BOTTOM)

 InTopLabel=Label(InTop,width=450,height=2,font=('times',18,'italic'),bg='Green',text="Welcome, Choose From The Options Below",fg='white')
 InTopLabel.pack()

 LeftFrame=Frame(Frame2,width=500,height=500,bg='Green',bd=8,relief='ridge')
 LeftFrame.pack(side=LEFT)

 RightFrame=Frame(Frame2,width=500,height=500,bg='Green',bd=8,relief='ridge')
 RightFrame.pack(side=RIGHT)

 RegisterButton=Button(LeftFrame,width=45,height=3,bg='white',font=('times',14,'italic'),text="Register Body",command=registerbody,fg='Green',bd=4,relief='ridge')
 RegisterButton.place(x=6,y=20)

 ViewRecordsButton=Button(LeftFrame,width=45,height=3,bg='white',font=('times',14,'italic'),text="View Records",command=viewrecords,fg='Green',bd=4,relief='ridge')
 ViewRecordsButton.place(x=6,y=150)

 HelpAndMore=Button(LeftFrame,width=45,height=3,bg='white',font=('times',14,'italic'),text="Help And More",command=forgotpassword,fg='Green',bd=4,relief='ridge')
 HelpAndMore.place(x=6,y=280)

 BillButton=Button(RightFrame,width=45,height=3,bg='white',font=('times',14,'italic'),text="Bill And Discharge Body",command=viewrecords,fg='Green',bd=4,relief='ridge')
 BillButton.place(x=6,y=20)

 AboutButton=Button(RightFrame,width=45,height=3,bg='white',font=('times',14,'italic'),text="About",command=forgotpassword,fg='Green',bd=4,relief='ridge')
 AboutButton.place(x=6,y=150)

 LogoutButton=Button(RightFrame,width=45,height=3,bg='white',font=('times',14,'italic'),text="Log Out",command=logout,fg='Green',bd=4,relief='ridge')
 LogoutButton.place(x=6,y=280)


class PasswordReset:
	root.title("Mortuary Management System")
	ComingSoonOne1=Frame(Frame3,width=1000,height=700,bg='Green',bd=8,relief='ridge')
	ComingSoonOne1.pack()
	ButtonQuit=Button(Frame3,text="Quit",bg='Green',fg='white',font=('times',16,'italic'),command=quit,bd=4,relief='ridge')
	ButtonQuit.place(x=500,y=500)
	ComingSoonLabel1=Label(ComingSoonOne1,text="Coming Soon",font=('times',30,'italic'),bg='Green',fg='white')
	ComingSoonLabel1.place(x=380,y=300)

root.geometry("1000x700+0+0")

class bodyreg():
	#root.title("Body Registration")
	NameEntryVariable=StringVar()
	IdNumberEntryVariable=StringVar()
	NextOfKinEntryVariable=StringVar()
	KinPhoneEntryVariable=StringVar()

	BodyWash=IntVar()
	BodyEmbalm=IntVar()
	BodyVIP=IntVar()
	BodyFlower=IntVar()
	BodyOther=IntVar()
	BodyCoffin=IntVar()
	BodyHearse=IntVar()
	BodyTent=IntVar()
	BodyPostMortem=IntVar()

	BodyWash.set(0)
	BodyEmbalm.set(0)
	BodyVIP.set(0)
	BodyFlower.set(0)
	BodyOther.set(0)
	BodyCoffin.set(0)
	BodyHearse.set(0)
	BodyTent.set(0)
	BodyPostMortem.set(0)

	BodyWashingAmount=IntVar()
	BodyEmbalmAmount=IntVar()
	BodyVIPAmount=IntVar()
	BodyFlowerAmount=IntVar()
	BodyOtherAmount=IntVar()
	BodyCoffinAmount=IntVar()
	BodyHearseAmount=IntVar()
	BodyTentAmount=IntVar()
	BodyPostMortemAmount=IntVar()

	BodyWashingAmount.set("0")
	BodyEmbalmAmount.set("0")
	BodyVIPAmount.set("0")
	BodyFlowerAmount.set("0")
	BodyOtherAmount.set("0")
	BodyCoffinAmount.set("0")
	BodyHearseAmount.set("0")
	BodyTentAmount.set("0")
	BodyPostMortemAmount.set("0")
#------------------------------------------------------------
NameEntryVariable=StringVar()
IdNumberEntryVariable=StringVar()
NextOfKinEntryVariable=StringVar()
KinPhoneEntryVariable=StringVar()


BodyWash=IntVar()
BodyEmbalm=IntVar()
BodyVIP=IntVar()
BodyFlower=IntVar()
BodyOther=IntVar()
BodyCoffin=IntVar()
BodyHearse=IntVar()
BodyTent=IntVar()
BodyPostMortem=IntVar()

BodyWash.set(0)
BodyEmbalm.set(0)
BodyVIP.set(0)
BodyFlower.set(0)
BodyOther.set(0)
BodyCoffin.set(0)
BodyHearse.set(0)
BodyTent.set(0)
BodyPostMortem.set(0)


BodyWashingAmount=IntVar()
BodyEmbalmAmount=IntVar()
BodyVIPAmount=IntVar()
BodyFlowerAmount=IntVar()
BodyOtherAmount=IntVar()
BodyCoffinAmount=IntVar()
BodyHearseAmount=IntVar()
BodyTentAmount=IntVar()
BodyPostMortemAmount=IntVar()

BodyWashingAmount.set("0")
BodyEmbalmAmount.set("0")
BodyVIPAmount.set("0")
BodyFlowerAmount.set("0")
BodyOtherAmount.set("0")
BodyCoffinAmount.set("0")
BodyHearseAmount.set("0")
BodyTentAmount.set("0")
BodyPostMortemAmount.set("0")
#-------------------------------
def resetbutton():
        BodyWash.set(0)
        BodyEmbalm.set(0)
        BodyVIP.set(0)
        BodyFlower.set(0)
        BodyOther.set(0)
        BodyCoffin.set(0)
        BodyHearse.set(0)
        BodyTent.set(0)
        BodyPostMortem.set(0)
        BodyWashingAmount.set("0")
        BodyEmbalmAmount.set("0")
        BodyVIPAmount.set("0")
        BodyFlowerAmount.set("0")
        BodyOtherAmount.set("0")
        BodyCoffinAmount.set("0")
        BodyHearseAmount.set("0")
        BodyTentAmount.set("0")
        BodyPostMortemAmount.set("0")

        BodyWashingEntry.configure(state=DISABLED)
        EmbalmingEntry.configure(state=DISABLED)
        VIPEntry.configure(state=DISABLED)
        FlowerEntry.configure(state=DISABLED)
        OtherEntry.configure(state=DISABLED)
        CoffinEntry.configure(state=DISABLED)
        HearseEntry.configure(state=DISABLED)
        TentEntry.configure(state=DISABLED)
        PostMortemEntry.configure(state=DISABLED)

        NameEntryVariable.set("")
        IdNumberEntryVariable.set("")
        NextOfKinEntryVariable.set("")
        KinPhoneEntryVariable.set("")
#-----------------------checkbutton state------------------
def cmdchkbtn():
        if(BodyWash.get() == 1):
                BodyWashingEntry.configure(state=NORMAL)
        elif BodyWash.get() == 0:
                BodyWashingEntry.configure(state=DISABLED)
                BodyWashingAmount.set(0)

        if(BodyEmbalm.get() == 1):
                EmbalmingEntry.configure(state=NORMAL)
        elif BodyEmbalm.get() == 0:
                EmbalmingEntry.configure(state=DISABLED)
                BodyEmbalmAmount.set(0)

        if(BodyVIP.get() == 1):
                VIPEntry.configure(state=NORMAL)
        elif BodyVIP.get() == 0:
                VIPEntry.configure(state=DISABLED)
                BodyVIPAmount.set(0)

        if(BodyFlower.get() == 1):
                FlowerEntry.configure(state=NORMAL)
        elif BodyFlower.get() == 0:
                FlowerEntry.configure(state=DISABLED)
                BodyFlowerAmount.set(0)

        if(BodyOther.get() == 1):
                OtherEntry.configure(state=NORMAL)
        elif BodyOther.get() == 0:
                OtherEntry.configure(state=DISABLED)
                BodyOtherAmount.set(0)

        if(BodyCoffin.get() == 1):
                CoffinEntry.configure(state=NORMAL)
        elif BodyCoffin.get() == 0:
                CoffinEntry.configure(state=DISABLED)
                BodyCoffinAmount.set(0)

        if(BodyHearse.get() == 1):
                HearseEntry.configure(state=NORMAL)
        elif BodyHearse.get() == 0:
                HearseEntry.configure(state=DISABLED)
                BodyHearseAmount.set(0)
        if(BodyTent.get() == 1):
                TentEntry.configure(state=NORMAL)
        elif BodyTent.get() == 0:
                TentEntry.configure(state=DISABLED)
                BodyTentAmount.set(0)

        if(BodyPostMortem.get() == 1):
                PostMortemEntry.configure(state=NORMAL)
        elif BodyPostMortem.get() == 0:
                PostMortemEntry.configure(state=DISABLED)
                BodyPostMortemAmount.set(0)


date1=StringVar()
date1.set(time.strftime("%Y/%m/%d"))
time1=StringVar()
time1.set(time.strftime("%H:%M:%S"))
TopFrame=Frame(Frame4,width=1000,height=100,bg='Green',bd=8,relief='ridge')
TopFrame.pack(expand=TRUE)
#-------------------------------------TOP FRAME-----------------------------------
TopLabel=Label(TopFrame,width=77,height=3,font=('times',17,'italic'),text="Body Registration",bg='Green',fg='white')
TopLabel.pack(side=TOP)
#--------------------------------------LEFT FRAME=--------------------------
LeftFrame=Frame(Frame4,width=700,height=600,bg='Green',bd=8,relief='ridge')
LeftFrame.pack(side=LEFT,expand=TRUE)
#---------------------------------------RIGHT FRAME----------------------------------
RightFrame=Frame(Frame4,width=300,height=600,bg='Green',bd=8,relief='ridge')
RightFrame.pack(side=RIGHT,expand=TRUE)

#------------------------------IN LEFT FRAME----------------------------------------------

LeftInLeftFrame=Frame(LeftFrame,width=700,height=600,bg='Green',bd=4,relief='ridge')
LeftInLeftFrame.pack(side=TOP)

BottomInLeftFrame=Frame(LeftFrame,width=700,height=600,bg='Green',bd=4,relief='ridge')
BottomInLeftFrame.pack(side=BOTTOM)
#-----------------------LABELS IN LEEFT FRAME----------------
NameLabel=Label(LeftInLeftFrame,width=20,bg='Green',text="Name",font=('times',18,'italic'),height=2,fg='white',anchor="w")
NameLabel.grid(row=0,column=0)

IdNumberLabel=Label(LeftInLeftFrame,width=20,bg='Green',text="ID Number",font=('times',18,'italic'),height=2,fg='white',anchor="w")
IdNumberLabel.grid(row=1,column=0)

NextOfKinLabel=Label(LeftInLeftFrame,width=20,bg='Green',text="Next Of Kin Name",font=('times',18,'italic'),height=2,fg='white',anchor="w")
NextOfKinLabel.grid(row=2,column=0)

KinPhoneLabel=Label(LeftInLeftFrame,width=20,bg='Green',text="Kin Phone Number",font=('times',18,'italic'),height=2,fg='white',anchor="w")
KinPhoneLabel.grid(row=3,column=0)

DateLabel=Label(LeftInLeftFrame,width=20,bg='Green',text="Date",font=('times',18,'italic'),fg='white',height=3,anchor="w")
DateLabel.grid(row=4,column=0)


#----------------------------------------------------------------ENTRIES IN LEFT FRAME-------TOP------------------------

Name1Entry=Entry(LeftInLeftFrame,width=53,font=('times',12,'italic'),bd=2,textvariable=NameEntryVariable,relief='ridge')
Name1Entry.grid(row=0,column=1,ipady=5)

IdNumberEntry=Entry(LeftInLeftFrame,width=51,font=('times',12,'italic'),textvariable=IdNumberEntryVariable,bd=2,relief='ridge')
IdNumberEntry.grid(row=1,column=1,ipady=5)

NextOfKinEntry=Entry(LeftInLeftFrame,width=51,font=('times',12,'italic'),bd=2,textvariable=NextOfKinEntryVariable,relief='ridge')
NextOfKinEntry.grid(row=2,column=1,ipady=5)

KinPhoneEntry=Entry(LeftInLeftFrame,width=51,font=('times',12,'italic'),textvariable=KinPhoneEntryVariable,bd=2,relief='ridge')
KinPhoneEntry.grid(row=3,column=1,ipady=5)

DateEntry=Entry(LeftInLeftFrame,width=51,font=('times',12,'italic'),textvariable=date1,bd=2,fg='Green',relief='ridge')
DateEntry.grid(row=4,column=1,ipady=5)

#-----------------------------LEFT FRAME----BOTTOM---------------
ServicesLabel=Label(BottomInLeftFrame,text="Services",bg='Green',font=('times',16,'italic'),fg='white',width=50,height=2)
ServicesLabel.grid(row=0,column=0,columnspan=20)

BodyWashing=Label(BottomInLeftFrame,text="Body Washing",font=('times',14,'italic'),bg='Green',fg='white',height=2,anchor="w")
BodyWashing.grid(row=1,column=1)
Chkbtn1=Checkbutton(BottomInLeftFrame,bg='Green',variable=BodyWash,onvalue=1,offvalue=0,command=cmdchkbtn,anchor="w")
Chkbtn1.grid(row=1,column=0)
BodyWashingEntry=Entry(BottomInLeftFrame,width=7,font=('times',10,'italic'),textvariable=BodyWashingAmount,bd=2,relief='ridge',state=DISABLED)
BodyWashingEntry.grid(row=1,column=2)

Embalming=Label(BottomInLeftFrame,text="Embalming",font=('times',14,'italic'),bg='Green',fg='white',height=2,anchor="w")
Embalming.grid(row=2,column=1)
Chkbtn2=Checkbutton(BottomInLeftFrame,bg='Green',variable=BodyEmbalm,offvalue=0,command=cmdchkbtn,onvalue=1)
Chkbtn2.grid(row=2,column=0)
EmbalmingEntry=Entry(BottomInLeftFrame,width=7,font=('times',10,'italic'),textvariable=BodyEmbalmAmount,bd=2,relief='ridge',state=DISABLED)
EmbalmingEntry.grid(row=2,column=2)

VIP=Label(BottomInLeftFrame,text="VIP Services",font=('times',14,'italic'),bg='Green',fg='white',height=2)
VIP.grid(row=3,column=1)
Chkbtn3=Checkbutton(BottomInLeftFrame,bg='Green',variable=BodyVIP,offvalue=0,command=cmdchkbtn,onvalue=1)
Chkbtn3.grid(row=3,column=0)
VIPEntry=Entry(BottomInLeftFrame,width=7,font=('times',10,'italic'),textvariable=BodyVIPAmount,bd=2,relief='ridge',state=DISABLED)
VIPEntry.grid(row=3,column=2)


FlowerServices=Label(BottomInLeftFrame,text="Flower Services",font=('times',14,'italic'),bg='Green',fg='white',height=2)
FlowerServices.grid(row=4,column=1)
Chkbtn4=Checkbutton(BottomInLeftFrame,bg='Green',variable=BodyFlower,offvalue=0,command=cmdchkbtn,onvalue=1)
Chkbtn4.grid(row=4,column=0)
FlowerEntry=Entry(BottomInLeftFrame,width=7,font=('times',10,'italic'),textvariable=BodyFlowerAmount,bd=2,relief='ridge',state=DISABLED)
FlowerEntry.grid(row=4,column=2)


HearseServices=Label(BottomInLeftFrame,text="Hearse Services",font=('times',14,'italic'),bg='Green',fg='white',height=2)
HearseServices.grid(row=3,column=4)
Chkbtn5=Checkbutton(BottomInLeftFrame,bg='Green',variable=BodyHearse,offvalue=0,command=cmdchkbtn,onvalue=1)
Chkbtn5.grid(row=3,column=3)
HearseEntry=Entry(BottomInLeftFrame,width=7,font=('times',10,'italic'),textvariable=BodyHearseAmount,bd=2,relief='ridge',state=DISABLED)
HearseEntry.grid(row=3,column=5)

OtherServices=Label(BottomInLeftFrame,text="Other Services",font=('times',14,'italic'),bg='Green',fg='white',height=2)
OtherServices.grid(row=1,column=4)
Chkbtn6=Checkbutton(BottomInLeftFrame,bg='Green',variable=BodyOther,offvalue=0,command=cmdchkbtn,onvalue=1)
Chkbtn6.grid(row=1,column=3)
OtherEntry=Entry(BottomInLeftFrame,width=7,font=('times',10,'italic'),textvariable=BodyOtherAmount,bd=2,relief='ridge',state=DISABLED)
OtherEntry.grid(row=1,column=5)

CoffinProvision=Label(BottomInLeftFrame,text="Coffin Provision",font=('times',14,'italic'),bg='Green',fg='white',height=2)
CoffinProvision.grid(row=2,column=4)
Chkbtn7=Checkbutton(BottomInLeftFrame,bg='Green',variable=BodyCoffin,offvalue=0,command=cmdchkbtn,onvalue=1)
Chkbtn7.grid(row=2,column=3)
CoffinEntry=Entry(BottomInLeftFrame,width=7,font=('times',10,'italic'),textvariable=BodyCoffinAmount,bd=2,relief='ridge',state=DISABLED)
CoffinEntry.grid(row=2,column=5)

PostMortem=Label(BottomInLeftFrame,text=" Post Mortem  ",font=('times',14,'italic'),bg='Green',fg='white',height=2)
PostMortem.grid(row=1,column=7)
Chkbtn6=Checkbutton(BottomInLeftFrame,bg='Green',variable=BodyPostMortem,offvalue=0,command=cmdchkbtn,onvalue=1)
Chkbtn6.grid(row=1,column=6)
PostMortemEntry=Entry(BottomInLeftFrame,width=7,font=('times',10,'italic'),textvariable=BodyPostMortemAmount,bd=2,relief='ridge',state=DISABLED)
PostMortemEntry.grid(row=1,column=8)

TentServices=Label(BottomInLeftFrame,text="Tent Services",font=('times',14,'italic'),bg='Green',fg='white',height=2)
TentServices.grid(row=4,column=4)
Chkbtn7=Checkbutton(BottomInLeftFrame,bg='Green',variable=BodyTent,offvalue=0,command=cmdchkbtn,onvalue=1)
Chkbtn7.grid(row=4,column=3)
TentEntry=Entry(BottomInLeftFrame,width=7,font=('times',10,'italic'),textvariable=BodyTentAmount,bd=2,relief='ridge',state=DISABLED)
TentEntry.grid(row=4,column=5)




#ResetButton=Button(BottomInLeftFrame,font=('times',14,'italic'),bg='Green',text="  Reset ",command=resetbutton,bd=4,fg='white',relief='ridge')
#ResetButton.grid(row=3,column=35)
#--------------------------------------------------

#-------------------------------------------------
image1=PhotoImage(file="Egerton.gif")

image2=PhotoImage(file="Egerton.gif")

TopLabel=Label(RightFrame,image=image2,bd=4,relief='ridge')
TopLabel.place(x=33,y=2)

AboutButton=Button(RightFrame,font=('times',14,'italic'),bg='Green',text="About",bd=4,fg='white',relief='ridge',width=22,height=2)
AboutButton.place(x=15,y=250)

OptionsButton=Button(RightFrame,font=('times',14,'italic'),bg='Green',text="Options",bd=4,command=optionspage,fg='white',relief='ridge',width=22,height=2)
OptionsButton.place(x=15,y=315)

ViewRecordsButton=Button(RightFrame,font=('times',14,'italic'),bg='Green',text="View Records",command=viewrecords,bd=4,fg='white',relief='ridge',width=22,height=2)
ViewRecordsButton.place(x=15,y=380)

BillButton=Button(RightFrame,font=('times',14,'italic'),bg='Green',text="Bill & Discharge Body",bd=4,command=viewrecords,fg='white',relief='ridge',width=22,height=2)
BillButton.place(x=15,y=445)

LogoutButton=Button(RightFrame,font=('times',14,'italic'),bg='Green',text="Log Out",bd=4,fg='white',command=logout,relief='ridge',width=22,height=2)
LogoutButton.place(x=15,y=510)


cnx=mysql.connector.connect(user='root',host='127.0.0.1',database='bodies')
cursor=cnx.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS trial(name VARCHAR (30) NOT NULL,idnumber VARCHAR (30) NOT NULL,kinname VARCHAR (30),kinnumber VARCHAR(30),bodywash INT,embalming INT,VIP INT,Flowers INT,Other INT,Coffin INT,Hearse INT,Tent INT,PostMortem INT,date1 date,PRIMARY KEY(idnumber))''')
cnx.commit()
cursor.close()
cnx.close()
#CREATE TABLE IF NOT EXISTS deceased(name VARCHAR (30),idnumber VARCHAR (30),kinname VARCHAR (30),kinnumber VARCHAR (30),bodywash VARCHAR(10),embalming VARCHAR(10),VIP VARCHAR(10),Flowers VARCHAR(10),Other VARCHAR(10),Coffin VARCHAR(10),Hearse VARCHAR(10),Tent VARCHAR(10),PostMortem VARCHAR(10))
#-----------------------------connect to the database--------------------------------------
def connect():
        cnx=mysql.connector.connect(user='root',host='127.0.0.1',database='bodies')
        cursor=cnx.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS trial(name VARCHAR (30) NOT NULL,idnumber VARCHAR (30) NOT NULL,kinname VARCHAR (30),kinnumber VARCHAR(30),bodywash INT,embalming INT,VIP INT,Flowers INT,Other INT,Coffin INT,Hearse INT,Tent INT,PostMortem INT,date1 date,primary key(idnumber))''')
        if(Name1Entry.get()=="" and IdNumberEntry.get()==""):
        	messagebox.showinfo("Warning","Name Cannot Be Blank")

        cursor.execute("INSERT INTO trial(name,idnumber,kinname,kinnumber,bodywash,embalming,VIP,Flowers,Other,Coffin,Hearse,Tent,PostMortem,date1) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(Name1Entry.get(),IdNumberEntry.get(),NextOfKinEntry.get(),KinPhoneEntry.get(),BodyWashingEntry.get(),EmbalmingEntry.get(),VIPEntry.get(),FlowerEntry.get(),OtherEntry.get(),CoffinEntry.get(),HearseEntry.get(),TentEntry.get(),PostMortemEntry.get(),DateEntry.get(),))
        cnx.commit()
        cursor.close()
        cnx.close()
        regsuccess()
        resetbutton()
#-----------------------checkbutton value--------------
SubmitButton=Button(BottomInLeftFrame,font=('times',14,'italic'),bg='Green',text="Submit",command=connect,bd=4,fg='white',relief='ridge')
SubmitButton.grid(row=4,column=35)

#class viewrecords():
 #       MainFrame=Frame(Frame5)
  #      MainFrame.pack()
#
 #       tree=Treeview(MainFrame,selectmode=BROWSE)
#
 #       yframe=Frame(MainFrame)
  #      yframe.pack(side='right',fill='y')
#
 #       yscrollbar = Scrollbar(yframe, orient="vertical", command=tree.yview)
  #      yscrollbar.pack(expand='yes', fill='y')
#
 #       xframe=Frame(MainFrame)
  #      xframe.pack(side='bottom',fill='x')
#
 #       xscrollbar = Scrollbar(xframe, orient="horizontal", command=tree.xview)
  #      xscrollbar.pack(expand='yes', fill='x')
#
 #       tree.configure(yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set)
  #      tree.pack(fill='both', expand='yes')
#
 #       cnx=mysql.connector.connect(user='root',host='127.0.0.1',database='bodies')
  #      cursor=cnx.cursor()
#
 #       tree["columns"]=("one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen")
  #      tree.column("one",width=130)
   #     tree.column("two",width=100)
    #    tree.column("three",width=130)
     #   tree.column("four",width=100)
      #  tree.column("five",width=100)
       # tree.column("six",width=100)
        #tree.column("seven",width=100)
        #tree.column("eight",width=100)
        #tree.column("nine",width=100)
        #tree.column("ten",width=100)
        #tree.column("eleven",width=100)
        #tree.column("twelve",width=100)
        #tree.column("thirteen",width=100)
        #tree.heading("one",text="Name",anchor="w")
        #tree.heading("two",text="Id Number",anchor="w")
        #tree.heading("three",text="Next Of Kin Name",anchor="w")
        #tree.heading("four",text="Next Of Kin Number",anchor="w")
        #tree.heading("five",text="Body Washing",anchor="w")
        #tree.heading("six",text="Body Embalming",anchor="w")
        #tree.heading("seven",text="VIP Preservation",anchor="w")
        #tree.heading("eight",text="Flower Services",anchor="w")
        #tree.heading("nine",text="Other Services",anchor="w")
        #tree.heading("ten",text="Coffin Provision",anchor="w")
        #tree.heading("eleven",text="Hearse Provision",anchor="w")
        #tree.heading("twelve",text="Tent Provision",anchor="w")
        #tree.heading("thirteen",text="Post Mortem",anchor="w")
#
 #       cursor.execute('''SELECT * FROM deceased''')
#
 #       for (name) in cursor:
  #              tree.insert("",index=END,values=(name))
#
 #       cnx.commit()
  #      cursor.close()
   #     cnx.close()
    #    tree.pack()
#from tkinter import *
#from tkinter.ttk import Treeview
#import mysql.connector
#import datetime
#import time
#root=Tk()
#root.title("TreeView")
#root.geometry("1000x700+0+0")
#root.resizable(0,0)

now=datetime.datetime.now()
today=now.date()
FrameOne1=Frame(Frame5)
FrameOne1.pack()
FrameTwo2=Frame(Frame5)
TopOne1Frame=Frame(FrameOne1,bg='white',height=100,width=1000,bd=4,relief='ridge')
TopOne1Frame.pack(side=TOP)
MainOne1Frame=Frame(FrameOne1)
MainOne1Frame.pack()
BottomOne1Frame=Frame(FrameOne1,bg='white',height=400,width=1000,bd=4,relief='ridge')
BottomOne1Frame.pack(side=BOTTOM)
SearchVariable=StringVar()


TopOne1LAbel=Label(TopOne1Frame,bg='white',text='                                                                                Records                                                                                 ',fg='Green',font=('times',18,'italic'))
TopOne1LAbel.pack()

NextFrame=Frame(FrameTwo2,bd=2,relief='ridge')
NextFrame.pack(side= BOTTOM)

NextFrameTop=Frame(FrameTwo2,bd=2,relief='ridge',height=50)
NextFrameTop.pack(side=TOP)

NextTopOne1LAbel=Label(NextFrameTop,text="\t\t\t\t                      Receipt\t\t\t\t\t\t",font=('times',18,'italic'),fg='green')
NextTopOne1LAbel.pack()

receipt=Text(NextFrame,bd=4,relief='ridge',bg='white',font=('times',14,'italic'),fg='green')
receipt.pack()

NameEntry=Entry(BottomOne1Frame,width=50,bd=4,relief='ridge',textvariable=SearchVariable,font=('times',16,'italic'))
NameEntry.place(x=100,y=100)


def connect():

    cnx=mysql.connector.connect(user='root',host='127.0.0.1',database='bodies')
    cursor=cnx.cursor(buffered=True)

    cursor.execute("SELECT name FROM trial WHERE name='%s'" %(NameEntry.get()))
    name=cursor.fetchone()
    print((name[0]))


    cursor.execute("SELECT Coffin FROM trial WHERE name='%s'" %(NameEntry.get()))
    Coffin=cursor.fetchone()
    print(int(Coffin[0]))

    cursor.execute("SELECT bodywash FROM trial WHERE name='%s'" %(NameEntry.get()))
    bodywash=cursor.fetchone()
    print((bodywash[0]))

    cursor.execute("SELECT embalming FROM trial WHERE name='%s'" %(NameEntry.get()))
    embalming=cursor.fetchone()
    print((embalming[0]))

    cursor.execute("SELECT Other FROM trial WHERE name='%s'" %(NameEntry.get()))
    Other=cursor.fetchone()
    print((Other[0]))

    cursor.execute("SELECT VIP FROM trial WHERE name='%s'" %(NameEntry.get()))
    VIP=cursor.fetchone()
    print((VIP[0]))

    cursor.execute("SELECT Flowers FROM trial WHERE name='%s'" %(NameEntry.get()))
    Flowers=cursor.fetchone()
    print((Flowers[0]))

    cursor.execute("SELECT Tent FROM trial WHERE name='%s'" %(NameEntry.get()))
    Tent=cursor.fetchone()
    print((Tent[0]))

    cursor.execute("SELECT PostMortem FROM trial WHERE name='%s'" %(NameEntry.get()))
    PostMortem=cursor.fetchone()
    print((PostMortem[0]))

    cursor.execute("SELECT date1 FROM trial WHERE name='%s'" %(NameEntry.get()))
    date1=cursor.fetchone()
    print((date1[0]))

    cursor.execute("SELECT Hearse FROM trial WHERE name='%s'" %(NameEntry.get()))
    Hearse=cursor.fetchone()
    print((Hearse[0]))



    #cursor.execute("SELECT name FROM trial WHERE name='%s'" %(NameEntry.get() "and Cofffin='%s'" %(CoffinEntry.get()))
    #cursor.execute("SELECT name FROM trial WHERE name=%s")
    #name=Name2
    
    #for (name) in cursor:
    #   print(name)

    #cursor.commit()
    #cnx.commit()
    cursor.close()
    cnx.close()
    #print(name)
    #return name
    #print(NameEntry.get())

    nowdate=(today-date1[0])
    print(nowdate.days)


    totalsum=(Coffin[0]+bodywash[0]+embalming[0]+Other[0]+VIP[0]+Flowers[0]+Tent[0]+PostMortem[0])
    print(totalsum)

    abstotal=IntVar()
    if ((nowdate.days<=7)):
        abstotal=(4000+totalsum)
    elif((nowdate.days>7)):
        abstotal=((((nowdate.days-7)*500)+4000)+totalsum)

    dayssum=abstotal-totalsum
    print(abstotal)


    #receipt=Text(FrameTwo2,bd=4,relief='ridge',bg='white',font=('times',14,'italic'),fg='green')
    #receipt.pack()

    receipt.insert(END,"Name\t\t\t")
    receipt.insert(END,name[0])

    receipt.insert(END,"\nBody Washing\t\t\t")
    receipt.insert(END,bodywash[0])

    receipt.insert(END,'\nCoffin Provision\t\t\t')
    receipt.insert(END,Coffin[0])

    receipt.insert(END,'\nEmbalming\t\t\t')
    receipt.insert(END,embalming[0])

    receipt.insert(END,'\nVIP\t\t\t')
    receipt.insert(END,VIP[0])

    receipt.insert(END,'\nFlowers\t\t\t')
    receipt.insert(END,Flowers[0])

    receipt.insert(END,'\nOther\t\t\t')
    receipt.insert(END,Other[0])

    receipt.insert(END,'\nHearse\t\t\t')
    receipt.insert(END,Hearse[0])

    receipt.insert(END,'\nTent\t\t\t')
    receipt.insert(END,Tent[0])

    receipt.insert(END,'\nPost Mortem\t\t\t')
    receipt.insert(END,PostMortem[0])

    receipt.insert(END,'\nNumber of Days\t\t\t')
    receipt.insert(END,nowdate.days)

    receipt.insert(END,'\nCost of Days\t\t\t')
    receipt.insert(END,dayssum)

    receipt.insert(END,'\n\n\n\n \t\t\t\t\t\t\t           Date  ')
    receipt.insert(END,'......................')

    receipt.insert(END,'\n\n \t\t\t\t\t\t\t           Sign  ')
    receipt.insert(END,'.......................')

    receipt.insert(END,'\n')

    receipt.insert(END,'\nTotal Sum\t\t\t')
    receipt.insert(END,abstotal)

    receipt.insert(END,'\n\n\n')
    receipt.insert(END,'\t\t            We At Egerton Are Honoured Serve You\t\t')

    FrameOne1.pack_forget()
    FrameTwo2.pack()


def back():
    FrameOne1.pack()
    receipt.delete('1.0',END)
    SearchVariable.set("")
    FrameTwo2.pack_forget()



tree=Treeview(MainOne1Frame,selectmode=BROWSE)

yframe=Frame(MainOne1Frame)
yframe.pack(side='right',fill='y')
yscrollbar = Scrollbar(yframe, orient="vertical", command=tree.yview)
yscrollbar.pack(expand='yes', fill='y')
xframe=Frame(MainOne1Frame)
xframe.pack(side='bottom',fill='x')
xscrollbar = Scrollbar(xframe, orient="horizontal", command=tree.xview)
xscrollbar.pack(expand='yes', fill='x')

tree.configure(yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set)
tree.pack(fill='both', expand='yes')

image1=PhotoImage(file="egerton.gif")
TopOne1LAbel=Label(BottomOne1Frame,image=image1)
#TopOne1LAbel.pack(side='top',fill='both',expand='yes')
TopOne1LAbel.place(x=792,y=0)

cnx=mysql.connector.connect(user='root',host='127.0.0.1',database='bodies')
cursor=cnx.cursor()

tree["columns"]=("one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen")
tree.column("one",width=130)
tree.column("two",width=100)
tree.column("three",width=130)
tree.column("four",width=100)
tree.column("five",width=100)
tree.column("six",width=100)
tree.column("seven",width=100)
tree.column("eight",width=100)
tree.column("nine",width=100)
tree.column("ten",width=100)
tree.column("eleven",width=100)
tree.column("twelve",width=100)
tree.column("thirteen",width=100)
tree.column("fourteen",width=100)
tree.heading("one",text="Name",anchor="w")
tree.heading("two",text="Id Number",anchor="w")
tree.heading("three",text="Next Of Kin Name",anchor="w")
tree.heading("four",text="Next Of Kin Number",anchor="w")
tree.heading("five",text="Body Washing",anchor="w")
tree.heading("six",text="Body Embalming",anchor="w")
tree.heading("seven",text="VIP Preservation",anchor="w")
tree.heading("eight",text="Flower Services",anchor="w")
tree.heading("nine",text="Other Services",anchor="w")
tree.heading("ten",text="Coffin Provision",anchor="w")
tree.heading("eleven",text="Hearse Provision",anchor="w")
tree.heading("twelve",text="Tent Provision",anchor="w")
tree.heading("thirteen",text="Post Mortem",anchor="w")
tree.heading("fourteen",text="Date",anchor="w")
tree.tag_configure("evenrow",background="RoyalBlue2")
tree.tag_configure("evenrow", background="gray88")

#tree.pack(side='left')
cursor.execute(''' SELECT * FROM trial''')

i=0
for (name) in cursor:
    if(i%2==0):
        tree.insert("",index=END,values=(name))
    else:
        tree.insert("",index=END,values=(name), tags= ("evenrow",))
i+=1
#for (name) in cursor:
#    tree.insert("",index=END,values=(name))
cnx.commit()
cursor.close()
cnx.close()
tree.pack()

def refresh2():
	#tree=Treeview(MainOne1Frame,selectmode=BROWSE)
	
	#yframe=Frame(MainOne1Frame)
	#yframe.pack(side='right',fill='y')
	#yscrollbar = Scrollbar(yframe, orient="vertical", command=tree.yview)
	#yscrollbar.pack(expand='yes', fill='y')
	#xframe=Frame(MainOne1Frame)
	#xframe.pack(side='bottom',fill='x')
	#xscrollbar = Scrollbar(xframe, orient="horizontal", command=tree.xview)
	#xscrollbar.pack(expand='yes', fill='x')

	#tree.configure(yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set)
	#tree.pack(fill='both', expand='yes')
	#image1=PhotoImage(file="egerton.gif")
	#TopOne1LAbel=Label(BottomOne1Frame,image=image1)
	#TopOne1LAbel.pack(side='top',fill='both',expand='yes')
	#TopOne1LAbel.place(x=792,y=0)

	cnx=mysql.connector.connect(user='root',host='127.0.0.1',database='bodies')
	cursor=cnx.cursor()


	tree["columns"]=("one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen")
	tree.column("one",width=130)
	tree.column("two",width=100)
	tree.column("three",width=130)
	tree.column("four",width=100)
	tree.column("five",width=100)
	tree.column("six",width=100)
	tree.column("seven",width=100)
	tree.column("eight",width=100)
	tree.column("nine",width=100)
	tree.column("ten",width=100)
	tree.column("eleven",width=100)
	tree.column("twelve",width=100)
	tree.column("thirteen",width=100)
	tree.column("fourteen",width=100)
	tree.heading("one",text="Name",anchor="w")
	tree.heading("two",text="Id Number",anchor="w")
	tree.heading("three",text="Next Of Kin Name",anchor="w")
	tree.heading("four",text="Next Of Kin Number",anchor="w")
	tree.heading("five",text="Body Washing",anchor="w")
	tree.heading("six",text="Body Embalming",anchor="w")
	tree.heading("seven",text="VIP Preservation",anchor="w")
	tree.heading("eight",text="Flower Services",anchor="w")
	tree.heading("nine",text="Other Services",anchor="w")
	tree.heading("ten",text="Coffin Provision",anchor="w")
	tree.heading("eleven",text="Hearse Provision",anchor="w")
	tree.heading("twelve",text="Tent Provision",anchor="w")
	tree.heading("thirteen",text="Post Mortem",anchor="w")
	tree.heading("fourteen",text="Date",anchor="w")
	tree.tag_configure("evenrow",background="RoyalBlue2")
	tree.tag_configure("evenrow", background="gray88")

	#tree.pack(side='left')
	cursor.execute(''' SELECT * FROM trial''')
	i=0
	for (name) in cursor:
		if(i%2==0):
			tree.insert("",index=END,values=(name))
		else:
			tree.insert("",index=END,values=(name), tags= ("evenrow",))
			i+=1
	#for (name) in cursor:
	#    tree.insert("",index=END,values=(name))
	cnx.commit()
	cursor.close()
	cnx.close()
	tree.pack()

def refresh_db():
	x=tree.get_children()
	for name in x:
		tree.delete(name)
	

	refresh2()
BackButton=Button(NextFrame,text="Back To Billing Page",font=('times',18,'italic'),fg='Green',command=back)
BackButton.pack()

SearchTopOne1LAbel=Label(BottomOne1Frame,text="Bill By Name",bg='white',fg='Green',font=('times',18,'italic'))
SearchTopOne1LAbel.place(x=400, y=0)

SearchLabel=Label(BottomOne1Frame,text="Name",bg='white',fg='Green',font=('times',16,'italic'))
SearchLabel.place(x=20, y=100)


RefreshButton=Button(BottomOne1Frame,width=20,bd=2,relief='ridge',text='Refresh Records',command=refresh_db,fg='Green',bg='white',font=('times',18,'italic'))
RefreshButton.place(x=700,y=230)

BillButton=Button(BottomOne1Frame,width=20,bd=2,relief='ridge',text='Bill Body',fg='Green',bg='white',command=connect,font=('times',18,'italic'))
BillButton.place(x=700,y=280)

BackOptionsButton=Button(BottomOne1Frame,width=20,bd=2,relief='ridge',text='Back',fg='Green',bg='white',command=optionspage,font=('times',18,'italic'))
BackOptionsButton.place(x=700,y=330)

	


root.mainloop()
