from tkinter import*
from PIL import ImageTk,Image

window=Tk()


###############locations################
location_1=Image.open('C:/Users/abdelali khamsi/Desktop/hangman pics/1.png')
location_2=Image.open('C:/Users/abdelali khamsi/Desktop/hangman pics/2.png')
location_3=Image.open('C:/Users/abdelali khamsi/Desktop/hangman pics/3.png')
location_4=Image.open('C:/Users/abdelali khamsi/Desktop/hangman pics/4.png')
location_5=Image.open('C:/Users/abdelali khamsi/Desktop/hangman pics/5.png')
location_6=Image.open('C:/Users/abdelali khamsi/Desktop/hangman pics/6.png')
location_7=Image.open('C:/Users/abdelali khamsi/Desktop/hangman pics/7.png')
location_8=Image.open('C:/Users/abdelali khamsi/Desktop/hangman pics/8.png')
#location_9=Image.open('C:/Users/abdelali khamsi/Desktop/hangman pics/9.png')
########################################

pic_1=ImageTk.PhotoImage(location_1)
pic_2=ImageTk.PhotoImage(location_2)
pic_3=ImageTk.PhotoImage(location_3)
pic_4=ImageTk.PhotoImage(location_4)
pic_5=ImageTk.PhotoImage(location_5)
pic_6=ImageTk.PhotoImage(location_6)
pic_7=ImageTk.PhotoImage(location_7)
pic_8=ImageTk.PhotoImage(location_8)
#pic_9=ImageTk.PhotoImage(location_9)

########################################

labe_1=Label(image=pic_1)
labe_2=Label(image=pic_2)
labe_3=Label(image=pic_3)
labe_4=Label(image=pic_4)
labe_5=Label(image=pic_5)
labe_6=Label(image=pic_6)
labe_7=Label(image=pic_7)
labe_8=Label(image=pic_8)
#labe_9=Label(image=pic_9)

############placement##################

labe_1.place(x=300,y=400)
labe_2.place(x=415,y=120)
labe_3.place(x=415,y=120)
labe_4.place(x=435,y=140)
labe_5.place(x=735,y=120)
labe_6.place(x=700,y=180)
labe_7.place(x=735,y=268)
labe_8.place(x=660,y=300)
# labe_9.pack()

######################################


window.mainloop()




















