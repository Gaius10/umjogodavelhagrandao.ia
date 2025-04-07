'''
Gera um heatmap indicando, para cada casa, o percentual de partidas ganhas em que ela foi preenchida.
'''

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from lib.runner import run
from lib.agents import RandomAgent

def accumulate_heatmap_info(game, victory_counts):
    if (victory_counts is None):
        return np.zeros((9, 9), dtype=int)

    winner = game.getWinner()

    if winner != 0:
        history = game.getHistory()
        player = 1
        for (r, c) in history:
            if player == winner:
                victory_counts[r][c] += 1
            player *= -1

    return victory_counts

N = 1000
player1 = RandomAgent()
player2 = RandomAgent()

victory_counts = run(player1, player2, accumulate_heatmap_info, N)
victory_ratio = (victory_counts / N) * 100

print(victory_ratio)

sns.heatmap(
    victory_ratio,
    annot=True,
    fmt=".2f",
    annot_kws={"size": 8},
    cmap="YlGnBu",
    cbar_kws={'label': 'Proporção de vitórias'},
    square=True,
    linewidths=0.5,
    linecolor='gray'
)

plt.title("Heatmap das Casas Ocupadas pelo Jogador Vencedor")
plt.xlabel("Colunas (0 a 8)")
plt.ylabel("Linhas (0 a 8)")
plt.tight_layout()
plt.show()
