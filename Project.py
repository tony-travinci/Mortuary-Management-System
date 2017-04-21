import tkinter as tkinter
from tkinter import *
import time
import datetime

root=Tk()
root.title("Log In Page")

root.geometry("1000x700+0+0")


Frame1=Frame(root,width=1000,height=700)
Frame1.pack()

Frame2=Frame(root,width=1000,height=700)
#Frame2.pack()

Frame3=Frame(root,width=1000,height=700)
#Frame3.pack()

Frame4=Frame(root,width=1000,height=700)
#Frame4.pack()


def login():
	Frame1.pack_forget()
	Frame3.pack_forget()
	Frame4.pack_forget()
	Frame2.pack()
	

def logout():
	Frame2.pack_forget()
	Frame3.pack_forget()
	Frame4.pack_forget()
	Frame1.pack()
	

def forgotpassword():
	Frame1.pack_forget()
	Frame2.pack_forget()
	Frame3.pack()
def registerbody():
	Frame1.pack_forget()
	Frame2.pack_forget()
	Frame3.pack_forget()
	Frame4.pack()

def quit():
	root.quit()

class LogIn:

 Date1=StringVar()
 Date1.set(time.strftime("%d/%m/%Y"))

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

 LogInButton=Button(MiddleFrame,width=20,text="Log In",font=('times',14,'italic'),bg='Green',command=login,fg='white',relief='ridge')
 LogInButton.place(x=680,y=250)

 ForgotPasswordButton=Button(MiddleFrame,width=20,text="Forgot Password",font=('times',14,'italic'),command=forgotpassword,bg='Green',fg='white',relief='ridge')
 ForgotPasswordButton.place(x=680,y=300)

 BottomMarking=Label(MiddleFrame,text="Transforming Lives Through Quality Education",width=38,bg='Green',font=('times',22,'italic'),fg='bisque2')
 BottomMarking.place(x=200,y=450)

 image1=PhotoImage(file="logo.gif")

 TopLabel=Label(TopFrame,image=image1)
 TopLabel.pack(side='top',fill='both',expand='yes')





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

 ViewRecordsButton=Button(LeftFrame,width=45,height=3,bg='white',font=('times',14,'italic'),text="View Records",command=forgotpassword,fg='Green',bd=4,relief='ridge')
 ViewRecordsButton.place(x=6,y=150)

 RegisterButton=Button(LeftFrame,width=45,height=3,bg='white',font=('times',14,'italic'),text="Help And More",command=forgotpassword,fg='Green',bd=4,relief='ridge')
 RegisterButton.place(x=6,y=280)

 BillButton=Button(RightFrame,width=45,height=3,bg='white',font=('times',14,'italic'),text="Bill And Discharge Body",command=forgotpassword,fg='Green',bd=4,relief='ridge')
 BillButton.place(x=6,y=20)

 AboutButton=Button(RightFrame,width=45,height=3,bg='white',font=('times',14,'italic'),text="About",command=forgotpassword,fg='Green',bd=4,relief='ridge')
 AboutButton.place(x=6,y=150)

 LogoutButton=Button(RightFrame,width=45,height=3,bg='white',font=('times',14,'italic'),text="Log Out",command=logout,fg='Green',bd=4,relief='ridge')
 LogoutButton.place(x=6,y=280)


class PasswordReset:
 root.title("Coming Soon")
 ComingSoonOne1=Frame(Frame3,width=1000,height=700,bg='Green',bd=8,relief='ridge')
 ComingSoonOne1.pack()

 ButtonQuit=Button(Frame3,text="Quit",bg='Green',fg='white',font=('times',16,'italic'),command=quit,bd=4,relief='ridge')
 ButtonQuit.place(x=500,y=500)
 ComingSoonLabel1=Label(ComingSoonOne1,text="Coming Soon",font=('times',30,'italic'),bg='Green',fg='white')
 ComingSoonLabel1.place(x=380,y=300)


class BodyRegistration:
 root.title("Body Registration")

 date1=StringVar()
 date1.set(time.strftime("%d/%m/%y"))
 time1=StringVar()
 time1.set(time.strftime("%H:%M:%S"))
 TopFrame=Frame(Frame4,width=1000,height=100,bg='Green',bd=8,relief='ridge')
 TopFrame.pack()
 #-------------------------------------TOP FRAME-----------------------------------
 TopLabel=Label(TopFrame,width=77,height=3,font=('times',17,'italic'),text="Body Registration",bg='Green',fg='white')
 TopLabel.pack(side=TOP)
 #--------------------------------------LEFT FRAME=--------------------------
 LeftFrame=Frame(Frame4,width=700,height=600,bg='Green',bd=8,relief='ridge')
 LeftFrame.pack(side=LEFT)
 #---------------------------------------RIGHT FRAME----------------------------------
 RightFrame=Frame(Frame4,width=300,height=600,bg='Green',bd=8,relief='ridge')
 RightFrame.pack(side=RIGHT) 

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

 NameEntry=Entry(LeftInLeftFrame,width=53,font=('times',12,'italic'),bd=2,relief='ridge')
 NameEntry.grid(row=0,column=1,ipady=5)

 IdNumberEntry=Entry(LeftInLeftFrame,width=53,font=('times',12,'italic'),bd=2,relief='ridge')
 IdNumberEntry.grid(row=1,column=1,ipady=5)

 NextOfKinEntry=Entry(LeftInLeftFrame,width=53,font=('times',12,'italic'),bd=2,relief='ridge')
 NextOfKinEntry.grid(row=2,column=1,ipady=5)
 
 KinPhoneEntry=Entry(LeftInLeftFrame,width=53,font=('times',12,'italic'),bd=2,relief='ridge')
 KinPhoneEntry.grid(row=3,column=1,ipady=5)

 DateEntry=Entry(LeftInLeftFrame,width=53,font=('times',12,'italic'),textvariable=date1,bd=2,fg='Green',relief='ridge')
 DateEntry.grid(row=4,column=1,ipady=5)

