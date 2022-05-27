from tkinter import*
from PIL import ImageTk,Image


window=Tk()


loc=Image.open('C:/Users/Abdelwakil/Desktop/test/pic.jpg')

pic=ImageTk.PhotoImage(loc)

labe=Label(image=pic)

labe.pack()

window.mainloop()