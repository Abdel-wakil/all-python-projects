w="word"

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


def display():
    print("")
    print("       ","  ".join(j))
    print("")

                            ##2##

def guessing_func():
    Let_guess=input("guess a letter pls: ")
    if Let_guess in w:
        index_guess=let1.index(Let_guess)
        j[index_guess]=Let_guess
    else:
        print("")
        print("  ","wrong letter try again")

empty_places()
while p==True:

    display()

    if j==let1:
        print("yess",w,"is the right guess")
        p=False
        break

    guessing_func()




