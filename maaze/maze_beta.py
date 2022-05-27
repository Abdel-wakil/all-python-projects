maze1 = [["#", "#", "#", "#", "#", "#", "#"],
         ["#", " ", " ", " ", "#", "S", "#"],
         ["#", " ", "#", " ", "#", " ", "#"],
         ["#", " ", "#", " ", " ", " ", "#"],
         ["#", " ", "#", "#", "#", " ", "#"],
         ["#", " ", " ", " ", "#", " ", "#"],
         ["#", "#", "#", "F", "#", "#", "#"]]


for x_S in range(7):
    if "S" in maze1[x_S]:
        y_S=maze1[x_S].index('S')
        break

#print(x_S)
#print(y_S)
A=x_S
B=y_S

                            ##### FUNC #####
def move_to_empty_path(a,b):
    global A
    global B

        #up
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




                          ##### END-FUNC #####

for z in range(3):
    move_to_empty_path(A,B)


for i in range(7):
    print(" ".join(maze1[i]))

































