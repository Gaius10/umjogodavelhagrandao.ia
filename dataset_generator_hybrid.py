'''
Gera datasets para analise posterior
'''

from lib.agents.hybrid import HybridAgent
from lib.runner import run
import json

player1 = HybridAgent()
player2 = HybridAgent()
n = 10**3

file = open(f'hybrid1_{n}.csv', 'w')
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
