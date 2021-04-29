from random import *
import collections

from Board import *


class Algorithm:

    def miniMax(State, Ply_num):

        for i in range(State.Current.dimensionY):
            for j in range(State.Current.dimensionX):
                if State.Current.Mat[i][j] == ' ' and (j, i) not in State.children:
                    State.Make(j, i, True)
                    if Ply_num < 2:
                        return (i, j)

        Minimum_Score = 1000
        i = 0
        j = 0
        for k, z in State.children.items():
            Result = Algorithm.Maximum(z, Ply_num - 1, Minimum_Score)
            if Minimum_Score > Result:
                Minimum_Score = Result
                i = k[0]
                j = k[1]

        return (i, j)

    def Maximum(State, Ply_num, Alpha):
        if Ply_num == 0:
            return State.CurrentScore

        for i in range(State.Current.dimensionY):
            for j in range(State.Current.dimensionX):
                if State.Current.Mat[i][j] == ' ' and (j, i) not in State.children:
                    State.Make(j, i, False)

        Maximum_Score = -1000
        i = 0
        j = 0
        for k, z in State.children.items():
            Result = Algorithm.Minimum(z, Ply_num - 1, Maximum_Score)
            if Maximum_Score < Result:
                Maximum_Score = Result
            if Result > Alpha:
                return Result

        return Maximum_Score

    def Minimum(State, Ply_num, Beta):
        if Ply_num == 0:
            return State.CurrentScore

        for i in range(State.Current.dimensionY):
            for j in range(State.Current.dimensionX):
                if State.Current.Mat[i][j] == ' ' and (j, i) not in State.children:
                    State.Make(j, i, True)

        Minimum_Score = 1000
        i = 0
        j = 0
        for k, z in State.children.items():
            Result = Algorithm.Maximum(z, Ply_num - 1, Minimum_Score)
            if Minimum_Score > Result:
                Minimum_Score = Result
            if Result < Beta:
                return Result

        return Minimum_Score


class Thing:
    def __init__(self, currentState):
        self.Current = currentState
        self.CurrentScore = 0
        self.children = {}

    def Make(self, i, j, player):
        self.children[(i, j)] = Thing(self.Current.Get_currentState())
        mul = 1
        if player:
            mul *= -1
        self.children[(i, j)].CurrentScore = (self.children[(i, j)].Current.action(i, j) * mul) + self.CurrentScore

    def Populate(self, i, j, Child):
        self.children[(i,j)] = Child

    def Draw(self):
        self.Current.Draw_mat()


class DotsNBoxes: 
    def __init__(self, Board_Xdim, Board_Ydim, Ply_num):
        currentState = Game([], Board_Xdim, Board_Ydim)
        currentState.Initiate()
        self.State = Thing(currentState)
        self.Ply_num = Ply_num
        self.Score = 0

    def players(self): 
        self.State.Draw()

        playersX = int(input("enter the 'X' coordinate : "))
        playersY = int(input("enter the 'Y' coordinate : "))
        if (playersX, playersY) not in self.State.children:
            self.State.Make(playersX, playersY, False)
            self.State = self.State.children[(playersX, playersY)]
        else:
            self.State = self.State.children[(playersX, playersY)]

        print("Score ==>> Your Score - AI Score = " + str(self.State.CurrentScore),end ="\n\n\n")

        self.AI_Player()


    def AI_Player(self): 
        self.State.Draw()

        move = Algorithm.miniMax(self.State, self.Ply_num)

        self.State = self.State.children[(move[0], move[1])]

        print("AI Move:\n" + "(" ,str(move[0]), ", " + str(move[1]), ")", end = "\n\n")

        print("Score ==>> Your Score - AI Score = " + str(self.State.CurrentScore), end = "\n\n\n")

        if len(self.State.children) == 0:
            self.State.Draw()
            self.Evaluation()
            return

        self.players()

    def Evaluation(self): 
        print("Evaluating!!!\n")
        if self.State.CurrentScore > 0:
            print("You won!")
            exit()
        elif self.State.CurrentScore < 0:
            print("AI won!")
            exit()
        else:
            print("tie")
            exit()

    def start(self):
        self.players()


def main():
    while True:

        print("\t\t!! Welcome !!\n\n\n")

        x = input("Press 0 or any other key to discontinue\n\n")
        if x == "0":

            Board_Xdim = int(input("\nrows : \n")) * 2 + 1

            if Board_Xdim < 5:
                print("\nthe number of rows should atleast be 2\n")
                exit()

            Board_Ydim = int(input("\ncolumns for the board: \n")) * 2 + 1

            if Board_Ydim < 5:
                print("\nthe number of columns should atleast be 2\n")
                exit()

            Ply_num = int(input("\nplies : \n"))

            if Ply_num < 2:
                print("\nThe number of plies should be higher than 1\n")
                exit()

            Match = DotsNBoxes(Board_Xdim, Board_Ydim, Ply_num)
            Match.start()
        else:
            print("\n\nexiting...")
            exit()


if __name__ == "__main__":
    main()