#-----------------------------LEFT FRAME----BOTTOM---------------
 ServicesLabel=Label(BottomInLeftFrame,text="Services",bg='Green',font=('times',16,'italic'),fg='white',width=50,height=4)
 ServicesLabel.grid(row=0,column=0,columnspan=10)

 BodyWashing=Label(BottomInLeftFrame,text="Body Washing",font=('times',14,'italic'),bg='Green',fg='white',height=2)
 BodyWashing.grid(row=1,column=1)
 Chkbtn1=Checkbutton(BottomInLeftFrame,bg='Green',offvalue=0,onvalue=1)
 Chkbtn1.grid(row=1,column=0)

 Embalming=Label(BottomInLeftFrame,text="Embalming",font=('times',14,'italic'),bg='Green',fg='white',height=2)
 Embalming.grid(row=2,column=1)
 Chkbtn2=Checkbutton(BottomInLeftFrame,bg='Green',offvalue=0,onvalue=1)
 Chkbtn2.grid(row=2,column=0)

 VIP=Label(BottomInLeftFrame,text="VIP Services",font=('times',14,'italic'),bg='Green',fg='white',height=2)
 VIP.grid(row=3,column=1)
 Chkbtn3=Checkbutton(BottomInLeftFrame,bg='Green',offvalue=0,onvalue=1)
 Chkbtn3.grid(row=3,column=0)

 HearseServices=Label(BottomInLeftFrame,text="Hearse Services",font=('times',14,'italic'),bg='Green',fg='white',height=2)
 HearseServices.grid(row=3,column=4)
 Chkbtn4=Checkbutton(BottomInLeftFrame,bg='Green',offvalue=0,onvalue=1)
 Chkbtn4.grid(row=3,column=3)

 OtherServices=Label(BottomInLeftFrame,text="Other Services",font=('times',14,'italic'),bg='Green',fg='white',height=2)
 OtherServices.grid(row=1,column=4)
 Chkbtn1=Checkbutton(BottomInLeftFrame,bg='Green',offvalue=0,onvalue=1)
 Chkbtn1.grid(row=1,column=3)

 CoffinProvision=Label(BottomInLeftFrame,text="Coffin Provision",font=('times',14,'italic'),bg='Green',fg='white',height=2)
 CoffinProvision.grid(row=2,column=4)
 Chkbtn1=Checkbutton(BottomInLeftFrame,bg='Green',offvalue=0,onvalue=1)
 Chkbtn1.grid(row=2,column=3)

 CoffinProvision=Label(BottomInLeftFrame,text="Flower Services",font=('times',14,'italic'),bg='Green',fg='white',height=2)
 CoffinProvision.grid(row=1,column=7)
 Chkbtn1=Checkbutton(BottomInLeftFrame,bg='Green',offvalue=0,onvalue=1)
 Chkbtn1.grid(row=1,column=6)

 CoffinProvision=Label(BottomInLeftFrame,text="Post Mortem",font=('times',14,'italic'),bg='Green',fg='white',height=2)
 CoffinProvision.grid(row=2,column=7)
 Chkbtn1=Checkbutton(BottomInLeftFrame,bg='Green',offvalue=0,onvalue=1)
 Chkbtn1.grid(row=2,column=6)

 CoffinProvision=Label(BottomInLeftFrame,text="Tent Services",font=('times',14,'italic'),bg='Green',fg='white',height=2)
 CoffinProvision.grid(row=3,column=7)
 Chkbtn1=Checkbutton(BottomInLeftFrame,bg='Green',offvalue=0,onvalue=1)
 Chkbtn1.grid(row=3,column=6)


 CoffinProvision=Label(BottomInLeftFrame,text="Death Certificate",font=('times',14,'italic'),bg='Green',fg='white',height=2)
 CoffinProvision.grid(row=1,column=9)
 Chkbtn1=Checkbutton(BottomInLeftFrame,bg='Green',offvalue=0,onvalue=1)
 Chkbtn1.grid(row=1,column=8)


 SubmitButton=Button(BottomInLeftFrame,font=('times',14,'italic'),bg='Green',text="Submit",bd=4,fg='white',relief='ridge')
 SubmitButton.grid(row=3,column=30)

 image1=PhotoImage(file="Egerton.gif")

 TopLabel=Label(RightFrame,image=image1,bd=4,relief='ridge')
 TopLabel.place(x=33,y=2)

 AboutButton=Button(RightFrame,font=('times',14,'italic'),bg='Green',text="About",bd=4,fg='white',relief='ridge',width=22,height=2)
 AboutButton.place(x=15,y=250)

 OptionsButton=Button(RightFrame,font=('times',14,'italic'),bg='Green',text="Options",bd=4,fg='white',command=login,relief='ridge',width=22,height=2)
 OptionsButton.place(x=15,y=315)

 ViewRecordsButton=Button(RightFrame,font=('times',14,'italic'),bg='Green',text="View Records",bd=4,fg='white',relief='ridge',width=22,height=2)
 ViewRecordsButton.place(x=15,y=380)

 BillButton=Button(RightFrame,font=('times',14,'italic'),bg='Green',text="Bill & Discharge Body",bd=4,fg='white',relief='ridge',width=22,height=2)
 BillButton.place(x=15,y=445)

 LogoutButton=Button(RightFrame,font=('times',14,'italic'),bg='Green',text="Log Out",bd=4,fg='white',command=logout,relief='ridge',width=22,height=2)
 LogoutButton.place(x=15,y=510)



root.mainloop()







