import tictactoe.tools as tools
import tictactoe.QAgent as QA
import numpy as np
from tqdm import tqdm as tqdm
if __name__ == "__main__":
    game = tools.init()
    statespace = tools.make_gamestate(game).reshape([3, 3])
    agent = QA.QAgent(lr=5e-3, epsilon=1., eps_dec=5e-6, eps_min=4e-2, gamma=.99,
                      statespace=statespace, actionspace=9, chkpt_dir="tmp/model",
                      memorysize=250000, batchsize=32, rplcinterv=500)
    scores = []

    for n_games in tqdm(range(250000)):
        meansize = 1000
        score = 0
        win = False
        game = tools.init()
        state_ = tools.make_gamestate(game)
        if n_games % meansize == 0:
            agent.save_models()
            mean = np.mean(scores[n_games-meansize:n_games]) if scores != [] else "nan"
            maximum = max(scores[n_games-meansize:n_games]) if scores != [] else "nan"

            print("Mean score:", mean, "\n", "Max score:", maximum, "\n", "epsilon:", agent.epsilon)
        for i in range(9):

            pid = 0 if i % 2 == 0 else 1
            #print("Player: ", pid+1)
            posmov = tools.getPosMovs(game_grid=game)
            state = tools.make_gamestate(game_grid=game)

            if pid == 0:
                #print("Possible moves:", posmov)
                #tools.drawGrid(game)
                #game = tools.move(mov=int(input()),
                #                emptyspaces=posmov, game_grid=game, pid=pid)
                game = tools.move(mov=tools.naive_bot(posmov),
                                  emptyspaces=posmov, game_grid=game, pid=pid)
            else:
                #print("Possible moves:", posmov)
                move = agent.choose_action(obs=state, posmovs=posmov)
                if move not in posmov:
                    score -= 100
                game = tools.move(mov=move,
                                  emptyspaces=posmov, game_grid=game, pid=pid)
                if move not in posmov:
                    break
                score += tools.give_reward(i=i)
                game = tools.move(mov=move,
                                  emptyspaces=posmov, game_grid=game, pid=pid)
                agent.store_transition(state, move,
                                       score, state_, int(win))

                agent.learn()
            #tools.drawGrid(game_grid=game)
            win = tools.checkWinLoss(game)
            if win:
                if pid == 2:
                    score+=25
                    agent.store_transition(state, move,
                                           score, state_, int(win))
                #tools.drawGrid(game)
                #print("Player: ", pid + 1, "won")
                break
            state_ = state
            #End of for
        scores.append(score)
        #print("GAME ENDED")
    #End of for


