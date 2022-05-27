maze1 = [["#", "#", "#", "#", "#", "#", "#"],
         ["#", " ", " ", " ", " ", " ", "#"],
         ["#", " ", "#", " ", "#", " ", "#"],
         ["#", " ", "#", " ", "#", "S", "#"],
         ["#", " ", "#", " ", "#", "#", "#"],
         ["#", " ", " ", " ", "#", " ", "#"],
         ["#", "#", "#", "F", "#", "#", "#"]]

for x_S in range(7):
    if "S" in maze1[x_S]:
        y_S=maze1[x_S].index('S')
        break

A=x_S
B=y_S

# s=100


################### FUNCTIONS-DEPARTEMENT ###################
                            ##1##
def move_to_empty_path(a,b):
    global A,B

        #up
    if maze1[a-1][b]==" ":
        maze1[a-1][b]='+'
        A=a-1
        B=b


        #down
    elif maze1[a+1][b]==" ":
        maze1[a+1][b]="+"
        A=a+1
        B=b

        #right
    elif maze1[a][b+1]==" ":
        maze1[a][b+1]="+"
        A=a
        B=b+1

        #left
    elif maze1[a][b-1]==" ":
        maze1[a][b-1]="+"
        A=a
        B=b-1
                            ##2##
def display_cool_maze(m):
    print()
    for i in range(7):
        print(" ".join(m[i]))
    print()
                            ##3##
def check_if_Im_out(a,b):
    surr=[]

    surr+=[maze1[a-1][b],maze1[a+1][b],maze1[a][b+1],maze1[a][b-1]]
    if 'F' in surr:
        print('im out')
    print(surr)
################################################################








display_cool_maze(maze1)
for i in range(4):
    #check_if_Im_out(A,B)
    move_to_empty_path(A,B)


display_cool_maze(maze1)






