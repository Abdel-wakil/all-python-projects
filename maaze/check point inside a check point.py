maze1 = [["#", "#", "#", "#", "#", "#", "#","#","#"],
        ["#", " ", " ", " ", " ", " ", " "," ","#"],
        ["#", "#", " ", "#", "#", " ", "#"," ","#"],
        ["#", "#", " ", " ", "#", " ", "#","S","#"],
        ["#", "#", "#", " ", "#", " ", "#","#","#"],
        ["#", "#", " ", " ", "#", " ", "#","#","#"],
        ["#", "#", " ", "#", " ", " ", " "," ","#"],
        ["#", " ", " ", "#", " ", "#", "#"," ","#"],
        ["#", "#", " ", "#", "#", "#", "#","#","#"],
        ["#", "#", "F", "#", "#", "#", "#","#","#"]]


checkpoint_A=[]
checkpoint_B=[]

################### FUNCTIONS-DEPARTEMENT ###################
                            ##1##
def how_many_ways(a,b):
    #global num
    num=0 # if it stays at zero ==> you're stuck
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


    return num
                            ##2##
def move_to_single_path(a,b):
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
    else:
        A=checkpoint_A[-1]
        B=checkpoint_B[-1]
        checkpoint_A.pop(-1)
        checkpoint_B.pop(-1)


                            ##3##
def display_cool_maze(m):
    print()
    n_rows = len(m) # how many rows in the maze
    for i in range(n_rows):
        print(" ".join(m[i]))
    print()
                            ##4##
def check_if_Im_out(a,b):
    """ [ Up, Down, Right, Left ] """
    out = False
    surr = [maze1[a-1][b], maze1[a+1][b], maze1[a][b+1], maze1[a][b-1]]
    if 'F' in surr:
        out = True
        print('out ==>', out)

    print(surr)
    return(out)
                            ##5##
def check_point(a,b):
    global checkpoint_A,checkpoint_B

    if how_many_ways(A,B)==2:
        checkpoint_A+=[A]
        checkpoint_B+=[B]
    print(checkpoint_A)
    print(checkpoint_B)

###############################################################





for x_S in range(7):
    if "S" in maze1[x_S]:
        y_S=maze1[x_S].index('S')
        break

A=x_S
B=y_S


display_cool_maze(maze1)
for i in range(50):

    IamOut = check_if_Im_out(A,B)
    if IamOut == True:
        break

    number_of_ways = how_many_ways(A,B)
    print("How many ways ? ===>", number_of_ways)

    check_point(A,B)


    move_to_single_path(A,B)


    display_cool_maze(maze1)
















