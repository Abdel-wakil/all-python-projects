w="wrrd"

p=True

j=["_"]
l_indexs=[]
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
    global l_indexs
    Let_guess=input("guess a letter pls: ")
    for n in let1:
        print(n)
        if n==Let_guess:
            l_indexs+=[let1.index(n)]
        print(l_indexs)
    while len(l_indexs)!=0:
        j[l_indexs[-1]]=Let_guess
        l_indexs.pop(-1)
    #
    # else:
    #     print("")
    #     print("  ","wrong letter try again")

empty_places()
while p==True:

    display()

    if j==let1:
        print("yess",w,"is the right guess")
        p=False
        break

    guessing_func()