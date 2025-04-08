
'''
# O jogo é justo?

Analisa proporção de vitórias entre o primeiro e o segundo jogador.

Entre 2 players do tipo randômico (RandomAgent vs RandomAgent), o experimento sugere que o primeiro jogador tem uma leve vantagem:
    O jogador 1 ganhou 4376 partidas (43.76%).
    O jogador 2 ganhou 3634 partidas (36.34%).
    Empates: 1990 (19.90%)
    Total de partidas: 10000.

Entre 2 players do tipo "Minimax" (AlphaBetaAgent vs AlphaBetaAgent, ambos com depth=1), a vantagem do primeiro jogador ainda existe, mas é menor:
    O jogador 1 ganhou 336 partidas (33.60%).
    O jogador 2 ganhou 319 partidas (31.90%).
    Empates: 345 (34.50%)
    Total de partidas: 1000.

'''

import numpy as np
from lib.runner import run
from lib.agents import RandomAgent, AlphaBetaAgent, MCTSagent

def accumulate_heatmap_info(game, scoreboard):
    if scoreboard is None:
        return {
            "player1": 0,
            "player2": 0,
            "total": 0,
        }

    winner = game.getWinner()
    if winner == 1:
        scoreboard["player1"] += 1
    elif winner == -1:
        scoreboard["player2"] += 1
    scoreboard["total"] += 1

    return scoreboard

N = 10**3
player1 = AlphaBetaAgent(depth=1)
player2 = AlphaBetaAgent(depth=1)

scoreboard = run(player1, player2, accumulate_heatmap_info, N)

print(f"O jogador 1 ganhou {scoreboard['player1']} partidas ({(scoreboard['player1']/scoreboard['total'])*100:.2f}%).")
print(f"O jogador 2 ganhou {scoreboard['player2']} partidas ({(scoreboard['player2']/scoreboard['total'])*100:.2f}%).")
print(f"Empates: {scoreboard['total'] - scoreboard['player1'] - scoreboard['player2']} ({((scoreboard['total'] - scoreboard['player1'] - scoreboard['player2'])/scoreboard['total'])*100:.2f}%)")
print(f"Total de partidas: {scoreboard['total']}.")
