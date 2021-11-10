import random
from tkinter import*



list=[]

with open("/Users/abdelali khamsi/Desktop/python sub text saves/hangman project/words lists/liste_francais.txt") as file:
    text=file.read()

list=text.split()

w=random.choice(list)

window=Tk()
window.geometry('1350x760')
window.title('The hangman.exe')
#w="diament"

on_off=0
let1=[]
for z in w:
    let1+=[z]

l_index=[]

var_1=StringVar()
var_2=StringVar()

j=["_"]

for i in range(len(w)-1):
    j=j+["_"]






#######################func#############

def hangman_algo(guess):
    global l_index,w,won
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
    maj="A"
    exep="â"
    hangman_algo(letter)
    hangman_algo(maj)
    hangman_algo(exep)
    button_a.configure(state='disabled')
    check_if_u_won_func()
def func_b():
    letter="b"
    maj="B"
    hangman_algo(letter)
    hangman_algo(maj)
    button_b.configure(state='disabled')
    check_if_u_won_func()
def func_c():
    letter="c"
    maj="C"
    hangman_algo(letter)
    hangman_algo(maj)
    button_c.configure(state='disabled')
    check_if_u_won_func()
def func_d():
    letter="d"
    maj="D"
    hangman_algo(letter)
    hangman_algo(maj)
    button_d.configure(state='disabled')
    check_if_u_won_func()
def func_é():
    letter="é"
    hangman_algo(letter)
    button_é.configure(state='disabled')
    check_if_u_won_func()
def func_e():
    letter="e"
    maj="E"
    hangman_algo(letter)
    hangman_algo(maj)
    button_e.configure(state='disabled')
    check_if_u_won_func()
def func_f():
    letter="f"
    maj="F"
    hangman_algo(letter)
    hangman_algo(maj)
    button_f.configure(state='disabled')
    check_if_u_won_func()
def func_g():
    letter="g"
    maj="G"
    hangman_algo(letter)
    hangman_algo(maj)
    button_g.configure(state='disabled')
    check_if_u_won_func()
def func_h():
    letter="h"
    maj="H"
    hangman_algo(letter)
    hangman_algo(maj)
    button_h.configure(state='disabled')
    check_if_u_won_func()
def func_i():
    letter="i"
    maj="I"
    hangman_algo(letter)
    hangman_algo(maj)
    button_i.configure(state='disabled')
    check_if_u_won_func()
def func_j():
    letter="j"
    maj="J"
    hangman_algo(letter)
    hangman_algo(maj)
    button_j.configure(state='disabled')
    check_if_u_won_func()
def func_k():
    letter="k"
    maj="K"
    hangman_algo(letter)
    hangman_algo(maj)
    button_k.configure(state='disabled')
    check_if_u_won_func()
def func_l():
    letter="l"
    maj="L"
    hangman_algo(letter)
    hangman_algo(maj)
    button_l.configure(state='disabled')
    check_if_u_won_func()
def func_m():
    letter="m"
    maj="M"
    hangman_algo(letter)
    hangman_algo(maj)
    button_m.configure(state='disabled')
    check_if_u_won_func()
def func_n():
    letter="n"
    maj="N"
    hangman_algo(letter)
    hangman_algo(maj)
    button_n.configure(state='disabled')
    check_if_u_won_func()
def func_o():
    letter="o"
    maj="O"
    hangman_algo(letter)
    hangman_algo(maj)
    button_o.configure(state='disabled')
    check_if_u_won_func()
def func_p():
    letter="p"
    maj="P"
    hangman_algo(letter)
    hangman_algo(maj)
    button_p.configure(state='disabled')
    check_if_u_won_func()
def func_q():
    letter="q"
    maj="Q"
    hangman_algo(letter)
    hangman_algo(maj)
    button_q.configure(state='disabled')
    check_if_u_won_func()
def func_r():
    letter="r"
    maj="R"
    hangman_algo(letter)
    hangman_algo(maj)
    button_r.configure(state='disabled')
    check_if_u_won_func()
