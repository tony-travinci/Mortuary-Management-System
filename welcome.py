from tkinter import *

root=Tk()

root.geometry("1000x700+0+0")

root.title("Welcome Page")

TopFrame=Frame(root,width=1000,height=100,bg='Green',bd=8,relief='ridge')
TopFrame.pack(side=TOP)

image1=PhotoImage(file="logo.gif")

TopLabel=Label(TopFrame,image=image1)
TopLabel.pack(side='top',fill='both',expand='yes')

InTop=Frame(TopFrame,width=1000,height=100,bg='Green',bd=4,relief='ridge')
InTop.pack(side=BOTTOM)

InTopLabel=Label(InTop,width=450,height=2,font=('times',18,'italic'),bg='Green',text="Welcome, Choose From The Options Below",fg='white')
InTopLabel.pack()

LeftFrame=Frame(root,width=500,height=500,bg='Green',bd=8,relief='ridge')
LeftFrame.pack(side=LEFT)

RightFrame=Frame(root,width=500,height=500,bg='Green',bd=8,relief='ridge')
RightFrame.pack(side=RIGHT)

RegisterButton=Button(LeftFrame,width=45,height=3,bg='white',font=('times',14,'italic'),text="Register Body",fg='Green',bd=8,relief='ridge')
RegisterButton.place(x=6,y=20)

ViewRecordsButton=Button(LeftFrame,width=45,height=3,bg='white',font=('times',14,'italic'),text="View Records",fg='Green',bd=8,relief='ridge')
ViewRecordsButton.place(x=6,y=140)

RegisterButton=Button(LeftFrame,width=45,height=3,bg='white',font=('times',14,'italic'),text="Help And More",fg='Green',bd=8,relief='ridge')
RegisterButton.place(x=6,y=280)

BillButton=Button(RightFrame,width=45,height=3,bg='white',font=('times',14,'italic'),text="Bill And Discharge Body",fg='Green',bd=8,relief='ridge')
BillButton.place(x=6,y=20)

AboutButton=Button(RightFrame,width=45,height=3,bg='white',font=('times',14,'italic'),text="About",fg='Green',bd=8,relief='ridge')
AboutButton.place(x=6,y=140)

LogoutButton=Button(RightFrame,width=45,height=3,bg='white',font=('times',14,'italic'),text="Log Out",fg='Green',bd=8,relief='ridge')
LogoutButton.place(x=6,y=280)

root.mainloop()