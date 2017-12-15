#Max Low
#12-14-17
#battleship.py -- battleship game

from ggame import *

 #constants and colors
ROWS = 5
COLS = 5
CELL_SIZE = 20
black = Color(0x000000,1)
white = Color(0xFFFFFF,1)

def buildBoard():
    board = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    return board

"""
def redrawAll():
square = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,black ),white)
 for row in range(0,5):
        for col in range(0,5):
            print(board[row][col],' ',end = '')
        print()
    
def pickComputerShips():
    
def computerTurn():
    
def mouseClick():
"""
    
if __name__ == '__main__':

    print(buildBoard())
