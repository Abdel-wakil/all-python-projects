import random
from tkinter import*
list=[]

with open("/Users/abdelali khamsi/Desktop/python sub text saves/hangman project/words lists/liste_francais.txt") as file:
    text=file.read()

list=text.split()

w=random.choice(list)

window=Tk()
window.geometry('700x500')

#w="word"


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

###############______letters_______################
def func_a():
    letter="a"
    hangman_algo(letter)
def func_b():
    letter="b"
    hangman_algo(letter)
def func_c():
    letter="c"
    hangman_algo(letter)
def func_d():
    letter="d"
    hangman_algo(letter)
def func_é():
    letter="é"
    hangman_algo(letter)
def func_e():
    letter="e"
    hangman_algo(letter)
def func_f():
    letter="f"
    hangman_algo(letter)
def func_g():
    letter="g"
    hangman_algo(letter)
def func_h():
    letter="h"
    hangman_algo(letter)
def func_i():
    letter="i"
    hangman_algo(letter)
def func_j():
    letter="j"
    hangman_algo(letter)
def func_k():
    letter="k"
    hangman_algo(letter)
def func_l():
    letter="l"
    hangman_algo(letter)
def func_m():
    letter="m"
    hangman_algo(letter)
def func_n():
    letter="n"
    hangman_algo(letter)
def func_o():
    letter="o"
    hangman_algo(letter)
def func_p():
    letter="p"
    hangman_algo(letter)
def func_q():
    letter="q"
    hangman_algo(letter)
def func_r():
    letter="r"
    hangman_algo(letter)
def func_s():
    letter="s"
    hangman_algo(letter)
def func_t():
    letter="t"
    hangman_algo(letter)
def func_u():
    letter="u"
    hangman_algo(letter)
def func_v():
    letter="v"
    hangman_algo(letter)
def func_w():
    letter="w"
    hangman_algo(letter)
def func_x():
    letter="x"
    hangman_algo(letter)
def func_y():
    letter="y"
    hangman_algo(letter)
def func_z():
    letter="z"
    hangman_algo(letter)
####################################################################

def surrender_func():
    answer=Label(window,text=w,font="verdana 20")
    answer.pack()











##########################creating stuff################################

pos=Label(window,text="            ",font="verdana 50")
pos1=Label(window,text="            ",font="verdana 50")

line2=Label(window,font="verdana 50",textvariable=var_1)


################buttons############################
button_a=Button(window,text="a",padx=10,pady=10,command=func_a)
button_b=Button(window,text="b",padx=10,pady=10,command=func_b)
button_c=Button(window,text="c",padx=10,pady=10,command=func_c)
button_d=Button(window,text="d",padx=10,pady=10,command=func_d)
button_e=Button(window,text="e",padx=10,pady=10,command=func_e)
button_é=Button(window,text="é",padx=10,pady=10,command=func_é)
button_f=Button(window,text="f",padx=10,pady=10,command=func_f)
button_g=Button(window,text="g",padx=10,pady=10,command=func_g)
button_h=Button(window,text="h",padx=10,pady=10,command=func_h)
button_i=Button(window,text="i",padx=10,pady=10,command=func_i)
button_j=Button(window,text="j",padx=10,pady=10,command=func_j)
button_k=Button(window,text="k",padx=10,pady=10,command=func_k)
button_l=Button(window,text="l",padx=10,pady=10,command=func_l)
button_m=Button(window,text="m",padx=10,pady=10,command=func_m)
button_n=Button(window,text="n",padx=10,pady=10,command=func_n)
button_o=Button(window,text="o",padx=10,pady=10,command=func_o)
button_p=Button(window,text="p",padx=10,pady=10,command=func_p)
button_q=Button(window,text="q",padx=10,pady=10,command=func_q)
button_r=Button(window,text="r",padx=10,pady=10,command=func_r)
button_s=Button(window,text="s",padx=10,pady=10,command=func_s)
button_t=Button(window,text="t",padx=10,pady=10,command=func_t)
button_u=Button(window,text="u",padx=10,pady=10,command=func_u)
button_v=Button(window,text="v",padx=10,pady=10,command=func_v)
button_w=Button(window,text="w",padx=10,pady=10,command=func_w)
button_x=Button(window,text="x",padx=10,pady=10,command=func_x)
button_y=Button(window,text="y",padx=10,pady=10,command=func_y)
button_z=Button(window,text="z",padx=10,pady=10,command=func_z)
##################creating buttons for letters###############

surrender=Button(window,text="surrender",padx=20,command=surrender_func)





#######################pos stuff#####################

pos.pack()
pos1.pack()

line2.place(x=515,y=200)
var_1.set(j)

#######buttons placment#############
button_a.place(x=100,y=400)
button_b.place(x=140,y=400)
button_c.place(x=180,y=400)
button_d.place(x=220,y=400)
button_e.place(x=260,y=400)
button_f.place(x=300,y=400)
button_g.place(x=340,y=400)
button_h.place(x=380,y=400)
button_i.place(x=420,y=400)
button_j.place(x=460,y=400)
button_k.place(x=500,y=400)
button_l.place(x=540,y=400)
button_m.place(x=580,y=400)
button_n.place(x=620,y=400)
button_o.place(x=660,y=400)
button_p.place(x=700,y=400)
button_q.place(x=740,y=400)
button_r.place(x=780,y=400)
button_s.place(x=820,y=400)
button_t.place(x=860,y=400)
button_u.place(x=900,y=400)
button_v.place(x=940,y=400)
button_w.place(x=980,y=400)
button_x.place(x=1020,y=400)
button_y.place(x=1060,y=400)
button_z.place(x=1100,y=400)
button_é.place(x=1140,y=400)

#################################
surrender.place(x=100,y=100)











##################################










window.mainloop()