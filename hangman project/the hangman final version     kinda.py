import random

list=[]

with open("C:/Users/Abdelwakil/Desktop/python sub text saves/hangman project/words lists/liste_francais.txt") as file:

    text=file.read()

# print(text)

list=text.split()

w=random.choice(list)

attemps=10

l_index=[]

#print(w)

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
    global l_index,attemps
    index=-1
    letter=input("enter guess: ")

    for u in w:
        index+=1
        if u==letter:
            l_index+=[index]
    if letter not in w:
        print("")
        print("  ","ce mot ne contient pas cette lettre veuillez faire un autre essaie svp")
        attemps-=1
        print(" ")
        print("     ","u have",attemps,"attemps left")

    for z in range(len(l_index)):
        j[l_index[-1]]=letter
        l_index.pop(-1)



                   ##############################
empty_places()
while p==True:

    display()

    if j==let1:
        print("ouiii",w,"est le mot correct")
        break

    guessing_func()



    if attemps ==0:
        print(" ")
        print("     game over ")
        print(" ")
        print("the word was ",w)
        break