def func_s():
    letter="s"
    maj="S"
    hangman_algo(letter)
    hangman_algo(maj)
    button_s.configure(state='disabled')
    check_if_u_won_func()
def func_t():
    letter="t"
    maj="T"
    hangman_algo(letter)
    hangman_algo(maj)
    button_t.configure(state='disabled')
    check_if_u_won_func()
def func_u():
    letter="u"
    maj="U"
    hangman_algo(letter)
    hangman_algo(maj)
    button_u.configure(state='disabled')
    check_if_u_won_func()
def func_v():
    letter="v"
    maj="V"
    hangman_algo(letter)
    hangman_algo(maj)
    button_v.configure(state='disabled')
    check_if_u_won_func()
def func_w():
    letter="w"
    maj="W"
    hangman_algo(letter)
    hangman_algo(maj)
    button_w.configure(state='disabled')
    check_if_u_won_func()
def func_x():
    letter="x"
    maj="X"
    hangman_algo(letter)
    hangman_algo(maj)
    button_x.configure(state='disabled')
    check_if_u_won_func()
def func_y():
    letter="y"
    maj="Y"
    hangman_algo(letter)
    hangman_algo(maj)
    button_y.configure(state='disabled')
    check_if_u_won_func()
def func_z():
    letter="z"
    maj="Z"
    hangman_algo(letter)
    hangman_algo(maj)
    button_z.configure(state='disabled')
    check_if_u_won_func()
def func_è():
    letter="è"
    hangman_algo(letter)
    button_è.configure(state='disabled')
    check_if_u_won_func()
def func_ê():
    letter="ê"
    hangman_algo(letter)
    button_ê.configure(state='disabled')
    check_if_u_won_func()



####################################################################


def show_hide_func():
    global on_off,line,w
    on_off+=1
    if on_off%2!=0:
        line=Label(window,text=w,font="verdana 20")
        line.place(x=300,y=100)

    elif on_off%2==0:
        line.place_forget()


def new_game():
    global w,j,won,let1,on_off

    line2.pack_forget()
    w=random.choice(list)
    j=["_"]
    for i in range(len(w)-1):
        j=j+["_"]

    var_1.set(j)
    line2.pack()
    won.place_forget()
    let1=[]
    for z in w:
        let1+=[z]
    new_game.place_forget()
    line.place_forget()
    if on_off%2!=0:
        on_off+=1
    button_a.configure(state='normal')
    button_b.configure(state='normal')
    button_c.configure(state='normal')
    button_d.configure(state='normal')
    button_e.configure(state='normal')
    button_f.configure(state='normal')
    button_g.configure(state='normal')
    button_h.configure(state='normal')
    button_i.configure(state='normal')
    button_j.configure(state='normal')
    button_k.configure(state='normal')
    button_l.configure(state='normal')
    button_m.configure(state='normal')
    button_n.configure(state='normal')
    button_o.configure(state='normal')
    button_p.configure(state='normal')
    button_q.configure(state='normal')
    button_r.configure(state='normal')
    button_s.configure(state='normal')
    button_t.configure(state='normal')
    button_u.configure(state='normal')
    button_v.configure(state='normal')
    button_w.configure(state='normal')
    button_x.configure(state='normal')
    button_y.configure(state='normal')
    button_z.configure(state='normal')
    button_é.configure(state='normal')
    button_è.configure(state='normal')
    button_ê.configure(state='normal')



def check_if_u_won_func():
    global won,j,w
    if j==let1:
        won=Label(window,text="yes u won thats the right word",font="40")
        won.place(x=540,y=300)
        new_game.place(x=1000,y=100)




##########################creating stuff################################

pos=Label(window,text="            ",font="verdana 50")
pos1=Label(window,text="            ",font="verdana 50")

line2=Label(window,font="verdana 50",textvariable=var_1)


