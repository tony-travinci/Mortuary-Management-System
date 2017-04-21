from tkinter import *
root=Tk()
root.geometry("1000x700+0+0")
root.title("Coming Soon")

ComingSoonOne1=Frame(root,width=1000,height=700,bg='Green',bd=8,relief='ridge')
ComingSoonOne1.pack()
ComingSoonLabel1=Label(ComingSoonOne1,text="Coming Soon",font=('times',30,'italic'),bg='Green',fg='white')
ComingSoonLabel1.place(x=380,y=300)
root.mainloop()