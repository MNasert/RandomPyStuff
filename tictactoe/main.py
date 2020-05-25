import tictactoe.tools as tools

if __name__ == "__main__":
    game = tools.init()
    win = False
    for i in range(9):
        pid = 0 if i % 2 == 0 else 1
        print("Player: ", pid+1)
        tools.drawGrid(game_grid=game)
        game = tools.move(game_grid=game, pid=pid)
        win = tools.checkWinLoss(game)
        if win:
            tools.drawGrid(game)
            print("Player: ", pid + 1, "won")
            break
    print("GAME ENDED")

