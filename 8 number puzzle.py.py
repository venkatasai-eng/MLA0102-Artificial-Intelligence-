puzzle = [
    [1, 2, 3],
    [4, 0, 5],
    [6, 7, 8]
]

def show(p):
    for row in p:
        print(row)
    print()

def move(p, direction):
    for i in range(3):
        for j in range(3):
            if p[i][j] == 0:   # find empty space
                x, y = i, j
    if direction == 'up' and x > 0:
        p[x][y], p[x-1][y] = p[x-1][y], p[x][y]
    elif direction == 'down' and x < 2:
        p[x][y], p[x+1][y] = p[x+1][y], p[x][y]
    elif direction == 'left' and y > 0:
        p[x][y], p[x][y-1] = p[x][y-1], p[x][y]
    elif direction == 'right' and y < 2:
        p[x][y], p[x][y+1] = p[x][y+1], p[x][y]
    else:
        print("Invalid move!")
    show(p)

# Example run
print("Initial Puzzle:")
show(puzzle)

move(puzzle, 'right')
move(puzzle, 'down')
