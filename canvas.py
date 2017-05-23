from tkinter import *
import os
import datetime
import time
import mysql.connector
import subprocess
#import ghostscript
import PIL
from PIL import Image

root=Tk()

Frame1=Frame(root)
Frame1.pack()
Frame2=Frame(root)
LeftFrameFrame2=Frame(Frame2,height=700,width=700,relief='ridge',bd=2)
LeftFrameFrame2.pack(side=LEFT)

RightFrameFrame2=Frame(Frame2,width=300,height=700,bd=2,relief='ridge',bg='white')
RightFrameFrame2.pack(side=RIGHT)


BackButton=Button(RightFrameFrame2,width=20,height=2,text='Back To Records',font=('times',14,'italic'),bd=2,fg='green',bg='white',relief='ridge')
BackButton.place(x=40,y=50)

OptionsButton=Button(RightFrameFrame2,width=20,height=2,text='Back To Options Menu',font=('times',14,'italic'),bd=2,fg='green',bg='white',relief='ridge')
OptionsButton.place(x=40,y=220)

PrintButton=Button(RightFrameFrame2,width=20,height=2,text='Print Receipt',font=('times',14,'italic'),bd=2,fg='green',bg='white',relief='ridge')
PrintButton.place(x=40,y=390)

LogOutButton=Button(RightFrameFrame2,width=20,height=2,text='Log Out',font=('times',14,'italic'),fg='green',bg='white',bd=2,relief='ridge')
LogOutButton.place(x=40,y=560)
#Frame2.pack()


NameEntry=Entry(Frame1)
NameEntry.pack()

receipt1=Canvas(LeftFrameFrame2,height=700,width=700,bg='white')


#receipt1.create_line(1000, 50, 1000,50,fill="green",dash=(4,4))
#receipt1.create_line(0,650,700,0,fill="green",dash=(4,4))

#receipt1.create_line(50,700,50,0,fill="green",dash=(4,4))

#-------------------(stretch x,origin,stretch y,origin)
#receipt1.create_line(1000,10,0,10,fill="green",dash=(4,4))


image5=PhotoImage(file="egerton.gif")
receipt1.create_image(280,120,image=image5)


receipt1.pack()



Frame5=Frame(root)
#Frame5.pack()




now=datetime.datetime.now()
today=now.date()


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



    
    cursor.close()
    cnx.close()
    

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

#-----------------------(  x,  y)------------------------------------------



    

    receipt1.create_text(225, 250, anchor=W, font="times",text=("Mortuary Receipt"))
    

    receipt1.create_text(50, 300, anchor=W, font="times",text=("Name"))
    receipt1.create_text(400, 300, anchor=W, font="times",text=(name[0]))


    
    receipt1.create_text(50, 330, anchor=W, font="times",text=("Body Washing"))
    receipt1.create_text(400, 330, anchor=W, font="times",text=(bodywash[0]))

    receipt1.create_text(50, 360, anchor=W, font="times",text=("Coffin Provision"))
    receipt1.create_text(400, 360, anchor=W, font="times",text=(Coffin[0]))

    receipt1.create_text(50, 390, anchor=W, font="times",text=("Embalming"))
    receipt1.create_text(400, 390, anchor=W, font="times",text=(embalming[0]))

    receipt1.create_text(50, 420, anchor=W, font="times",text=("VIP"))
    receipt1.create_text(400, 420, anchor=W, font="times",text=(VIP[0]))

    receipt1.create_text(50, 450, anchor=W, font="times",text=("Flowers"))
    receipt1.create_text(400, 450, anchor=W, font="times",text=(Flowers[0]))

    receipt1.create_text(50, 480, anchor=W, font="times",text=("Hearse"))
    receipt1.create_text(400, 480, anchor=W, font="times",text=(Hearse[0]))

    receipt1.create_text(50, 510, anchor=W, font="times",text=("Tent"))
    receipt1.create_text(400, 510, anchor=W, font="times",text=(Tent[0]))

    receipt1.create_text(50, 540, anchor=W, font="times",text=("Post Mortem"))
    receipt1.create_text(400, 540, anchor=W, font="times",text=(PostMortem[0]))

    receipt1.create_text(50, 570, anchor=W, font="times",text=("Number Of Days"))
    receipt1.create_text(400, 570, anchor=W, font="times",text=(nowdate.days))

    receipt1.create_text(50, 600, anchor=W, font="times",text=("Cost Of Days"))
    receipt1.create_text(400, 600, anchor=W, font="times",text=(dayssum))

    receipt1.create_text(50, 650, anchor=W, font="times",text=("Total"))
    receipt1.create_text(400, 650, anchor=W, font="times",text=(abstotal))



    Frame1.pack_forget()
    Frame2.pack()
name1=NameEntry.get()
def printout():
	receipt1.update()
	receipt1.postscript(file="tmp.ps")
	#img = Image.open("tmp.eps")
	#img.save("circles.png", "png")
Button1=Button(Frame1,text="Submit",command=connect)
Button1.pack()

Button2=Button(Frame1,text="Print Receipt",command=printout)
Button2.pack()

PrintButton=Button(RightFrameFrame2,width=20,height=2,text='Print Receipt',font=('times',14,'italic'),command=printout,bd=2,fg='green',bg='white',relief='ridge')
PrintButton.place(x=40,y=390)



root.mainloop()
