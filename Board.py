from random import *


class Game: 
    def __init__(self, Mat, dimensionX, dimensionY):
        self.Mat = Mat
        self.dimensionX = dimensionX
        self.dimensionY = dimensionY

    def Initiate(self): 
        for i in range(0, self.dimensionY):
            R = []
            for j in range (0, self.dimensionX):
                if i % 2 == 1 and j % 2 == 1:
                    R.append(randint(1, 9))  
                elif i % 2 == 0 and j % 2 == 0:
                    R.append('*') 
                else:
                    R.append(' ') 
            self.Mat.append(R)

    def Get_matrix(self): 
        ans = []
        for i in range(0, self.dimensionY):
            R = []
            for j in range(0, self.dimensionX):
                R.append(self.Mat[i][j])
            ans.append(R)
        return ans

    def Draw_mat(self): 
        
        if self.dimensionX > 9:
            print(" ", end='')
        print("   ", end='')
        for i in range(0, self.dimensionX):
            print(str(i), end='  ')
        print()

        if self.dimensionX > 9:
            print(" ", end='')
        print("   ", end='')
        for i in range(0, self.dimensionX + 1):
            print("___", end='')
        print()
        for j in range(self.dimensionY):
            if self.dimensionX > 9 and j < 10:
                print(" ", end='')
            print(str(j) + "| ", end='')
            for z in range(self.dimensionX):
                print(str(self.Mat[j][z]), end='  ')
            print()
        print("   _________________________\n")

    def Get_currentState(self):
        return Game(self.Get_matrix(), self.dimensionX, self.dimensionY)

    def action(self, i, j): 
        Sum = 0

        if j % 2 == 0 and i % 2 == 1:
            self.Mat[j][i] = '-'
            if j < self.dimensionY - 1:
                if self.Mat[j+2][i] == '-' and self.Mat[j+1][i+1] == '|' and self.Mat[j+1][i-1] == '|':
                    Sum += self.Mat[j+1][i]
            if j > 0:
                if self.Mat[j-2][i] == '-' and self.Mat[j-1][i+1] == '|' and self.Mat[j-1][i-1] == '|':
                    Sum += self.Mat[j-1][i]

        else:
            self.Mat[j][i] = '|'
            if i < self.dimensionX - 1:
                if self.Mat[j][i+2] == '|' and self.Mat[j+1][i+1] == '-' and self.Mat[j-1][i+1] == '-':
                    Sum += self.Mat[j][i+1]
            if i > 0:
                if self.Mat[j][i-2] == '|' and self.Mat[j+1][i-1] == '-' and self.Mat[j-1][i-1] == '-':
                    Sum += self.Mat[j][i-1]
        return Sum
