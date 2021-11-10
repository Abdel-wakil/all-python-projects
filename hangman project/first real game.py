import random

list=[]

with open("/Users/abdelali khamsi/Desktop/python sub text saves/hangman project/words lists/liste_francais.txt") as file:

    text=file.read()

# print(text)

list=text.split()

w=random.choice(list)


print(w)

p=True

j=["_"]

let1=[]
for i in w:
    let1+=[i]

#print(let1)

################### FUNCTIONS-DEPARTEMENT ###################
                            ##1##

def empty_places():
    global j


    for i in range(len(w)-1):
        j=j+["_"]
                            ##2##

def display():
    print("")
    print("       ","  ".join(j))
    print("")

                            ##3##

def guessing_func():
    Let_guess=input("guess a letter pls: ")
    if Let_guess in w:
        index_guess=let1.index(Let_guess)
        j[index_guess]=Let_guess
    else:
        print("")
        print("  ","ce mot ne contient pas cette lettre veuillez faire un autre essaie svp")
                   ##############################
empty_places()
while p==True:

    display()

    if j==let1:
        print("ouiii",w,"est le mot correct")
        break

    guessing_func()