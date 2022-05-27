maze = [["#", "#", "#", "#"],
        ["#", "+", "+", "#"],
        ["#", "#", "+", "#"],
        ["#", "#", "+", "#"],]


################################################################
def display_cool_maze(m):
    print()
    n_rows = len(m) # how many rows in the maze
    for i in range(n_rows):
        print(" ".join(m[i]))
    print()
################################################################

display_cool_maze(maze)

for x in maze:
    while "+" in x:
        x[x.index("+")]=" "


display_cool_maze(maze)


























