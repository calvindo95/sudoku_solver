grid = [[0, 0, 0, 8, 1, 6, 0, 0, 0],
        [0, 0, 6, 5, 0, 0, 0, 9, 0],
        [3, 7, 0, 9, 0, 0, 6, 0, 1],
        [7, 8, 0, 3, 0, 0, 2, 0, 0],
        [9, 0, 2, 0, 6, 0, 1, 0, 7],
        [0, 0, 3, 0, 0, 2, 0, 4, 5],
        [8, 0, 1, 0, 0, 5, 0, 7, 6],
        [0, 3, 0, 0, 0, 9, 5, 0, 0],
        [0, 0, 0, 6, 8, 7, 0, 0, 0]]

def printGrid(gr):
    for i in range(len(gr)):
        for j in range(len(gr[i])):
            print(f'{gr[i][j]}',end='  ')
            if (j+1) % 3 == 0:
                if (j+1) == 9:
                    pass
                else:
                    print('|', end='  ')
        print('')
        if (i+1) % 3 == 0:
            if (i+1) == 9:
                pass
            else:
                print('-------------------------------')
    print('')

def findEmpty(gr):
    for i in range(len(gr)):
        for j in range(len(gr[i])):
            if gr[i][j] == 0:
                return (i,j) # returns row, column
    return None

def solveGrid(gr):
    pos = findEmpty(gr)
    if not pos:
        return True
    else:
        row, col = pos

    # iterates through the 9 possible numbers
    for i in range(1,10):
        if check(gr, i, (row,col)):
            gr[row][col] = i

            if solveGrid(gr):
                return True
            
            gr[row][col] = 0
    return False

def check(gr, num, pos):
    # check row
    for i in range(len(gr[0])):
        if gr[pos[0]][i] == num and pos[1] != i:
            return False
    
    # check column
    for i in range(len(gr)):
        if gr[i][pos[1]] == num and pos[0] != i:
            return False

    # check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3+3):
        for j in range(box_x*3, box_x*3+3):
            if gr[i][j] == num and (i,j) != pos:
                return False
    return True

printGrid(grid)
solveGrid(grid)
print('######### Solved Puzzle ######### \n' )
printGrid(grid)