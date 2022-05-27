from tkinter import*

window=Tk()
window.geometry('700x500')

w="word"


let1=[]
for z in w:
    let1+=[z]

l_index=[]

var_1=StringVar()

j=["_"]

for i in range(len(w)-1):
    j=j+["_"]






#######################func#############

def hangman_algo(guess):
    global l_index
    index=-1
    for u in w:
        index+=1
        if u==guess:
            l_index+=[index]


    for y in range(len(l_index)):
        j[l_index[-1]]=guess
        l_index.pop(-1)
    var_1.set(j)












def func_w():
    letter="w"
    hangman_algo(letter)

def func_o():
    letter="o"
    hangman_algo(letter)

def func_r():
    letter="r"
    hangman_algo(letter)

def func_d():
    letter="d"
    hangman_algo(letter)







##########################creating stuff#####################"

pos=Label(window,text="            ",font="verdana 50")
pos1=Label(window,text="            ",font="verdana 50")

line2=Label(window,font="verdana 50",textvariable=var_1)


button_w=Button(window,text="w",padx=10,pady=10,command=func_w)
button_o=Button(window,text="o",padx=10,pady=10,command=func_o)
button_r=Button(window,text="r",padx=10,pady=10,command=func_r)
button_d=Button(window,text="d",padx=10,pady=10,command=func_d)

#######################pos stuff#####################

pos.pack()
pos1.pack()

line2.place(x=515,y=200)
var_1.set(j)

button_w.place(x=600,y=400)
button_o.place(x=640,y=400)
button_r.place(x=680,y=400)
button_d.place(x=720,y=400)

#################################




window.mainloop()