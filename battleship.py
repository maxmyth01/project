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
gray = Color(0xD3D3D3,1)
red = Color(0xFF0000,1)
blue = Color(0x0000FF,1)



def buildBoard():
    data['board'] = []
    for i in range(0,COLS):
        data['board'].append([0]*ROWS)
    return data['board']



def redrawAll():
    square = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,black),blue)
    ship = blueCircle = CircleAsset(0.5*CELL_SIZE,LineStyle(1,black),gray)
    miss = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,black),white)
    hit  = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,black),red)
    for item in App().spritelist[:]:
        item.destroy()
    for z in range (0,2):
        for col in range(0,COLS):
            for row in range(0,ROWS):
                Sprite(square,(row*CELL_SIZE +(200*z),col*CELL_SIZE))
                if z == 0 and data['playerboard'][row][col] == "x": #print a ship on your board so you can see the computers move
                    Sprite(ship,(row*CELL_SIZE +(200*z)+(0.5*CELL_SIZE),col*CELL_SIZE+(0.5*CELL_SIZE)))
                if z == 0 and data['playerboard'][row][col] == "y": # print a miss
                    Sprite(miss,(row*CELL_SIZE +(200*z),col*CELL_SIZE))
                if z == 0 and data['playerboard'][row][col] == "z": # print a hit
                    Sprite(hit,(row*CELL_SIZE +(200*z)),(col*CELL_SIZE))
                if z == 1 and data['computerboard'][row][col] == "y": # print a miss your current moves to plan your next
                    Sprite(miss,(row*CELL_SIZE +(200*z),col*CELL_SIZE))
                if z == 1 and data['computerboard'][row][col] == "z": # print a hit
                    Sprite(hit,(row*CELL_SIZE +(200*z),col*CELL_SIZE))
                if z == 1 and data['computerboard'][row][col] == "x": # helping code
                    Sprite(ship,(row*CELL_SIZE +(200*z)+(0.5*CELL_SIZE),col*CELL_SIZE+(0.5*CELL_SIZE)))



def pickComputerShips(): # x represents a ship
    data['cships'] =0 
    while data['cships'] < 3:
        rand1 = randint(0,COLS-1)
        rand2 = randint(0,ROWS-1)
        if data['computerboard'][rand1][rand2] != "x":
            data['computerboard'][rand1][rand2] = "x"
            data['cships'] += 1
        
    

def computerTurn(): # y represents a miss, z is a hit
    while True:
        rand1 = randint(0,COLS-1)
        rand2 = randint(0,ROWS-1)
        if data['playerboard'][rand1][rand2] != "y" and data['playerboard'][rand1][rand2] != "z":
            if data['playerboard'][rand1][rand2] == 0:
                print('max', rand1, rand2)
                data['playerboard'][rand1][rand2] = "y"
                data['playerboard'][rand1][rand2] = "y"
                break
            else:
                data['pships'] -= 1
                if data['pships'] == 0:
                    print("The Computer wins!")
                    break
                data['playerboard'][rand1][rand2] = "z"
                break
    redrawAll()
    
    
    
def mouseClick(event):
    
    
    if data['placedships'] == False:
        x_location = event.x // CELL_SIZE # lets user place their ships on their board, left side
        y_location = event.y // CELL_SIZE
        
        if data['pships'] < 3:
            print('hi',x_location,y_location)
            if data['playerboard'][x_location][y_location] == 0: #if empty cell mark as ship
                data['playerboard'][x_location][y_location] = "x"
                data['pships'] += 1
                redrawAll()
                print(data['playerboard'])
                print(data['computerboard'])
            elif data['computerboard'][x_location][y_location] == "x": #if already a ship do nothing
                print("INVALID MOVE, GO AGAIN")
        if data['pships'] == 3: 
            data['placedships'] = True
        
    else:
        x_location = (event.x - 200) // CELL_SIZE # lets user attack enemy board, right side
        y_location = (event.y) // CELL_SIZE
        if data['computerboard'][x_location][y_location] == 0: #if empty cell mark as miss
            data['computerboard'][x_location][y_location] = "y"
        elif data['computerboard'][x_location][y_location] == "x": #if ship mark as hit
            data['computerboard'][x_location][y_location] = "z"
            data['cships'] -= 1
            
        elif data['computerboard'][x_location][y_location] == "z" or data['computerboard'][x_location][y_location0] == "y":
            print("INVALID MOVE, GO AGAIN, ALREADY SELECTED TILE") 
        else:
            print("INVALID MOVE, OUT OF RANGE")
        redrawAll()
        print(data['playerboard'])
        print(data['computerboard'])
        #after your turn checks if you won
        if data['cships'] == 0:
            print("The player wins!")
        computerTurn()
        
    
    

    
if __name__ == '__main__':
    
    data = {}
    data['board'] = []
    data['playerboard'] = []
    data['computerboard'] = []
    data['cships'] =0
    data['pships'] =0
    data['placedships'] = False

    data['playerboard'] = buildBoard()
    data['computerboard'] = buildBoard()
  
    redrawAll()
    pickComputerShips()

    print(data['playerboard'])
    print(data['computerboard'])

    
    App().listenMouseEvent('click', mouseClick)
    
    App().run()
