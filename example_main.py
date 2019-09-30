''''

EXAMPLE RUN FUNCTION - MM - Final Version - 6/12/18
An example template function to carry out tetris solving 

'''

import numpy as np
from findSolutions import findSolutions
from pieceBin import pieceBin
from target import target

# Set testMode to true during development. False for the real run
testMode = False

'''
Purpose: Tetris solving function
Parameters: 
    targetGrid: The target region grid
    piecesLimit: The set quantity of tetromino pieces
Return: Solution Matrix
'''
def Tetris (targetGrid, piecesLimit):

    # Grid
    gridSize = 4
    
    z = []
    t = []

    # Get a target for a gridSizexgridSize grid
    challangeTarget = target(targetGrid, gridSize, testMode)
    
    # Power up the pieced bin
    pieces = pieceBin(piecesLimit, gridSize, testMode)

    #Bash the target
    challangeTarget.bashBits()
    
    # Find Solutions
    findSolutions(challangeTarget, pieces, gridSize, 0)

    # Slice target and rerun with a shift of 1
    challangeTarget.sliceTarget(1)
    challangeTarget.bashBits()
    findSolutions(challangeTarget, pieces, gridSize, 1)

    # Shift
    challangeTarget.sliceTarget(1)
    challangeTarget.bashBits()
    findSolutions(challangeTarget, pieces, gridSize, 2)

    # Shift
    challangeTarget.sliceTarget(1)
    challangeTarget.bashBits()
    findSolutions(challangeTarget, pieces, gridSize, 3)        
    
    tots = sum(pieces.limitArray.values())
    z.append(challangeTarget.targetSolution)
    t.append(tots)
    
    # Add further shifts...
    
    s = np.argmin(t)
    challangeTarget.targetSolution = z[s]
    M = challangeTarget.targetSolution
    return M