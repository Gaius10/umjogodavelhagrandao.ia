'''
Gera datasets para analise posterior
'''

from lib.agents.random import RandomAgent
from lib.runner import run
import json

player1 = RandomAgent()
player2 = RandomAgent()
n = 10**5

file = open(f'random2_{n}.csv', 'w')
file.write('"history","num_moves","winner","final_board","final_mini_wins"\n')
def accumulate(game, info):
    global file
    line = [
        json.dumps(game.getHistory()),
        game.getNumMoves(),
        game.getWinner(),
        json.dumps(game.getBoard().tolist()),
        json.dumps(game.getMiniWins().tolist()),
    ]
    file.write('"{}","{}","{}","{}","{}"\n'.format(*line))

run(player1, player2, accumulate, n)

print(f"Total games played: {n}")
file.close()
