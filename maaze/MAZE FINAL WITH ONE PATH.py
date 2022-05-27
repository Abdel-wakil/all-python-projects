maze1 =[["#", "#", "#", "#", "#", "#", "#","#","#"],
        ["#", " ", " ", " ", " ", " ", " "," ","#"],
        ["#", "#", " ", "#", "#", " ", "#"," ","#"],
        ["#", "#", " ", " ", "#", " ", "#"," ","#"],
        ["#", "#", "#", " ", "#", " ", "#","S","#"],
        ["#", "#", " ", " ", "#", " ", "#","#","#"],
        ["#", "#", " ", "#", " ", " ", " "," ","#"],
        ["#", " ", " ", "#", " ", "#", "#"," ","#"],
        ["#", "#", " ", "#", "#", "#", "#","#","#"],
        ["#", "#", "F", "#", "#", "#", "#","#","#"]]


checkpoint_A=[]
checkpoint_B=[]
history = []

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
    global A,B, history

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



    history = history + [ [A,B] ]




                            ##3##
def display_cool_maze(m):
    print()
    n_rows = len(m) # how many rows in the maze
    for i in range(n_rows):
        print(" ".join(m[i]))
    print()
    print("History -->", history)

                            ##4##
def check_if_Im_out(a,b):
    """ [ Up, Down, Right, Left ] """
    out = False
    surr = [maze1[a-1][b], maze1[a+1][b], maze1[a][b+1], maze1[a][b-1]]
    if 'F' in surr:
        out = True
        print('out ==>', out)

    print("  ",surr)
    return(out)
                            ##5##
def check_point(a,b):
    global checkpoint_A,checkpoint_B

    if how_many_ways(A,B)==2:
        checkpoint_A+=[A]
        checkpoint_B+=[B]
    print(checkpoint_A)
    print(checkpoint_B)
                            ##6##

def finding_final_path():
    global history

    if how_many_ways(A,B)==0:
        if check_if_Im_out(A,B)==False:
            x_checkpoint=checkpoint_A[-1]
            y_checkpoint=checkpoint_B[-1]

            index_check=history.index([x_checkpoint,y_checkpoint])

            history=history[:index_check]
                            ##7##

def clear_maze(maze):
    for x in maze:
        while "+" in x:
            x[x.index("+")]=" "

                            ##8##

def draw_the_final_path(maze):
    for i in history:
        maze[i[0]][i[1]]="+"


###############################################################





for x_S in range(7):
    if "S" in maze1[x_S]:
        y_S=maze1[x_S].index('S')
        break

A=x_S
B=y_S
# (A,B) Current position of the algorithm during maze exploration

display_cool_maze(maze1)
for i in range(50):

    display_cool_maze(maze1)


    number_of_ways = how_many_ways(A,B)
    print("How many ways ? ===>", number_of_ways)

    IamOut = check_if_Im_out(A,B)
    if IamOut == True:
        break

    check_point(A,B)


    move_to_single_path(A,B)

    finding_final_path()


clear_maze(maze1)

draw_the_final_path(maze1)

display_cool_maze(maze1)




