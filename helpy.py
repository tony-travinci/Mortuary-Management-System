from tkinter import *
import PIL

root=Tk()
root.geometry("1000x700+0+0")
root.title("Mortuary Management System")
root.iconbitmap("morgue.ico")

class Helpy():
	image1=PhotoImage(file="logo.gif")

	FramehelpTop=Label(root,image=image1,bd=2,relief='ridge')
	FramehelpTop.pack(side=TOP)

	FramehelpBottom=Frame(root,bg='Green',bd=2,relief='ridge',height=700,width=1000)
	FramehelpBottom.pack(side=BOTTOM)

	RequirementsLabel=Label(FramehelpBottom,text="                                                Help and Requirements",font=('times',22,'italic'),fg='white',bg='green')
	RequirementsLabel.place(x=50,y=20)

	Requirement1Label=Label(FramehelpBottom,text='''1. Python 3, most preferably python3.4 ''',font=('times',14,'italic'),fg='white',bg='green')
	Requirement1Label.place(x=50,y=80)

	Requirement2Label=Label(FramehelpBottom,text='''2. tkinter module for python 3  ''',font=('times',14,'italic'),fg='white',bg='green')
	Requirement2Label.place(x=50,y=140)

	Requirement3Label=Label(FramehelpBottom,text='''3. Mysql module for python 3 ''',font=('times',14,'italic'),fg='white',bg='green')
	Requirement3Label.place(x=50,y=200)

	Requirement4Label=Label(FramehelpBottom,text='''4. PIL module for python 3 ''',font=('times',14,'italic'),fg='white',bg='green')
	Requirement4Label.place(x=50,y=260)

	Requirement5Label=Label(FramehelpBottom,text='''Or you can as well contact the developers on:''',font=('times',14,'italic'),fg='white',bg='green')
	Requirement5Label.place(x=50,y=320)

	Requirement6Label=Label(FramehelpBottom,text='''                                                                       Tony : 0703362565''',font=('times',14,'italic'),fg='white',bg='green')
	Requirement6Label.place(x=50,y=370)

	Requirement7Label=Label(FramehelpBottom,text='''                                                                       Andy : 0729285255''',font=('times',14,'italic'),fg='white',bg='green')
	Requirement7Label.place(x=50,y=430)

	Requirement8Label=Label(FramehelpBottom,text='''                                                                       Kibet : UNKNOWN''',font=('times',14,'italic'),fg='white',bg='green')
	Requirement8Label.place(x=50,y=490)


	Requirement9Label=Label(FramehelpBottom,text='''Cyril : 0716329550''',font=('times',14,'italic'),fg='white',bg='green')
	Requirement9Label.place(x=700,y=370)

	Requirement10Label=Label(FramehelpBottom,text='''Regina : 0722556303''',font=('times',14,'italic'),fg='white',bg='green')
	Requirement10Label.place(x=700,y=430)




















root.mainloop()