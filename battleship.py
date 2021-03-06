#Max Low
#12-14-17
#battleship.py -- battleship game, three ships against 3 computer picks randomly

from ggame import *
from random import randint



#constants and colors
ROWS = 5
COLS = 5
CELL_SIZE = 50
BOARD_SEPARATE = 500
black = Color(0x000000,1)
white = Color(0xFFFFFF,1)
gray = Color(0xD3D3D3,1)
red = Color(0xFF0000,1)
blue = Color(0x0000FF,1)



def buildBoard():# create the list that maintain the board
    data['board'] = []
    for i in range(0,COLS):
        data['board'].append([0]*ROWS)
    return data['board']



def redrawAll(): # recreaet the board after each action accoding to the state of the lists and sprites graphics
    square = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,black),blue)
    ship = blueCircle = CircleAsset(0.5*CELL_SIZE,LineStyle(1,black),gray)
    miss = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,black),white)
    hit  = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,black),red)
    for item in App().spritelist[:]:
        item.destroy()
    for z in range (0,2): #allows for two boards to be created by a seprate distance 
        for col in range(0,COLS):
            for row in range(0,ROWS):
                Sprite(square,(row*CELL_SIZE +(BOARD_SEPARATE*z),col*CELL_SIZE))
                if z == 0 and data['playerboard'][row][col] == "x": #print a ship on your board so you can see the computers move
                    Sprite(ship,(row*CELL_SIZE +(BOARD_SEPARATE*z)+(0.5*CELL_SIZE),col*CELL_SIZE+(0.5*CELL_SIZE)))
                if z == 0 and data['playerboard'][row][col] == "y": # print a miss
                    Sprite(miss,(row*CELL_SIZE +(BOARD_SEPARATE*z),col*CELL_SIZE))
                if z == 0 and data['playerboard'][row][col] == "z": # print a hit
                    Sprite(hit,(row*CELL_SIZE +(BOARD_SEPARATE*z),col*CELL_SIZE))
                if z == 1 and data['computerboard'][row][col] == "y": # print a miss your current moves to plan your next
                    Sprite(miss,(row*CELL_SIZE +(BOARD_SEPARATE*z),col*CELL_SIZE))
                if z == 1 and data['computerboard'][row][col] == "z": # print a hit
                    Sprite(hit,(row*CELL_SIZE +(BOARD_SEPARATE*z),col*CELL_SIZE))



def pickComputerShips(): # x represents a ship in the list
    data['cships'] =0 
    while data['cships'] < 3:
        rand1 = randint(0,COLS-1)
        rand2 = randint(0,ROWS-1) #random placement of computer ships
        if data['computerboard'][rand1][rand2] != "x": #prevents repeats
            data['computerboard'][rand1][rand2] = "x"
            data['cships'] += 1
        
    

def computerTurn(): # y represents a miss, z is a hit
    if data['end'] == False:
        while True:
            rand1 = randint(0,COLS-1)
            rand2 = randint(0,ROWS-1)
            if data['playerboard'][rand1][rand2] != "y" and data['playerboard'][rand1][rand2] != "z": # prevents placing another shot on existing misses and hits
                if data['playerboard'][rand1][rand2] == 0:
                    data['playerboard'][rand1][rand2] = "y"
                    break
                else:
                    data['pships'] -= 1
                    if data['pships'] == 0:# check to see if the player is out of ship and they lose
                        print("The Computer wins!")
                        data['end'] = True 
                    data['playerboard'][rand1][rand2] = "z"
                    break
        redrawAll()
    
    
    
def mouseClick(event):
    if data['end'] == False:
        if data['placedships'] == False:
            x_location = event.x // CELL_SIZE # lets user place their ships on their board, left side
            y_location = event.y // CELL_SIZE
            
            if data['pships'] < 3:
                if data['playerboard'][x_location][y_location] == 0: #if empty cell mark as ship
                    data['playerboard'][x_location][y_location] = "x"
                    data['pships'] += 1
                    redrawAll()
                elif data['computerboard'][x_location][y_location] == "x": #if already a ship do nothing
                    print("INVALID MOVE, GO AGAIN")
            if data['pships'] == 3: 
                data['placedships'] = True
            
        else:
            x_location = (event.x - BOARD_SEPARATE) // CELL_SIZE # lets user attack enemy board, right side
            y_location = (event.y) // CELL_SIZE
            if data['computerboard'][x_location][y_location] == 0: #if empty cell mark as miss
                data['computerboard'][x_location][y_location] = "y"
            elif data['computerboard'][x_location][y_location] == "x": #if ship mark as hit
                data['computerboard'][x_location][y_location] = "z"
                data['cships'] -= 1
            elif data['computerboard'][x_location][y_location] == "z" or data['computerboard'][x_location][y_location] == "y":
                print("INVALID MOVE, GO AGAIN, ALREADY SELECTED TILE")
                data['sucessful_shot'] = False
            else:
                print("INVALID MOVE, OUT OF RANGE")
                data['sucessful_shot'] = False
            redrawAll()
            #after your turn checks if you won and to end the game, if not end allows computer to play
            if data['cships'] == 0:
                print("The player wins!")
                data['end'] = True
                
            if data['sucessful_shot'] == True: # checks to see that the person sucessful shot before allowing computer turn
                computerTurn()
            data['sucessful_shot'] = True #reset for next turn
        

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
    data['sucessful_shot'] = True
    data['end'] = False
  
    redrawAll()
    pickComputerShips()

    App().listenMouseEvent('click', mouseClick)
    App().run()