from tkinter import*

w="word"

j=["_"]

for i in range(len(w)-1):
    j=j+["_"]

window=Tk()

window.geometry('700x400')

line=Label(window,text=w)
line2=Label(window,text=j,font="verdana 50")

line2.pack()

window.mainloop()


