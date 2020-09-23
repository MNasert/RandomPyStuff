import tictactoe.tools as tools
import tictactoe.QAgent as QA
import numpy as np
import time as time
from tqdm import tqdm as tqdm
if __name__ == "__main__":
    game = tools.init()
    statespace = tools.make_gamestate(game, 0).reshape([3, 3])
    agentP1 = QA.QAgent(lr=5e-3, epsilon=1., eps_dec=2e-5, eps_min=4e-2, gamma=.99,
                        statespace=statespace, actionspace=9, chkpt_dir="ModelP1/dqnttt",
                        memorysize=150000, batchsize=64, rplcinterv=100)

    agentP2 = QA.QAgent(lr=5e-3, epsilon=1., eps_dec=1e-5, eps_min=4e-2, gamma=.99,
                        statespace=statespace, actionspace=9, chkpt_dir="ModelP2/dqnttt",
                        memorysize=150000, batchsize=64, rplcinterv=100)
    player = 0
    vis = 0
    load = 1
    messesP1 = 0
    messesP2 = 0
    scoresP1 = []
    scoresP2 = []
    try:
        if load:
            agentP1.load_models()
            agentP2.load_models()
    except:
        None
    for n_games in tqdm(range(45000)):
        meansize = 750
        scoreP1, scoreP2 = 0, 0
        win = False
        game = tools.init()
        state_ = tools.make_gamestate(game_grid=game, pid=0)
        if n_games % meansize == 0:
            agentP1.save_models()
            agentP2.save_models()

            meanP1 = np.mean(scoresP1[n_games-meansize:n_games]) if scoresP1 != [] else "nan"
            maximumP1 = max(scoresP1[n_games-meansize:n_games]) if scoresP1 != [] else "nan"
            meanP2 = np.mean(scoresP2[n_games - meansize:n_games]) if scoresP1 != [] else "nan"
            maximumP2 = max(scoresP2[n_games - meansize:n_games]) if scoresP1 != [] else "nan"

            print("Mean score for P1:", meanP1, "\n", "Max score of P1:",
                  maximumP1, "\n", "epsilon:", agentP1.epsilon, "messes P1:", messesP1)
            print("Mean score for P2:", meanP2, "\n", "Max score of P2:",
                  maximumP2, "\n", "epsilon:", agentP2.epsilon, "Messes P2:", messesP2)
            messesP1 = 0
            messesP2 = 0

        for i in range(9):
            pid = 0 if i % 2 == 0 else 1
            posmov = tools.getPosMovs(game_grid=game)
            state = tools.make_gamestate(game_grid=game, pid=pid)

            if pid == 0:
                if player != 1:
                    moveP1 = agentP1.choose_action(obs=state, posmovs=posmov)
                    if moveP1 not in posmov:
                        scoreP1 -= 100
                        messesP1 += 1
                    agentP1.store_transition(state, moveP1,
                                             scoreP1, state_, int(win))
                    if moveP1 not in posmov:
                        break
                    game = tools.move(mov=moveP1,
                                      emptyspaces=posmov, game_grid=game, pid=pid)
                    scoreP1 += tools.give_reward(i=i)


                    agentP1.learn()
                else:
                    tools.drawGrid(game_grid=game)
                    print(posmov)
                    game = tools.move(mov=int(input()),
                                      emptyspaces=posmov, game_grid=game, pid=pid)

            else:
                if player != 2:
                    moveP2 = agentP2.choose_action(obs=state*-1, posmovs=posmov)
                    if moveP2 not in posmov:
                        scoreP2 -= 100
                        messesP2 += 1
                    agentP2.store_transition(state*-1, moveP2,
                                             scoreP2, state_*-1, int(win))

                    if moveP2 not in posmov:
                        break
                    scoreP2 += tools.give_reward(i=i)
                    game = tools.move(mov=moveP2,
                                      emptyspaces=posmov, game_grid=game, pid=pid)
                    agentP2.learn()
                else:
                    tools.drawGrid(game_grid=game)
                    print(posmov)
                    game = tools.move(mov=int(input()),
                                      emptyspaces=posmov, game_grid=game, pid=pid)

            #################
            win = tools.checkWinLoss(game)
            if win:
                if pid == 2:
                    scoreP1 -= 10
                    scoreP2 += 20
                    if player != 2:
                        agentP2.store_transition(state*-1, moveP2,
                                                 scoreP2, state_*-1, int(win))
                    if player != 1:
                        agentP1.store_transition(state, moveP1,
                                                 scoreP1, state_, int(win))
                else:
                    scoreP1 += 20
                    scoreP2 -= 10
                    if player != 2:
                        agentP1.store_transition(state * -1, moveP2,
                                                 scoreP2, state_ * -1, int(win))
                    if player != 1:
                        agentP2.store_transition(state, moveP1,
                                                 scoreP1, state_, int(win))
                if vis == 1:
                    print("Game: ", n_games, "winner: ", pid+1)
                    tools.drawGrid(game_grid=game)
                    time.sleep(5)
                break

            state_ = state
            #End of for
        scoresP1.append(scoreP1)
        scoresP2.append(scoreP2)
        #print("GAME ENDED")
    #End of for


