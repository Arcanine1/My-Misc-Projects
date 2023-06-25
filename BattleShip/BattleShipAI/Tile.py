class Tile:

    # -number is ship hit
    # -1 is nothing hit
    # 0 is nothing
    # number is the ship hidden with that ID
    state = 0

    #if you hit a spot you have not hit before returns True and updates the board.
    def hit(self):

        #if already hit return false
        if(self.state <0):
            return False

        if(self.state==0):
            self.state = -1
            return True
        
        if(self.state>0):
            self.state = -self.state
            return True