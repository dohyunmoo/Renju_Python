ROW, COLUMN = 9, 9

grid = []
for row in range(ROW+1):
    grid.append([])
    for column in range(COLUMN+1):
        grid[row].append('-')

finished = False
count = 1
turn = "Black"
piece = "B"

numType = lambda x: x%2

while not finished:
    for row in range(ROW+1):
        grid[row][0] = str(row)

    for column in range(COLUMN+1):
        grid[0][column] = str(column)

    for row in range(ROW+1):
        print(grid[row])

    if numType(count):
        turn = "Black"
        piece = "B"
    else:
        turn = "White"
        piece = "W"

    x = int(input(f"It is {turn}'s turn. Please input row number then press Enter: "))
    y = int(input(f"It is {turn}'s turn. Please input column number then press Enter: "))

    print(x, y)

    while (0 >= x) or (x > ROW) or (0 >= y) or (y > COLUMN):
        x = int(input(f"Error: input value out of the range. It is {turn}'s turn. Please re-input row number then press Enter: "))
        y = int(input(f"Error: input value out of the range. It is {turn}'s turn. Please re-input column number then press Enter: "))
    
    while grid[x][y] != '-':
        x = int(input(f"Error: cell occupied. It is {turn}'s turn. Please re-input row number then press Enter: "))
        y = int(input(f"Error: cell occupied. It is {turn}'s turn. Please re-input column number then press Enter: "))

    grid[x][y] = piece

    for row in range(1, ROW+1):
        for column in range(1, COLUMN+1):
            while column+4 <= COLUMN:
                if grid[row][column] == grid[row][column+1] == grid[row][column+2] == grid[row][column+3] == grid[row][column+4] != '-':
                    print(f"{turn} wins!")
                    finished = True

            while row+4 <= ROW:
                if grid[row][column] == grid[row+1][column] == grid[row+2][column] == grid[row+3][column] == grid[row+4][column] != '-':
                    print(f"{turn} wins!")
                    finished = True
            
            while row+4 <= ROW and column+4 <= COLUMN:
                if grid[row][column] == grid[row+1][column+1] == grid[row+2][column+2] == grid[row+3][column+3] == grid[row+4][column+4] != '-':
                    print(f"{turn} wins!")
                    finished = True
    
    count += 1
