from lib.agents import RandomAgent, AlphaBetaAgent
from lib.runner import run

player1 = RandomAgent()
player2 = RandomAgent()

def accumulate(game, previous_info):
    if previous_info is not None:
        return previous_info + 1

    return 1

n = 10**4

info = run(player1, player2, accumulate, n)

print(f"Total games played: {n}")
print(f"Total accumulated: {info}")
