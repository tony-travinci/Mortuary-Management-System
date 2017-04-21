from tkinter import *
import time
import datetime

root=Tk()
root.geometry("1000x700+0+0")
root.title("Body Registration")

date1=StringVar()
date1.set(time.strftime("%d/%m/%y"))
time1=StringVar()
time1.set(time.strftime("%H:%M:%S"))
TopFrame=Frame(root,width=1000,height=100,bg='Green',bd=8,relief='ridge')
TopFrame.pack()
#-------------------------------------TOP FRAME-----------------------------------
TopLabel=Label(TopFrame,width=77,height=3,font=('times',17,'italic'),text="Body Registration",bg='Green',fg='white')
TopLabel.pack(side=TOP)
#--------------------------------------LEFT FRAME=--------------------------
LeftFrame=Frame(root,width=700,height=600,bg='Green',bd=8,relief='ridge')
LeftFrame.pack(side=LEFT)
#---------------------------------------RIGHT FRAME----------------------------------
RightFrame=Frame(root,width=300,height=600,bg='Green',bd=8,relief='ridge')
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

IdNumberEntry=Entry(LeftInLeftFrame,width=51,font=('times',12,'italic'),bd=2,relief='ridge')
IdNumberEntry.grid(row=1,column=1,ipady=5)

NextOfKinEntry=Entry(LeftInLeftFrame,width=51,font=('times',12,'italic'),bd=2,relief='ridge')
NextOfKinEntry.grid(row=2,column=1,ipady=5)

KinPhoneEntry=Entry(LeftInLeftFrame,width=51,font=('times',12,'italic'),bd=2,relief='ridge')
KinPhoneEntry.grid(row=3,column=1,ipady=5)

DateEntry=Entry(LeftInLeftFrame,width=51,font=('times',12,'italic'),textvariable=date1,bd=2,fg='Green',relief='ridge')
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

OptionsButton=Button(RightFrame,font=('times',14,'italic'),bg='Green',text="Options",bd=4,fg='white',relief='ridge',width=22,height=2)
OptionsButton.place(x=15,y=315)

ViewRecordsButton=Button(RightFrame,font=('times',14,'italic'),bg='Green',text="View Records",bd=4,fg='white',relief='ridge',width=22,height=2)
ViewRecordsButton.place(x=15,y=380)

BillButton=Button(RightFrame,font=('times',14,'italic'),bg='Green',text="Bill & Discharge Body",bd=4,fg='white',relief='ridge',width=22,height=2)
BillButton.place(x=15,y=445)

LogoutButton=Button(RightFrame,font=('times',14,'italic'),bg='Green',text="Log Out",bd=4,fg='white',relief='ridge',width=22,height=2)
LogoutButton.place(x=15,y=510)



root.mainloop()
