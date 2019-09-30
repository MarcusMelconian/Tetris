# Tetris
An algorithm which solves a random polynomial region with tetromino pieces, using binary logic.

Contains 4 files:

 1. An example main function to run the algorithm, given the correct input parameters.
 
 2. The Find Solution function, responsible for finding all possible solutions.
 
 3. The Piece Bin class, containing the tetromino piece database for the reduced grid size.
 
 4. The Target class, responsible for creating the new solvable target and outputting the solution.

The Challenge:
To design an algorithm to return a solution to fill an arbitrary sized polyomino region with a given set and amount of tetromino pieces. A target matrix grid is given where a 1 represents a 1x1 block in the region to be filled and a 0 should be left blank (not filled by a piece)
