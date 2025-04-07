import lib.tictactoe
import random
from lib.agents import AlphaBetaAgent, MCTSagent, DQNagent, RandomAgent, HybridAgent
import time

# Nome e criação dos agentes
agentNames = ['Random', 'Minimax', 'MCTS', 'Hybrid']
agents = [RandomAgent(),
          AlphaBetaAgent(depth=2),
          MCTSagent(itermax=100),
          HybridAgent()]
agents[3].agent1 = agents[2]
agents[3].agent2 = agents[1]

# Lista para armazenar o número de jogadas até a vitória
all_moves = []

def simulateGames(agent1, agent2, n=100):
    for _ in range(n):
        myGame = lib.tictactoe.Game()
        myGame.currPlayer = 1
        while myGame.getMoves() and not myGame.isEnd():
            if myGame.getNumMoves() % 2 == 0:
                myGame.move(agent1.getAction(myGame))
            else:
                myGame.move(agent2.getAction(myGame))
        if myGame.getWinner() != 0:  # Se houve vencedor (sem empates)
            all_moves.append(myGame.getNumMoves())

def main():
    for i in range(len(agentNames)):
        for j in range(i, len(agentNames)):
            label = f"{agentNames[i]} vs {agentNames[j]}"
            print(f"Simulando: {label}")
            start = time.time()
            simulateGames(agents[i], agents[j], n=200)
            print(f"Tempo: {time.time() - start:.2f} s\n")

    # Estatísticas das jogadas
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
    plt.title("Número de jogadas até a vitória (sem empates) - Todos os confrontos")
    plt.ylabel("Jogadas até a vitória")
    plt.xticks([0], ["Todos os confrontos"])
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

main()
