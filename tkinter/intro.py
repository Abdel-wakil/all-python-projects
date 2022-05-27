from tkinter import*


window=Tk()

window.title("The hangman.exe")

window.geometry('700x500')

def button1(argue):

    if argue==1:
        line=Label(window,text="")
        line.pack()
    elif argue==2:
        line=Label(window,text="u clicked me im 2 ty")
        line.pack()





butt1 = Button(window,text="im one",command=lambda:button1(1))
butt2 = Button(window,text="and im two",command=lambda:button1(2))

butt1.pack()
butt2.pack()


window.mainloop()