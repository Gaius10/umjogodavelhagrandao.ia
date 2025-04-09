
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

Entre 2 players do tipo "Minimax" (AlphaBetaAgent vs AlphaBetaAgent, ambos com depth=2), a vantagem do primeiro jogador ainda existe, mas é menor:
    O jogador 1 ganhou 359 partidas (35.90%).
    O jogador 2 ganhou 283 partidas (28.30%).
    Empates: 358 (35.80%)
    Total de partidas: 1000.

    O jogador 1 ganhou 321 partidas (32.10%).
    O jogador 2 ganhou 341 partidas (34.10%).
    Empates: 338 (33.80%)
    Total de partidas: 1000.

    O jogador 1 ganhou 355 partidas (35.50%).
    O jogador 2 ganhou 290 partidas (29.00%).
    Empates: 355 (35.50%)
    Total de partidas: 1000.

    O jogador 1 ganhou 348 partidas (34.80%).
    O jogador 2 ganhou 315 partidas (31.50%).
    Empates: 337 (33.70%)
    Total de partidas: 1000.

    ---

    Medias:

    O jogador 1 ganhou 345.75 partidas (34.58%).
    O jogador 2 ganhou 307.25 partidas (30.73%).
    Empates: 347.00 (34.7%)
    Total de partidas: 4000.

Entre 2 players do tipo MCTS
    O jogador 1 ganhou 45 partidas (45.45%).
    O jogador 2 ganhou 47 partidas (47.47%).
    Empates: 7 (7.07%)
    Total de partidas: 99.

'''

import numpy as np
from lib.runner import run
from lib.agents.random import RandomAgent
from lib.agents.minimax import AlphaBetaAgent
from lib.agents.mcts import MCTSAgent

def accumulate_heatmap_info(game, scoreboard):
    if scoreboard is None:
        return {
            "player1": 0,
            "player2": 0,
            "total": 1,
        }

    winner = game.getWinner()
    if winner == 1:
        scoreboard["player1"] += 1
    elif winner == -1:
        scoreboard["player2"] += 1
    scoreboard["total"] += 1

    return scoreboard

N = 10**3
player1 = AlphaBetaAgent(depth=2)
player2 = AlphaBetaAgent(depth=2)

scoreboard = run(player1, player2, accumulate_heatmap_info, N)

print(f"O jogador 1 ganhou {scoreboard['player1']} partidas ({(scoreboard['player1']/scoreboard['total'])*100:.2f}%).")
print(f"O jogador 2 ganhou {scoreboard['player2']} partidas ({(scoreboard['player2']/scoreboard['total'])*100:.2f}%).")
print(f"Empates: {scoreboard['total'] - scoreboard['player1'] - scoreboard['player2']} ({((scoreboard['total'] - scoreboard['player1'] - scoreboard['player2'])/scoreboard['total'])*100:.2f}%)")
print(f"Total de partidas: {scoreboard['total']}.")
