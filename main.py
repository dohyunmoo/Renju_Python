import pygame
import objects as obj

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BEIGE = (225, 198, 153)

# size of each cells and margin
WIDTH, HEIGHT, MARGIN = 30, 30, 2

# no. of rows and columns
ROW, COLUMN = 15, 15

# 15x15 grid
grid = []
for row in range(ROW):
    grid.append([])
    for column in range(COLUMN):
        grid[row].append(0)

count = 1

pygame.init()
 
WINDOW = [(WIDTH + MARGIN)*ROW + MARGIN, (HEIGHT + MARGIN)*COLUMN + MARGIN]
screen = pygame.display.set_mode(WINDOW)
 
pygame.display.set_caption("Renju")

run = True
 
clock = pygame.time.Clock()

# main
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            if grid[row][column] == 0:
                grid[row][column] = count
                count += 1

    screen.fill(BLACK)

    for row in range(ROW):
        for column in range(COLUMN):
            color = BEIGE
            if ~obj.numberType(grid[row][column]):
                color = BLACK
            elif (obj.numberType(grid[row][column])) and (grid[row][column] != 0):
                color = WHITE
            pygame.draw.rect(screen,color,[(MARGIN + WIDTH) * column + MARGIN,(MARGIN + HEIGHT) * row + MARGIN,WIDTH,HEIGHT])

            # win types
            while grid[row][column] != 0:
                while row+4 <= ROW-1 and column+4 <= COLUMN-1:
                    # horizontal win
                    if obj.numberType(grid[row][column]) == obj.numberType(grid[row][column+1]) == obj.numberType(grid[row][column+2]) == obj.numberType(grid[row][column+3]) == obj.numberType(grid[row][column+4]):
                        obj.winType(grid[row][column])
                    # vertical win
                    elif obj.numberType(grid[row][column]) == obj.numberType(grid[row+1][column]) == obj.numberType(grid[row+2][column]) == obj.numberType(grid[row+3][column]) == obj.numberType(grid[row+4][column]):
                        obj.winType(grid[row][column])
                    # diagonal win
                    elif obj.numberType(grid[row][column]) == obj.numberType(grid[row+1][column+1]) == obj.numberType(grid[row+2][column+2]) == obj.numberType(grid[row+3][column+3]) == obj.numberType(grid[row+4][column+4]):
                        obj.winType(grid[row][column])

    clock.tick(20)

    pygame.display.update()

pygame.quit()

print(grid)