################buttons############################
button_a=Button(window,text="a",font="bold 15",padx=20,pady=10,command=func_a)
button_b=Button(window,text="b",font="bold 15",padx=20,pady=10,command=func_b)
button_c=Button(window,text="c",font="bold 15",padx=20,pady=10,command=func_c)
button_d=Button(window,text="d",font="bold 15",padx=20,pady=10,command=func_d)
button_e=Button(window,text="e",font="bold 15",padx=20,pady=10,command=func_e)
button_é=Button(window,text="é",font="bold 15",padx=20,pady=10,command=func_é)
button_f=Button(window,text="f",font="bold 15",padx=20,pady=10,command=func_f)
button_g=Button(window,text="g",font="bold 15",padx=20,pady=10,command=func_g)
button_h=Button(window,text="h",font="bold 15",padx=20,pady=10,command=func_h)
button_i=Button(window,text="i",font="bold 15",padx=20,pady=10,command=func_i)
button_j=Button(window,text="j",font="bold 15",padx=20,pady=10,command=func_j)
button_k=Button(window,text="k",font="bold 15",padx=20,pady=10,command=func_k)
button_l=Button(window,text="l",font="bold 15",padx=22,pady=10,command=func_l)
button_m=Button(window,text="m",font="bold 15",padx=18,pady=10,command=func_m)
button_n=Button(window,text="n",font="bold 15",padx=20,pady=10,command=func_n)
button_o=Button(window,text="o",font="bold 15",padx=20,pady=10,command=func_o)
button_p=Button(window,text="p",font="bold 15",padx=20,pady=10,command=func_p)
button_q=Button(window,text="q",font="bold 15",padx=20,pady=10,command=func_q)
button_r=Button(window,text="r",font="bold 15",padx=20,pady=10,command=func_r)
button_s=Button(window,text="s",font="bold 15",padx=20,pady=10,command=func_s)
button_t=Button(window,text="t",font="bold 15",padx=20,pady=10,command=func_t)
button_u=Button(window,text="u",font="bold 15",padx=20,pady=10,command=func_u)
button_v=Button(window,text="v",font="bold 15",padx=20,pady=10,command=func_v)
button_w=Button(window,text="w",font="bold 15",padx=18,pady=10,command=func_w)
button_x=Button(window,text="x",font="bold 15",padx=20,pady=10,command=func_x)
button_y=Button(window,text="y",font="bold 15",padx=20,pady=10,command=func_y)
button_z=Button(window,text="z",font="bold 15",padx=20,pady=10,command=func_z)
button_è=Button(window,text="è",font="bold 15",padx=20,pady=10,command=func_è)
button_ê=Button(window,text="ê",font="bold 15",padx=20,pady=10,command=func_ê)

##################creating buttons for letters###############

surrender=Button(window,text="show and hide word",padx=20,command=show_hide_func)

new_game=Button(window,text="play again",padx=20,command=new_game)



#######################pos stuff#####################

pos.pack()
pos1.pack()

line2.pack()
var_1.set(j)

#######buttons placment#############
button_a.place(x=330,y=400)
button_z.place(x=400,y=400)
button_e.place(x=470,y=400)
button_r.place(x=540,y=400)
button_t.place(x=610,y=400)
button_y.place(x=680,y=400)
button_u.place(x=750,y=400)
button_i.place(x=820,y=400)
button_o.place(x=890,y=400)
button_p.place(x=960,y=400)
button_q.place(x=330,y=480)
button_s.place(x=400,y=480)
button_d.place(x=470,y=480)
button_f.place(x=540,y=480)
button_g.place(x=610,y=480)
button_h.place(x=680,y=480)
button_j.place(x=750,y=480)
button_k.place(x=820,y=480)
button_l.place(x=890,y=480)
button_m.place(x=960,y=480)
button_w.place(x=380,y=560)
button_x.place(x=450,y=560)
button_c.place(x=520,y=560)
button_v.place(x=590,y=560)
button_b.place(x=660,y=560)
button_n.place(x=730,y=560)
button_é.place(x=800,y=560)
button_è.place(x=870,y=560)
button_ê.place(x=940,y=560)



#################################
surrender.place(x=100,y=100)













##################################










window.mainloop()