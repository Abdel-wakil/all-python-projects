w="word"

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


empty_places()
for i in range(10):

    display()

    guessing_func()




