'''
Com 10**5 simulações:

Média de jogadas até a vitória: 67.60
Desvio padrão: 9.04
Mínimo de jogadas: 25
Máximo de jogadas: 81

'''

from lib.agents.random import RandomAgent
from lib.runner import run

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def accumulate_plays(game, plays):
    if game.getWinner() == 0:
        return plays
    
    if plays is None:
        return [game.getNumMoves()]

    plays.append(game.getNumMoves())
    return plays

N = 10**5
player1 = RandomAgent()
player2 = RandomAgent()

all_moves = run(player1, player2, accumulate_plays, N)

media = np.mean(all_moves)
desvio = np.std(all_moves)
minimo = np.min(all_moves)
maximo = np.max(all_moves)

print(f"Média de jogadas até a vitória: {media:.2f}")
print(f"Desvio padrão: {desvio:.2f}")
print(f"Mínimo de jogadas: {minimo}")
print(f"Máximo de jogadas: {maximo}")

# Criar boxplot único
plt.figure(figsize=(8, 6))
sns.boxplot(data=all_moves)
plt.title("Número de jogadas até a vitória (sem empates)")
plt.ylabel("Jogadas até a vitória")
plt.xticks([0], ["Todos os confrontos"])
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()