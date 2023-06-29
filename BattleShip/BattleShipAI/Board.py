import copy
from Tile import Tile
import random

class Board:

    def __init__(self,height,width,ships) -> None:
        self.height = height
        self.width = width
        self.numOfShips = 0
        self.gameState = [[Tile() for i in range(height)] for j in range(width)]
        self.ships = ships
        self.randomizeBoard(ships)
        self.done = False

    #updates state of board. 
    #if returns false it is not a valid hit.
    def updateState(self,row,column):
         
         #checks if valid row and column number
         if(row>len(self.gameState)):
             return False
         
         if(column>len(self.gameState[0])):
             return False
         
         if (row <1 or column <1):
             return False
         
         tile = self.gameState[row-1][column-1]

        
         if(tile.hit()):
            pass
         else:
             return False
         
         #returns if its a miss
         if(tile.state == -1):
             return "Miss"
         
         if(self._shipSunk(-tile.state)):
            #sorrounds ship and gets the length
            length = self._sorroundShip(-tile.state)
            self.ships[length-1] = self.ships[length-1] -1
        
         if(self.numOfShips==0):
            self.done = True
         
         return "Hit"
    
    def printBoard(self):
        for row in self.gameState:
            print('  '.join(str(tile.state) for tile in row))

    #creates a new board. Returns false if fails 100 times
    #ships array should be like so,
    #first entry is number of ships of size 1
    #second is number of ships of size 2
    #etc
    def randomizeBoard(self,ships):

        #if impossible to create returns false
        if(len(ships)+1 > self.height and len(ships)+1 > self.width):
            return False
        
        while(True):
            boardCopy = copy.deepcopy(self)
            failed = False
            length = 1

            #adds ships by length
            for num in ships:
                while num > 0:
                    if boardCopy._addRandomShip(length):
                        num -= 1
                    else:
                        failed = True
                        break

                if failed:
                    break

                length += 1

            if not failed:
                self.gameState = copy.deepcopy(boardCopy.gameState)
                return True
            

    #erases Ships
    #keeps all misses, hits, and sunk ships
    def eraseShips(self):
        for row in self.gameState:
            for tile in row:
                if(tile.state >0):
                    tile.state = 0


    #takes ship ID and checks if any more of the ship remains on the board
    def _shipSunk(self,ID):
        Sunk = True
        
        #checks if the ID is still on the baord
        for row in self.gameState:
            for tile in row:
                if(tile.state == ID):
                    Sunk = False

        #returns true if ship sink and decreases ship count
        if(Sunk):
            self.numOfShips = self.numOfShips-1
            return True
        
    #inputs the ID of the sunken ship and hits every tile around the ship    
    #returns lenght of ship
    def _sorroundShip(self,ID):

        found = False

        #finds one tile of the sunken ship
        rowIndex = 0
        columnIndex =0
        while (rowIndex < self.height):
            while (columnIndex < self.width):
                tile = self.gameState[rowIndex][columnIndex]
                if(tile.state == -ID):
                    startTile = tile
                    found = True
                    break
                columnIndex = columnIndex+1
            
            if(found):
                break
            columnIndex = 0
            rowIndex = rowIndex +1

        #finds orientation of ship
        orientation = "H"
        if(columnIndex == self.width-1):
            orientation = "V"
        else:
            tile = self.gameState[rowIndex+1][columnIndex]
            if(tile.state == -ID):
                orientation = "V"

        #for horizontal ships
        if(orientation == "H"):
            #length of horizonaal ship
            check = columnIndex+1
            length =1
            while(check < self.width):
                if(self.gameState[rowIndex][check].state != -ID):
                    break
                length= length +1
                check = check+1
            
            #actually blocks it out
            for i in range(-1,2):
                for j in range (-1,length+1):
                    self.updateState(rowIndex+1 + i,columnIndex+1 + j)

            

        #length of vertical ship
        if(orientation == "V"):
            check = rowIndex+1
            length =1
            while(check < self.height):
                if(self.gameState[check][columnIndex].state != -ID):
                    break
                length= length +1
                check = check+1
         
            #actually blocks it out
            for i in range(-1,2):
                for j in range (-1,length+1):
                    self.updateState(rowIndex+1 + j,columnIndex+1 + i)
        
        return length

    # adds a new ship. Returns false if invalid
    def _newShip(self,row,column,length,orienation):

        #checks if valid orientation
        if(orienation != "H" and orienation != "V"):
            return False

        if(orienation == "H"):
            
            #checks for validity of ship
            valid = True 
            if(column + length-1  > self.width):
                return False
            
            #checks for validity of ship
            for i in range (0,length):
                #ensures there are no ships in the sorrounding
                if(self.gameState[row-1][column+i-1].state >1):
                    valid= False
            
            if(not valid):
                return False
            
            #adds ship
            for i in range (0,length):
                self.gameState[row-1][column+i-1].state = self.numOfShips + 2
            
            self.numOfShips = self.numOfShips +1

        if(orienation == "V"):
            
            #checks for validity of ship
            if(row + length -1  > self.height):
                return False
            
            #checks for validity of ship
            valid = True 
            for i in range (0,length):
                #ensures there are no ships in the sorrounding
                if(self.gameState[row+i-1][column-1].state >1):
                    valid= False
            
            if(not valid):
                return False
            
            #adds ship
            for i in range (0,length):
                self.gameState[row+i-1][column-1].state = self.numOfShips + 2
            
            self.numOfShips = self.numOfShips +1

        return True

            
    #creates ship on random position on board with a specified length
    #returns false if its fails 25 times
    def _addRandomShip(self, length):

        for i in range (0,25):
            #creates orientation
            orientation= "H"

            if(random.random() > .5):
                orientation = "V"

            #creates random position
            column = random.randint(1,self.width)
            row = random.randint(1,self.height)

            #changes one axis to make it valid
            if(orientation == "V"):
                row = random.randint(1,self.height-length+1)

            if(orientation == "H"):
                column = random.randint(1,self.width-length+1)

            if(self._newShip(row,column,length,orientation)):
                return True
            
        return False
    

        
        