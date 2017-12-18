#Max Low
#12-14-17
#battleship.py -- battleship game

from ggame import *
from random import randint

 #constants and colors
ROWS = 3
COLS = 8
CELL_SIZE = 20
black = Color(0x000000,1)
white = Color(0xFFFFFF,1)

def buildBoard():
    data['board'] = []
    subboard = []
    for i in range(0,COLS):
        data['board'].append([0]*ROWS)
    return data['board']


def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()

    for z in range (0,2):
        y=0
        square = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,black),white)
        for row in range(0,ROWS):
            x=0
            for col in range(0,COLS):
                if z == 1:
                    x = x+200
                    z+=1
                Sprite(square,(x,y))
                x += CELL_SIZE
            y += CELL_SIZE

def pickComputerShips():
    ships =0 
    while ships < 3:
        if data['board'][randint(0,COLS-1)][randint(0,ROWS-1)] != "x":
            data['board'][randint(0,COLS-1)][randint(0,ROWS-1)]
            ships += 1
        
    
"""
def computerTurn():
    
def mouseClick():
"""
    
if __name__ == '__main__':
    
    data = {}
    data['board'] = []

    print(buildBoard())
    redrawAll()
    pickComputerShips()
    print(data['board'])
    
    App().run()
