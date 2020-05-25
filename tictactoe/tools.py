def init():
    blocks = [i for i in range(9)]
    game_grid = {}
    for i in range(len(blocks)):
        game_grid[blocks[i]] = "*"
    return game_grid

def drawGrid(game_grid):
    print(game_grid[0], "", game_grid[1], "", game_grid[2])
    print(game_grid[3], "", game_grid[4], "", game_grid[5])
    print(game_grid[6], "", game_grid[7], "", game_grid[8])

def move(game_grid, pid):
    try:
        posmov = []
        for i in game_grid:
            if game_grid[i] == "*":
                posmov.append(i+1)
        mov = int(input("Possible Moves: " + str(posmov) + "\n"))
        if mov not in posmov:
            raise Exception
        if pid == 0:
            game_grid[int(mov)-1] = "X"
        else:
            game_grid[int(mov) - 1] = "O"
    except:
        print("Hey stay inside the grid! And don´t cheat!")
        game_grid = move(game_grid, pid)
        drawGrid(game_grid)
    return game_grid

def checkWinLoss(game_grid):
    vals = list(game_grid.values())
    r1 = vals[0:3]
    r2 = vals[3:6]
    r3 = vals[6:9]
    r4 = [vals[0], vals[4], vals[8]]
    r5 = [vals[2], vals[4], vals[6]]
    r6 = [r1[0], r2[0], r3[0]]
    r7 = [r1[1], r2[1], r3[1]]
    r8 = [r1[2], r2[2], r3[2]]
    if checkRow(r1) or checkRow(r2) or checkRow(r3) \
       or checkRow(r4) or checkRow(r5) or checkRow(r6) or checkRow(r7) or checkRow(r8):
        return True
    else:
        return False

def checkRow(row):
    if "*" not in row[0:3]:
        if row[0] == row[1] and row[0] == row[2]:
            return True

