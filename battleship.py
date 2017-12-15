#Max Low
#12-14-17
#battleship.py -- battleship game

from ggame import *
from random import randint

 #constants and colors
ROWS = 3
COLS = 12
CELL_SIZE = 20
black = Color(0x000000,1)
white = Color(0xFFFFFF,1)

def buildBoard():
    board = []
    subboard = []
    for j in range(0,ROWS):
        subboard.append(0)
    for i in range(0,COLS):
        board.append(subboard)
    return board


def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()
    
    y=0
    square = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,black),white)
    for row in range(0,ROWS):
        x=0
        for col in range(0,COLS):
            Sprite(square,(x,y))
            x += CELL_SIZE
        y += CELL_SIZE

def pickComputerShips():
    board[randint(0,ROWS)][randint(0,COLS)] = X 
    
"""
def computerTurn():
    
def mouseClick():
"""
    
if __name__ == '__main__':

    print(buildBoard())
    redrawAll()
    
    App().run()
