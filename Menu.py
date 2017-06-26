from tkinter import *

root=Tk()

class menu():
	MenuFrame=Frame(root,width=1366,height=768,bg='Green',bd=2,relief='ridge')
	MenuFrame.pack()

	
	MenuFrameLeft=Frame(MenuFrame,width=1010,height=768,bg='Green',relief='ridge',bd=2)
	MenuFrameLeft.pack(side=LEFT)

	MenuFrameRight=Frame(MenuFrame,width=356,height=768,bg='Green',relief='ridge',bd=2)
	MenuFrameRight.pack(side=RIGHT)

	MenuFrameBottomLeft=Frame(MenuFrameLeft,width=1010,height=768,bg='Green',relief='ridge',bd=2)
	MenuFrameBottomLeft.pack(side=LEFT)

	

	imagemenutop=PhotoImage(file="logo.gif")

	ToppictureLeftLogin=Label(MenuFrameLeft,image=imagemenutop,bd=4,relief='ridge')
	ToppictureLeftLogin.place(x=0,y=0)

	imagemenuright=PhotoImage(file="Egerton.gif")

	ToppictureRightMenu=Label(MenuFrameRight,image=imagemenuright,bd=4,relief='ridge')
	ToppictureRightMenu.place(x=80,y=50)

	RegisterBodyButton=Button(MenuFrameBottomLeft,text="Register Body",height=2,width=20,relief='ridge',bd=2,fg='green',bg='white',font=('times',14,'italic'))
	RegisterBodyButton.place(x=50,y=250)

	ViewRecordsButton=Button(MenuFrameBottomLeft,text="View Records",height=2,width=20,relief='ridge',bd=2,fg='green',bg='white',font=('times',14,'italic'))
	ViewRecordsButton.place(x=50,y=450)

	BillBodyButton=Button(MenuFrameBottomLeft,text="Bill Body",height=2,width=20,relief='ridge',bd=2,fg='green',bg='white',font=('times',14,'italic'))
	BillBodyButton.place(x=50,y=650)

	AdditionalChargesButton=Button(MenuFrameBottomLeft,text="Additional Charges",height=2,width=20,relief='ridge',bd=2,fg='green',bg='white',font=('times',14,'italic'))
	AdditionalChargesButton.place(x=350,y=250)

	PenaltiesButton=Button(MenuFrameBottomLeft,text="Penalties",relief='ridge',height=2,width=20,bd=2,fg='green',bg='white',font=('times',14,'italic'))
	PenaltiesButton.place(x=350,y=450)

	PenaltiesButton=Button(MenuFrameBottomLeft,text="Penalties",relief='ridge',height=2,width=20,bd=2,fg='green',bg='white',font=('times',14,'italic'))
	PenaltiesButton.place(x=350,y=650)

	AdditionalChargesButton=Button(MenuFrameBottomLeft,text="Additional Charges",height=2,width=20,relief='ridge',bd=2,fg='green',bg='white',font=('times',14,'italic'))
	AdditionalChargesButton.place(x=650,y=250)

	PenaltiesButton=Button(MenuFrameBottomLeft,text="Penalties",relief='ridge',height=2,width=20,bd=2,fg='green',bg='white',font=('times',14,'italic'))
	PenaltiesButton.place(x=650,y=450)

	PenaltiesButton=Button(MenuFrameBottomLeft,text="Penalties",relief='ridge',height=2,width=20,bd=2,fg='green',bg='white',font=('times',14,'italic'))
	PenaltiesButton.place(x=650,y=650)






root.mainloop()
