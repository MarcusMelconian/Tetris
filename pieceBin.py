''''

PIECE BIN CLASS - MM - Final Version - 6/12/18
Contains the piece database stored as a list of tuples

'''

import random

class pieceBin:
    def __init__(self, limitArray, gridSize, testMode = False):
        self.limitArray = dict(limitArray)
        self.gridSize = gridSize
        self.testMode = testMode
        
        # Hard list of tuples of pieces in all possible positions in 4x4 grid
        self.Binners = [
            # The (2,2) gives the max 'x' and 'y' position of the shape from the home position (bottom right corner)
            # Here we have a square with max position of (2,2) in the x & y from the home position
            # Therefore this square can be moved two further up in y or two further across in x while remaining in the grid
            # In a 4x4 grid this max position can't exceed 4 in 'x' or 4 in 'y' for any shape, otherwise they will be outside 
            # the grid
            (51, 1, (2,2)),
            (4369, 2, (1,4)),
            (15, 3, (4,1)),
            (547, 4, (2,3)),
            (23, 5, (3,2)),
            (785, 6, (2,3)),
            (116, 7, (3,2)),
            (275, 8, (2,3)),
            (113, 9, (3,2)),
            (802, 10, (2,3)),
            (71, 11, (3,2)),
            (562, 12, (2,3)),
            (39, 13, (3,2)),
            (305, 14, (2,3)),
            (114, 15, (3,2)),
            (54, 16, (3,2)),
            (561, 17, (2,3)),
            (99, 18, (3,2)),
            (306, 19, (2,3)),
        ]    

        self.pieceBinary = []
        for i in range (0,19):
            # Append the initial value from Binners to pieceBinary
            self.pieceBinary.append(self.Binners[i])
            # Here we are obtaining the information we'll need from the Binners value
            base = self.Binners[i][0]
            ids = self.Binners[i][1]
            x = self.Binners[i][2][0]
            y = self.Binners[i][2][1]
            # Here we are finding the max 'x' and 'y' values that our shape can be shifted to, Eg for shape 1: if gridSize = 4, 4-2 = 2 for x, 4-2 = 2 for y
            xr = gridSize - x
            yr = gridSize - y
            # Find the wub
            if gridSize == 8:
                wub = 256
            else:
                wub = 16
            if xr == 0:
                xr = 0
            else:
                # Appending all the shifts in 'x' possible for the shape
                for j in range (1, xr+1):
                    New1 = (base*(2**j), ids, ((x+j),(y)))
                    self.pieceBinary.append(New1)
            if yr == 0:
                yr = 0
            else:
                # Appending all the shifs in 'y' possible for the shape
                for p in range (1, yr+1):   
                    New2 = (base*(wub**p), ids, ((x),(y+p)))
                    self.pieceBinary.append(New2)
                    if xr == 0:
                        xr = 0
                    else:
                        # Appending all the shifts in 'x' relative to the shifts in 'y' possible for the shape
                        for q in range (1, xr+1):
                            New4 = (base*(wub**p)*(2**q), ids, ((x+q),(y+p)))
                            # If it's already been appended ignore it
                            if New4 in self.pieceBinary:
                                New4 = 0
                            else:
                                self.pieceBinary.append(New4)
            
        # Seed the generator 
        random.seed()

        # If in test mode, slice the grid as it is easier to study (pieces 1 and 2 should do)
        #if self.testMode == True:
            #self.pieceBinary = [pieces for pieces in self.pieceBinary if pieces[1] <= 2]
            #print ("Test Mode: piecesBin: Pieces have been cut down to size:")
            #print (self.pieceBinary)

        if self.testMode == True:
            print ("Test Mode: piecesBin:")
            print (self.pieceBinary)             

        if self.testMode == True:
            print ("Test Mode: Limit:")
            print (self.limitArray)  

    '''
    Purpose: Get a piece at random from pieces still left that will fit given a 
             passed challenge
    Parameters: 
        challange: The bashed target
    Return: void
    '''
    def findRandomFit(self, challange):
        #inRange = [pieces for pieces in self.pieceBinary if pieces[0] <= challange and pieces[0] & challange == pieces[0] and self.limitArrayTrial[pieces[1]] != 0]
        # Faster
        inRange = [pieces for pieces in self.pieceBinary if pieces[0] & challange == pieces[0] and self.limitArrayTrial[pieces[1]] != 0]        

        #if self.testMode == True:
        #    print ("Test Mode: piecesBin: Random in Range")
        #    print (inRange)
        
        if len(inRange) > 0:
           return random.choice(inRange)
           
        return (0, 0, 0)

    '''
    Purpose: Find any fit
    Parameters: 
        challange: The bashed target
    Return: void
    '''
    def anyFit(self, challange):
        inRange = [pieces for pieces in self.pieceBinary if pieces[0] & challange == pieces[0] and self.limitArrayTrial[pieces[1]] != 0]            
        return len(inRange)        

    '''
    Purpose: use a trial limit while we attempt to find a good fit
    Parameters: 
        id: Shape ID
    Return: void
    '''
    def usePieceTrial(self, id):
        if self.limitArrayTrial[id] > 0:
            self.limitArrayTrial[id] -= 1        
        else:
            print (f"Error: Trial Part {id} is being over used!")
        return     

    '''
    Purpose: Reset the trial limit for another go
    Parameters: None
    Return: void
    '''
    def usePieceTrialRestore(self):
        self.limitArrayTrial =  dict(self.limitArray)

    '''
    Purpose: Decrement available count for a piece
    Parameters:
        id: Shape ID
    Return: void
    '''
    def usePiece(self, id):   
        if self.limitArray[id] > 0:
            self.limitArray[id] -= 1
        else:
            print (f"Error: Part {id} is being over used!")
        return