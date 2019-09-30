''''

TARGET CLASS - MM - Final Version - 6/12/18
Responsible for obtaining the bashed target and returning the final solution

'''

import numpy as np
from copy import deepcopy

class target:
    def __init__(self, target, gridSize, testMode = False):
        self.gridSize = gridSize
        self.testMode = testMode
        self.bashedTarget = []
        self.target = deepcopy(target)
        self.targetSolution = [[(0,0) for x in range(len(self.target[0]))] for y in range(len(self.target))]

        # Make target a multiple of grid + 2, padding with 0's
        if len(self.target) % self.gridSize != 0 or len(self.target[0]) % self.gridSize != 0:
            self.difference1 = self.gridSize - (len(self.target) % self.gridSize) 
            self.difference2 = self.gridSize - (len(self.target[0]) % self.gridSize) 
        else: 
            self.difference1 = 0
            self.difference2 = 0

        self.target = np.pad(self.target, ((0, self.difference1 + 4), (0, self.difference2 + 4)), 'constant')
        
        # Count of soltion uniques 
        self.targetSolutionCounter = 1

        if self.testMode == True:
            print ("Test Mode: target: target:")
            print (self.target)

    '''
    Purpose: Slices the target in order to allow a window shift
    Parameters:
        bySize: The size of the slice in x and y
    Return: void
    '''
    def sliceTarget(self, bySize):
        self.target = self.target[bySize:, bySize:]
        self.target = np.pad(self.target, ((0, bySize), (0, bySize)), 'constant')
        return

    '''
    Purpose: Obtaining the bashed target from the input target matrix
    Parameters: None
    Return: void
    '''
    def bashBits (self): 
        # Can only continue if target is a muliple of bit array size (must be modulus)
        if len(self.target) % self.gridSize  == 0 and len(self.target[0]) % self.gridSize == 0:
            rowsInBasher = int(len(self.target) / self.gridSize )
            columnsInBasher = int(len(self.target[0]) / self.gridSize )
            self.bashedTarget = [[0 for j in range(columnsInBasher)] for i in range(rowsInBasher)]
            
            # For Step in gridSize row and column
            targetSectorRow = 0
            targetSectorColumn = 0
            targetCount = 0

            # For each row in target, stepping in self.gridSize 
            for row in range (0, len(self.target), self.gridSize):

                # For each column in target, stepping in self.gridSize 
                for column in range (0, len(self.target[0]), self.gridSize):
                    # Target is where we are poining to in the taget array at any point in time
                    # We will be scanning self.gridSize  row * self.gridSize  columns moving left to right
                    # Keep track of where we are
                    targetSectorRow = row
                    targetSectorColumn = column
                    targetCount = 0

                    # There will be self.gridSize  * self.gridSize  bits. 
                    for bitPosition in range (self.gridSize * self.gridSize - 1, -1, -1): 
                        # Add next bit to the running total, rembering to shift it left       
                        # The running total is in self.bashedTarget[row/this.gridSize ][column/this.gridSize ]
                        self.bashedTarget[int(row / self.gridSize)][int(column / self.gridSize)] |= (self.target[targetSectorRow][targetSectorColumn] << bitPosition)              

                        # Shift column 
                        targetSectorColumn += 1

                        # targetCount tells us when we need to step to next row (when it is this.gridSize)
                        targetCount += 1

                        # Shift down a row when we have done last column in current row. Back to first column of new row
                        if targetCount == self.gridSize:
                            targetCount = 0 
                            targetSectorRow += 1
                            targetSectorColumn = column
            
            if self.testMode == True:
                print ("Test Mode: target: bashedTarget:")
                print (self.bashedTarget)

        else:
            print ("Error: Can't generate bit array. Unsupported target size")
        return

    '''
    Purpose: Returning the target solution
    Parameters: None
    Return: The final solution matrix
    '''
    def getTargetSolution(self):
        return self.targetSolution

    '''
    Purpose: Adding a solution to the final target solution matrix
    Parameters:
        solutionPiece: The solution piece
        gridsize: Size of grid
        gridRow: Row position in grid
        gridColumn: Column position in grid
        pieceId: The shape ID
        windowShift: Window Shift value
    Return:
    '''
    def addSolution(self, solutionPiece, gridsize, gridRow, gridColumn, pieceId, windowShift):
        bit = 1
        bitRow = gridsize -1
        bitColumn = gridsize -1 

        while solutionPiece >= bit:
            if solutionPiece & bit:             
                self.targetSolution[(gridsize * gridRow) + bitRow + windowShift][(gridsize * gridColumn) + bitColumn + windowShift] = (pieceId, self.targetSolutionCounter)
                self.target[(gridsize * gridRow) + bitRow][(gridsize * gridColumn) + bitColumn] = 0

            bit <<= 1            
            bitColumn -= 1
            if bitColumn < 0:
                bitColumn = gridsize -1
                bitRow -= 1
        
        self.targetSolutionCounter += 1

        if self.testMode == True:
            print ("Test Mode: target: Added Solution:")
            print (self.targetSolution)            
        return 