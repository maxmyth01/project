#Max Low
#12-14-17
#battleship.py -- battleship game

from ggame import *
from random import randint

 #constants and colors
ROWS = 5
COLS = 5
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
        square = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,black),white)
        for row in range(0,ROWS):
            for col in range(0,COLS):
                Sprite(square,(row*CELL_SIZE +(200*z),col*CELL_SIZE))

def pickComputerShips(): # x represents a ship
    data['cships'] =0 
    while data['cships'] < 3:
        rand1 = randint(0,COLS-1)
        rand2 = randint(0,ROWS-1)
        if data['computerboard'][rand1][rand2] != "x":
            data['computerboard'][rand1][rand2] = "x"
            data['cships'] += 1
        
    
"""
def computerTurn(): # y represents a miss, z is a hit
    while false:
        rand1 = randint(0,COLS-1)
        rand2 = randint(0,ROWS-1)
        if data['playerboard'][rand1][rand2] != "y":
            if data['playerboard'][rand1][rand2] != "x":
                data['playerboard'][rand1][rand2] = "z"
            else:
                data['playerboard'][rand1][rand2] = "y"
    
    
def mouseClick():
"""
    
if __name__ == '__main__':
    
    data = {}
    data['board'] = []
    data['playerboard'] = []
    data['computerboard'] = []
    data['cships'] =0
    data['pships'] =0
    
    data['playerboard'] = buildBoard()
    data['computerboard'] = buildBoard()
    
    redrawAll()
    pickComputerShips()
    
    print(data['computerboard'])
    print(data['playerboard'])
    
    
    
    
    
    App().run()
