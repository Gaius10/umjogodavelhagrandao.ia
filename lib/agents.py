# agents.py
import random
import collections
import numpy as np
from keras.models import Model
from keras import layers
from tictactoe import Game

class RandomAgent:
    def getAction(self, gameState):
        return gameState.getRandomMove()

class AlphaBetaAgent:
    def __init__(self, depth=3):
        self.depth = depth

    def evaluationFunction(self, gameState):
        return float('inf')*gameState.getWinner() + sum(sum(wins) for wins in gameState.getMiniWins())

    def getAction(self, gameState):
        if gameState.getNumMoves() < 10:
            return gameState.getRandomMove()

        def recurse(gameState, player, depth, alpha, beta):
            if gameState.isEnd() or depth == 0:
                return (self.evaluationFunction(gameState), (-1, -1))
            moves = gameState.getMoves()
            if player == 1:
                ans = (-float('Inf'), (-1, -1))
                for action in moves:
                    ans = max(ans, (recurse(gameState.generateSuccessor(action), -player, depth - 1, alpha, beta)[0], action))
                    alpha = max(alpha, ans)
                    if alpha >= beta:
                        break
                return alpha
            else:
                ans = (float('Inf'), (-1, -1))
                for action in moves:
                    ans = min(ans, (recurse(gameState.generateSuccessor(action), -player, depth - 1, alpha, beta)[0], action))
                    beta = min(beta, ans)
                    if alpha >= beta:
                        break
                return beta

        alph0 = (-float('Inf'), (-1, -1))
        beta0 = (float('Inf'), (-1, -1))
        utility, action = recurse(gameState, gameState.getCurrPlayer(), 2*self.depth, alph0, beta0)
        return action if action != (-1, -1) else gameState.getRandomMove()

class MCTSagent:
    def __init__(self, itermax=10, agent=None):
        self.itermax = itermax
        self.agent = agent or RandomAgent()

    def getAction(self, gameState):
        return self.agent.getAction(gameState)

class HybridAgent:
    def __init__(self):
        self.mcts = MCTSagent(itermax=15, agent=AlphaBetaAgent(depth=1))

    def getAction(self, gameState):
        return self.mcts.getAction(gameState)

class DQNagent:
    def __init__(self, dim=3):
        self.state_size = (dim**2, dim**2, 4)
        self.memory = collections.deque(maxlen=2000)
        self.gamma = 0.95
        self.epsilon = 1.0
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.learning_rate = 0.0001
        self.model = self._build_model()
        self.history = None

    def _build_model(self):
        board_input = layers.Input(shape=self.state_size, name='board')
        board_cnn = layers.Conv2D(64, (3,3), activation='relu', strides=(3,3))(board_input)
        board_cnn = layers.Dropout(0.2)(board_cnn)
        dense_0 = layers.Flatten()(board_cnn)
        dense_1 = layers.Dense(16, activation='relu')(dense_0)
        dense_1 = layers.Dropout(0.2)(dense_1)
        probability = layers.Dense(1, activation='tanh')(dense_1)
        model = Model(board_input, probability)
        model.compile(loss='mean_squared_error', optimizer='rmsprop')
        return model

    def remember(self, state, next_state, winner):
        self.memory.append((state, next_state, winner))

    def extractState(self, game):
        state = np.zeros((1, self.state_size[0], self.state_size[1], self.state_size[2]))
        state[0,:,:,0] = (game.getBoard() == 1)
        state[0,:,:,1] = (game.getBoard() == -1)
        state[0,:,:,2] = (game.getCurrPlayer() == 1)
        for move in game.getMoves():
            state[0,move[0],move[1],3] = 1
        return state

    def getAction(self, game):
        moves = game.getMoves()
        if np.random.rand() <= self.epsilon:
            return random.choice(moves)
        q = []
        for action in moves:
            newState = game.generateSuccessor(action)
            q.append((-self.getVal(newState), action))
        return max(q)[1]

    def getVal(self, game):
        return self.model.predict(self.extractState(game))[0][0] * game.getCurrPlayer()