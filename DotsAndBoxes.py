from copy import deepcopy
from Board import *


class DotsAndBoxes:
    def __init__(self, _x, _y, _ply):
        self.ply = _ply
        self.board = Board(_x, _y)

    def playGame(self):

        print("Dots And Boxes")
        while len(self.board.openVectors) > 0:
            print("Coordinate format == x,y,x2,y2")
            print("Hit 0 and enter to quit")

            self.board.displayBoard()

            success = self.playerMove()
            if success is False:
                break

            print("\nPlease wait while your opponent moves...\n")
            self.aiMove()
        self.reportWinner()

    def playerMove(self):

        while True:
            try:
                integers = input("Enter the coordinates of the dots you wish to connect:")
                if integers is 0:
                    return False
                print(integers)
                coordinates = ((eval(integers[0]), eval(integers[1])), (eval(integers[2]), eval(integers[3])))
                print(coordinates)
                success = self.board.move(coordinates, 0)
                print("===> success",success)

                if success == 0:
                    break
                elif success == -1:
                    print("Invalid coordinates specified!")
            except SyntaxError:
                print("Invalid input, please try again...")
        return True

    def aiMove(self):
        state = deepcopy(self.board)
        openVectors = deepcopy(self.board.openVectors)

        coordinates = self.minimax(state, openVectors, self.ply, True)

        self.board.move(coordinates[1], 1)

    def minimax(self, state, openVectors, ply, max_min):

        if max_min is True:
            bestMove = (-1000000, None)
        else:
            bestMove = (1000000, None)

        if ply == 0 or len(openVectors) == 0:
            h = self.evaluationFunction(state)
            return (h, None)

        for i in range(0, len(openVectors)):
           
            move = openVectors.pop()

            stateCopy = deepcopy(state)
            openVectorsCopy = deepcopy(openVectors)
            stateCopy.move(move, max_min)

            openVectors.appendleft(move)

            h = self.evaluationFunction(stateCopy)
            if max_min is True:
                if h >= stateCopy.beta:
                    return (h, move)
                else:
                    stateCopy.alpha = max(stateCopy.alpha, h)
            else:
                if h <= stateCopy.alpha:
                    return (h, move)
                else:
                    stateCopy.beta = min(stateCopy.beta, h)

            nextMove = self.minimax(stateCopy, openVectorsCopy, ply - 1, not max_min)

            if max_min is True:
                if nextMove[0] > bestMove[0]:
                    bestMove = (nextMove[0], move)
            else:
                if nextMove[0] < bestMove[0]:
                    bestMove = (nextMove[0], move)
        return bestMove

    def evaluationFunction(self, state):
        h = state.aiScore - state.playerScore
        return h

    def reportWinner(self):
        
        self.board.displayBoard()
        if self.board.playerScore > self.board.aiScore:
            print("You won!")
        elif self.board.playerScore < self.board.aiScore:
            print("The AI won!")
        else:
            print("The game was a draw")
        print("Player Score: %s" % self.board.playerScore)
        print("AI Score: %s" % self.board.aiScore)
        print("\nExiting game...")
