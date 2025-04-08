from progress.bar import ChargingBar
from progress.spinner import PixelSpinner
from .tictactoe import Game

def run(player1, player2, accumulate=lambda: None, n=1000):
    current_player = player1
    info = None

    spinner = PixelSpinner('Simulating games... ')
    for _ in ChargingBar('Simulating games...   ', suffix="%(percent)d%% | %(elapsed)ds elapsed").iter(range(n+1)):
        game = Game()
        spinner.start()

        while not game.isEnd():
            move = current_player.getAction(game)
            game.move(move)
            current_player = player2 if current_player == player1 else player1
            spinner.next()

        info = accumulate(game, info)

    spinner.finish()
    return info
