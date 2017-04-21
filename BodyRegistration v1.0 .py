from tkinter import *
import time
import datetime

root=Tk()
root.geometry("1000x700+0+0")
root.title("Body Registration")

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
date1.set(time.strftime("%d/%m/%y"))
time1=StringVar()
time1.set(time.strftime("%H:%M:%S"))
TopFrame=Frame(root,width=1000,height=100,bg='Green',bd=8,relief='ridge')
TopFrame.pack(expand=TRUE)
#-------------------------------------TOP FRAME-----------------------------------
TopLabel=Label(TopFrame,width=77,height=3,font=('times',17,'italic'),text="Body Registration",bg='Green',fg='white')
TopLabel.pack(side=TOP)
#--------------------------------------LEFT FRAME=--------------------------
LeftFrame=Frame(root,width=700,height=600,bg='Green',bd=8,relief='ridge')
LeftFrame.pack(side=LEFT,expand=TRUE)
#---------------------------------------RIGHT FRAME----------------------------------
RightFrame=Frame(root,width=300,height=600,bg='Green',bd=8,relief='ridge')
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


SubmitButton=Button(BottomInLeftFrame,font=('times',14,'italic'),bg='Green',text="Submit",bd=4,fg='white',relief='ridge')
SubmitButton.grid(row=4,column=35)

ResetButton=Button(BottomInLeftFrame,font=('times',14,'italic'),bg='Green',text="  Reset ",bd=4,fg='white',relief='ridge')
ResetButton.grid(row=3,column=35)
#--------------------------------------------------

#-------------------------------------------------
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

#-----------------------checkbutton value--------------

root.mainloop()
