from DotsAndBoxes import *
print("Please enter the length, width, and (ai)depth of the board (x,y,z): ")
m = int(input("enter length :"))
n= int(input("enter width :"))

ply = int (input("enter ai depth"))
game = DotsAndBoxes(m, n, ply)
game.playGame()