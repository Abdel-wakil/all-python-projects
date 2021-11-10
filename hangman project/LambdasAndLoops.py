import random
from tkinter import*



list=[]

with open("C://Users//Abdelkoddous//Desktop//PythonProgramming//liste_francais.txt") as file:
    text=file.read()

list=text.split()

w=random.choice(list)

window=Tk()
window.geometry('1350x760')

w="football"


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

    if j==let1:
        won=Label(window,text="yes u won thats the right word",font="40")
        won.place(x=580,y=300)
        new_game=Button(window,text="play again",padx=20)#,command=new_game)
        new_game.place(x=1000,y=100)





###############______letters_______################

# compressed version
def func_letter(letter):
    hangman_algo(letter)
####################################################################

def surrender_func():
    answer=Label(window,text=w,font="verdana 20")
    answer.place(x=300,y=100)

def new_game():
    new=Label(window,text="work still in progress :)")
    new.pack()

##########################creating stuff################################

pos=Label(window,text="            ",font="verdana 50")
pos1=Label(window,text="            ",font="verdana 50")

line2=Label(window,font="verdana 50",textvariable=var_1)

################buttons############################



# Different approach
AllLetters = ["a", "b", "c", "d", "e", "f", "g" ]
Buttons = [] # Empty list of buttons
x_increment = 0

for myletter in AllLetters:

    # Add a NEW different button to the list
    # This button will be the last element in the list
    Buttons += [ Button(window, text=myletter, padx=20, pady=10, command=lambda myletter=myletter:func_letter(myletter)) ]

    # Place the button
    Buttons[-1].place(x=400+x_increment, y=400)
    x_increment += 60

print(Buttons)
##################creating buttons for letters###############

surrender=Button(window,text="show word",padx=20,command=surrender_func)




#######################pos stuff#####################

pos.pack()
pos1.pack()

line2.pack()
var_1.set(j)

# #######buttons placment#############
# button_a.place(x=400,y=400)
# button_b.place(x=460,y=400)
# button_c.place(x=520,y=400)
# button_d.place(x=580,y=400)
# button_e.place(x=640,y=400)
# button_f.place(x=700,y=400)
# button_g.place(x=760,y=400)
# button_h.place(x=820,y=400)
# button_i.place(x=880,y=400)
# button_j.place(x=940,y=400)
# button_k.place(x=400,y=450)
# button_l.place(x=460,y=450)
# button_m.place(x=520,y=450)
# button_n.place(x=580,y=450)
# button_o.place(x=640,y=450)
# button_p.place(x=700,y=450)
# button_q.place(x=760,y=450)
# button_r.place(x=820,y=450)
# button_s.place(x=880,y=450)
# button_t.place(x=940,y=450)
# button_u.place(x=400,y=500)
# button_v.place(x=460,y=500)
# button_w.place(x=520,y=500)
# button_x.place(x=580,y=500)
# button_y.place(x=640,y=500)
# button_z.place(x=700,y=500)
# button_é.place(x=760,y=500)

#################################
surrender.place(x=100,y=100)











##################################










window.mainloop()