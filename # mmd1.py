# metr be santi metr

from tkinter import *

root=Tk()

root.geometry("500x300+480+250")

lab1=Label(root,text="عدد کاربر به متر:")
lab1.grid(row=0,column=0)

lab2=Label(root,text="عدد به سانتی متر")
lab2.grid(row=3,column=0)


ent=Entry(root)
ent.grid(row=0,column=1)

def mmd1():
    m=int(ent.get())*100
    tex.insert(INSERT,m)


but=Button(text="تایید",command=mmd1)
but.grid(row=0,column=3)

tex=Text(root,bg="green",height=5,width=25)
tex.grid(row=4,column=0)


root.mainloop()











