from lib.agents.random import RandomAgent
from lib.runner import run
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

player1 = RandomAgent()
player2 = RandomAgent()

def accumulate_heatmap_info(game, victory_counts):
    if victory_counts is None:
        return np.zeros((3, 3), dtype=int)

    winner = game.getWinner()

    if winner != 0:
        mini_wins = game.getMiniWins()
        victory_counts += (mini_wins == winner).astype(int)

    return victory_counts

N = 10**5
victory_counts = run(player1, player2, accumulate_heatmap_info, N)
victory_ratio = (victory_counts / N) * 100

print(victory_ratio)

plt.figure(figsize=(6, 5))

sns.heatmap(
    victory_ratio,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    cbar_kws={'label': 'Frequência relativa'}
)

plt.title("Vitórias por minitabuleiro")
plt.xlabel("Coluna do minitabuleiro")
plt.ylabel("Linha do minitabuleiro")
plt.tight_layout()
plt.show()
