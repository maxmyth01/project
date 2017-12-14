#Max Low
#12-14-17
#battleship.py -- battleship game

def buildBoard():
    board = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    for row in range(0,5):
        for col in range(0,5):
            print(board[row][col],' ',end = '')
        print()
"""
def redrawAll():
    
def pickComputerShips():
    
def computerTurn():
    
def mouseClick():
"""
    
if __name__ == '__main__':
    buildBoard()
