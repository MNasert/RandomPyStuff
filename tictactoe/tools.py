import random
import numpy as np

def init():
    blocks = [i for i in range(9)]
    game_grid = []
    for i in range(len(blocks)):
        game_grid.append("*")
    return game_grid


def drawGrid(game_grid):
    print(game_grid[0], "", game_grid[1], "", game_grid[2])
    print(game_grid[3], "", game_grid[4], "", game_grid[5])
    print(game_grid[6], "", game_grid[7], "", game_grid[8])


def getPosMovs(game_grid):
    emptyspaces = []
    for i in range(len(game_grid)):
        if game_grid[i] == "*":
            emptyspaces.append(i+1)
    return emptyspaces

def move(mov, emptyspaces, game_grid, pid):
    try:
        if mov in emptyspaces:
            game_grid[mov-1] = "X" if pid == 0 else "O"
        else:
            raise ValueError
    except:
        if pid == 0:
            print("Not a valid move.")
            emptyspaces = getPosMovs(game_grid=game_grid)
            print("Valid moves are:", emptyspaces)
            mov = int(input("Your move?:"))
            game_grid = move(mov=mov, game_grid=game_grid, emptyspaces=emptyspaces, pid=pid)
        else:
            return None
    return game_grid

def checkWinLoss(game_grid):
    vals = game_grid
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

def make_gamestate(game_grid):
    gamestate = []
    for i in range(len(game_grid)):
        if game_grid[i] == "X":
            gamestate.append(-1)
        elif game_grid[i] == "O":
            gamestate.append(0)
        else:
            gamestate.append(1)
    gamestate = np.array(gamestate)
    gamestate = gamestate.reshape([3, 3])
    return gamestate

def give_reward(i):
    return 4-i

def naive_bot(posmov):
    return np.random.choice(posmov)












#








