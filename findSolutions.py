''''

SOLUTION FINDER FUNCTION - MM - Final Version - 6/12/18
Finds the optimum solution from a set number of tries, using the pieceBin and target

'''

'''
Purpose: Solution Finder Function
Parameters:
    challangeTarget: The bashed target
    pieces: The piece bin database
    gridSize: The size of the grid (4 used for optimality) 
    windowShift: Grid shift value (same for x and y)
Return: void
'''
def findSolutions(challangeTarget, pieces, gridSize, windowShift):

    for row in range (0, len(challangeTarget.bashedTarget), 1):
        for column in range(0, len(challangeTarget.bashedTarget[0]), 1):
            #isSolved = solutionsGraph.alreadySolved(challangeTarget.bashedTarget[row][column])

            # There is no solution for this
            isSolved = None
            if isSolved == None: 
                if testMode == True:
                    print (f"Test Mode: Need solution: {challangeTarget.bashedTarget[row][column]}")
                
                challange = challangeTarget.bashedTarget[row][column]
                currentBestSolution = []
                currentBestEndPoint = challange
                
                pieces.usePieceTrialRestore()
                inRangeCount = pieces.anyFit(currentBestEndPoint)
                if inRangeCount > 0:
                    if inRangeCount <= 8:                        
                        numberTries = 4
                    else:
                        numberTries = 16

                    while (numberTries != 0):
                        if testMode == True:
                            print (F"Try {numberTries}")
                        rollingSolution = []
                        currentRollingEndPoint = challange  
                        pieces.usePieceTrialRestore()
                                    
                        while (True):
                            nextPieceTuple = pieces.findRandomFit(currentRollingEndPoint)
                            nextPiece = nextPieceTuple[0]     
                            nextPieceId = nextPieceTuple[1]                    

                            if testMode == True:
                                print(f"Found: {nextPiece}")
                                print("{0:b}".format(nextPiece))

                            if nextPiece != 0:
                                rollingSolution.append( (currentRollingEndPoint, currentRollingEndPoint - nextPiece, nextPiece, nextPieceId) )
                                pieces.usePieceTrial(nextPieceId)
                                currentRollingEndPoint -= nextPiece
                                if currentRollingEndPoint == 0:
                                    break
                            else:
                                break

                        if bin(currentRollingEndPoint).count('1') < bin(currentBestEndPoint).count('1'):
                            currentBestEndPoint = int(currentRollingEndPoint)
                            currentBestSolution = list(rollingSolution)
                        else: 
                            numberTries -= 1

                        # We have the perfect solution
                        if currentBestEndPoint == 0:
                            break
                    

                if len(currentBestSolution) > 0:
                    #solutionsGraph.addChallange(challange)
                    for solutionStep in currentBestSolution:
                        #solutionsGraph.addNewSolution(solutionStep[0], solutionStep[1], solutionStep[2])
                        challangeTarget.addSolution(solutionStep[2], gridSize, row, column, solutionStep[3], windowShift)
                        pieces.usePiece(solutionStep[3])
                        if testMode == True:
                            print (f"Test Mode: Adding solution {solutionStep[0]},{solutionStep[1]},{solutionStep[2]}")
                
            # There is a solution but this is not a viable route
            elif isSolved == 0:
                #if testMode == False:
                    print (f"Test Mode: 0 for solution: {challangeTarget.bashedTarget[row][column]}")
            
            # There is a solution
            else:
                #if testMode == False:
                    print (f"Test Mode: Solution exists: {challangeTarget.bashedTarget[row][column]}")
              