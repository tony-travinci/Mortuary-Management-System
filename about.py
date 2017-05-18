from tkinter import *
import PIL

root=Tk()
root.geometry("1000x700+0+0")
root.title("Mortuary Management System")
root.iconbitmap("morgue.ico")

class About():
	image1=PhotoImage(file="logo.gif")

	FrameaboutTop=Label(root,image=image1,bd=2,relief='ridge')
	FrameaboutTop.pack(side=TOP)

	FrameAboutBottom=Frame(root,bg='Green',bd=2,relief='ridge',height=700,width=1000)
	FrameAboutBottom.pack(side=BOTTOM)

	NameLabel=Label(FrameAboutBottom,text="Name",font=('times',14,'italic'),fg='white',bg='green')
	NameLabel.place(x=50,y=20)

	RoleLabel=Label(FrameAboutBottom,text="Role",font=('times',14,'italic'),fg='white',bg='green')
	RoleLabel.place(x=800,y=20)

	AnthonyLabel=Label(FrameAboutBottom,text="Anthony Muchiri",font=('times',14,'italic'),fg='white',bg='green')
	AnthonyLabel.place(x=50,y=100)

	RoleAnthonyLabel=Label(FrameAboutBottom,text="Lead Programmer",font=('times',14,'italic'),fg='white',bg='green')
	RoleAnthonyLabel.place(x=800,y=100)

	AndyLabel=Label(FrameAboutBottom,text="Andrew Wambugu",font=('times',14,'italic'),fg='white',bg='green')
	AndyLabel.place(x=50,y=180)

	RoleAndyLabel=Label(FrameAboutBottom,text="Database Designer and Administrator",font=('times',14,'italic'),fg='white',bg='green')
	RoleAndyLabel.place(x=650,y=180)

	CyrilLabel=Label(FrameAboutBottom,text="Cyril Paul",font=('times',14,'italic'),fg='white',bg='green')
	CyrilLabel.place(x=50,y=260)

	RoleCyrilLabel=Label(FrameAboutBottom,text="Programmer and Documentation Preparation",font=('times',14,'italic'),fg='white',bg='green')
	RoleCyrilLabel.place(x=600,y=260)

	ReginaLabel=Label(FrameAboutBottom,text="Regina Njeri Ndiritu",font=('times',14,'italic'),fg='white',bg='green')
	ReginaLabel.place(x=50,y=340)

	RoleReginaLabel=Label(FrameAboutBottom,text="Program Manager and Documentation",font=('times',14,'italic'),fg='white',bg='green')
	RoleReginaLabel.place(x=650,y=340)

	KibetLabel=Label(FrameAboutBottom,text="Kibet Korir",font=('times',14,'italic'),fg='white',bg='green')
	KibetLabel.place(x=50,y=420)

	RoleKibetLabel=Label(FrameAboutBottom,text="Program Documentation",font=('times',14,'italic'),fg='white',bg='green')
	RoleKibetLabel.place(x=780,y=420)

	BackButton=Button(FrameAboutBottom,text="Back",font=('times',20,'italic'),bg='green',fg='white',bd=2,relief='ridge')
	BackButton.place(x=915,y=460)



root.mainloop()