maze1 =[["#", "#", "#", "#", "#", "#", "#","#","#"],
        ["#", " ", " ", " ", " ", " ", " "," ","#"],
        ["#", "#", " ", "#", "#", " ", "#"," ","#"],
        ["#", "#", " ", " ", "#", " ", "#"," ","#"],
        ["#", "#", "#", " ", "#", " ", "#","S","#"],
        ["#", "#", " ", " ", "#", " ", "#","#","#"],
        ["#", "#", " ", "#", "#", " ", " "," ","#"],
        ["#", " ", " ", "#", " ", "#", "#"," ","#"],
        ["#", "#", " ", "#", "#", "#", "#","#","#"],
        ["#", "#", "F", "#", "#", "#", "#","#","#"]]




solution = [[3, 7], [2, 7], [1, 7], [1, 6], [1, 5], [1, 4], [1, 3], [1, 2], [2, 2], [3, 2], [3, 3], [4, 3], [5, 3], [5, 2], [6, 2], [7, 2], [8, 2]]

for i in solution:
    maze1[i[0]][i[1]]="+"

def display_cool_maze(m):
    print()
    n_rows = len(m) # how many rows in the maze
    for i in range(n_rows):
        print(" ".join(m[i]))
    print()

display_cool_maze(maze1)