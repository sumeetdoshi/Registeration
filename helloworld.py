from tkinter import *
root=Tk()
def getvalue():
    print(namevalue.get())
    print(passvalue.get())
root.geometry("600x500")
name=Label(text="ENTER NAME:",relief=RIDGE)
name.grid()
password=Label(text="ENTER PASSWORD?",relief=RIDGE)
password.grid(row=1)
passvalue=StringVar()
namevalue=StringVar()
nameentry=Entry(textvariable=namevalue)
passentry=Entry(textvariable=passvalue)
nameentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)
c=Checkbutton(text="KEEP ME LOGGED IN")
c.grid(row=2,column=1)
b=Button(text="LOG IN",command=getvalue)
b.grid(row=2,column=0)

root.mainloop()
