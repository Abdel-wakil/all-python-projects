maze1 = [["#", "#", "#", "#", "#", "#", "#","#","#"],
         ["#", " ", " ", " ", " ", " ", " "," ","#"],
         ["#", "#", " ", "#", "#", " ", "#"," ","#"],
         ["#", "#", " ", "#", "#", " ", "#"," ","#"],
         ["#", "#", " ", "#", "#", " ", "#","S"," "],
         ["#", "#", " ", "#", "#", " ", "#","#","#"],
         ["#", "#", " ", "#", " ", " ", " "," ","#"],
         ["#", " ", " ", "#", " ", "#", "#"," ","#"],
         ["#", "#", " ", "#", "#", "#", "#","#","#"],
         ["#", "#", "F", "#", "#", "#", "#","#","#"],

for x_S in range(7):
    if "S" in maze1[x_S]:
        y_S=maze1[x_S].index('S')
        break

A=x_S
B=y_S

# s=100


################### FUNCTIONS-DEPARTEMENT ###################
                            ##1##
def how_many_ways(a,b):
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

    if num==2:
        print('two ways ha')
                            ##2##
def move_to_single_path(a,b):
    global A,B
    if num==1:
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


                            ##3##
def display_cool_maze(m):
    print()
    for i in range(7):
        print(" ".join(m[i]))
    print()
                            ##4##
def check_if_Im_out(a,b):
    surr=[]

    surr+=[maze1[a-1][b],maze1[a+1][b],maze1[a][b+1],maze1[a][b-1]]
    if 'F' in surr:
        print('im out')
    print(surr)
###############################################################







display_cool_maze(maze1)
for i in range(5):
    check_if_Im_out(A,B)
    how_many_ways(A,B)
    move_to_single_path(A,B)


display_cool_maze(maze1)
