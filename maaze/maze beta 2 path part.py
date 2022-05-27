maze1 = [["#", "#", "#", "#", "#", "#", "#"],
         ["#", " ", " ", " ", "#", "S", "#"],
         ["#", " ", "#", " ", "#", " ", "#"],
         ["#", " ", "#", " ", " ", " ", "#"],
         ["#", " ", "#", " ", "#", "#", "#"],
         ["#", " ", " ", " ", " ", " ", "#"],
         ["#", "#", "#", "F", "#", "#", "#"]]


for x_S in range(7):
    if "S" in maze1[x_S]:
        y_S=maze1[x_S].index('S')
        break

#print(x_S)
#print(y_S)
A=x_S
B=y_S
num=0
                            ##### FUNCS #####
def move_to_empty_path(a,b):
    global A
    global B
    global num
    num=0

        #up
    if maze1[a-1][b]==" ":
        num+=1

        #down
    if maze1[a+1][b]==" ":
        num+=1

        #right
    if maze1[a][b+1]==" ":
        num+=1

        #left
    if maze1[a][b-1]==" ":
        num+=1

    if num==1:
        if maze1[a-1][b]==" ":
            maze1[a-1][b]='+'
            A-=1
            B==b

            #down
        elif maze1[a+1][b]==" ":
            maze1[a+1][b]="+"
            A+=1
            B==b

            #right
        elif maze1[a][b+1]==" ":
            maze1[a][b+1]="+"
            A==a
            B+=1

            #left
        elif maze1[a][b-1]==" ":
            maze1[a][b-1]="+"
            A==a
            B-=1
    elif num==2:
            #up
        if maze1[a-1][b]==" ":
            maze1[a-1][b]='+'


            #down
        elif maze1[a+1][b]==" ":
            maze1[a+1][b]="+"


            #right
        elif maze1[a][b+1]==" ":
            maze1[a][b+1]="+"


            #left
        elif maze1[a][b-1]==" ":
            maze1[a][b-1]="+"


    for i in range(7):
        print(" ".join(maze1[i]))







#############print-func##################

def print_maze():
    for i in range(7):
        print(" ".join(maze1[i]))




                          ##### END-FUNCS #####

for z in range(16):
    move_to_empty_path(A,B)
    print('')






