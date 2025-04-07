import random, copy
import numpy as np

class Game:
    def __init__(self, dim=3):
        self.dim = dim
        self.board = np.zeros((self.dim**2, self.dim**2))
        self.miniWins = np.zeros((self.dim, self.dim))
        self.currPlayer = -1 + 2*random.randint(0,1)
        self.validMoves = [(x,y) for x in range(self.dim*self.dim) for y in range(self.dim*self.dim)]
        self.numMoves = 0
        self.winner = 0

    def getMoves(self): return self.validMoves
    def getNumMoves(self): return self.numMoves
    def getRandomMove(self): return random.choice(self.validMoves)
    def getCurrPlayer(self): return self.currPlayer
    def getMiniWins(self): return self.miniWins
    def getBoard(self): return self.board
    def isEnd(self): return self.winner != 0 or not self.validMoves
    def getWinner(self): return self.winner

    def generateSuccessor(self, action):
        newGame = copy.deepcopy(self)
        newGame.move(action)
        return newGame

    def move(self,pos):
        if not pos in self.validMoves:
            raise Exception("Invalid Move")
        self.board[pos[0]][pos[1]] = self.currPlayer
        self.updateMiniWinners(pos)
        self.updateWinner()
        self.updateValidMoves(pos)
        self.currPlayer = -self.currPlayer
        self.numMoves += 1

    def updateValidMoves(self,pos):
        self.validMoves = []
        r0 = pos[0] % self.dim
        c0 = pos[1] % self.dim
        for dr in range(self.dim):
            for dc in range(self.dim):
                r = self.dim*r0 + dr
                c = self.dim*c0 + dc
                if self.board[r][c] == 0:
                    self.validMoves.append((r,c))
        if self.validMoves == []:
            for r in range(self.dim**2):
                for c in range(self.dim**2):
                    if self.board[r][c] == 0:
                        self.validMoves.append((r,c))

    def updateMiniWinners(self,pos):
        r0 = pos[0]//self.dim
        c0 = pos[1]//self.dim
        row = r0 * self.dim
        col = c0 * self.dim
        miniBoard = self.board[row : row + self.dim, col : col + self.dim]
        if self.miniWins[r0][c0] == 0 and self.hasWinningPattern(miniBoard):
            self.miniWins[r0][c0] = self.currPlayer

    def updateWinner(self):
        if self.winner == 0 and self.hasWinningPattern(self.miniWins):
            self.winner = self.currPlayer

    def hasWinningPattern(self, board):
        for dr in range(self.dim):
            if abs(sum(board[dr, i] for i in range(self.dim))) == self.dim:
                return True
        for dc in range(self.dim):
            if abs(sum(board[i, dc] for i in range(self.dim))) == self.dim:
                return True
        if abs(sum(board[i, i] for i in range(self.dim))) == self.dim:
            return True
        if abs(sum(board[self.dim - 1 - i, i] for i in range(self.dim))) == self.dim:
            return True
        return False