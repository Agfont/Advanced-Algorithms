## Coded by Aina Ferra Marcus

import time

#------------------------------------------------Enumerative programming: sudoku solver:
##-----------------------------
#This two functions are used in both sudoku solvers.


'''
Parser function.
Transforms a file with numbers and points into a sudoku.
Notice that this function accepts a determinated type of file.
If the file is corrupt, it will return an error
Complexity is O(n) being n = number of boxes (aka 81 boxes in a 9x9 sudoku)
Commonly, we will write O(n^2) being n = number of cols/rows (9 cols/rows => 9x9 sudoku => 81 boxes).

Notice that this is thought for a 9x9 sudoku.
Can be changed for a nxn sudoku by changing the numbers of the matrix for the length of the firs line (for example).
'''
def sudokuParser(fileName):
    matrix = [[0]*9 for v in range(9)]
    fi = open(fileName, "r")
    
    lines = fi.readlines()
    for line in xrange(9):
        for elem in xrange (9):
            if lines[line][elem] != "\n" and  lines[line][elem] != ".":
                matrix[line][elem] = int(lines[line][elem])     
            
    fi.close()
    return matrix

'''
Satisfact function.
Checks if the sudoku can be solved.
Complexity is O(n^2), as said before, being n = number of cols/rows.

Notice again that this is thought for an 9x9 sudoku, it makes de code simplier and cleaner.
Can be easily generalized to a nxn sudoku by reading the length of the first row, for example.
First loops should be len(m[0]), and second loops should be range (0, len(m[0]), sqrt(len(m[0]))).
'''
def satisfact(m):
    #We will put every number in the row /in the col in a list.
    #For every col/row we will check if numbers are repeated. 
    for i in xrange (9):
        auxRows = []
        auxCols = []
        for j in xrange(9):
            if (m[i][j] == 0 or m[i][j] not in auxRows) and (m[j][i] == 0 or m[j][i] not in auxCols):
                auxRows.append(m[i][j])
                auxCols.append(m[j][i])
            else:
                return False
            
    
    #Blocks works the same way.
    #But we need to go steps of 3 on 3.
    for i in xrange(9):
        auxBlocks = []
        for j in xrange(9):
            if (m[(i/3)*3 + j/3][(i%3)*3 + j%3] == 0 or m[(i/3)*3 + j/3][(i%3)*3 + j%3] not in auxBlocks):
                auxBlocks.append(m[(i/3)*3 + j/3][(i%3)*3 + j%3])
            else:
                return False
            
    return True

'''
Auxiliar function to print the sudoku.
This is not really necessary, just for informative purposes.
Complexity is O(n) being n = number of col/rows
'''
def printSudoku(m):
    for i in m:
        print i

##------------------
#-------------------------------------------------------SUDOKU SOLVERS:
        
'''        
This will be our recursive function to fill the sudoku.
There are n^(n^2) possibilities of sudokus, since we have k full boxes
some of these are reduced.
Still, a pretty bad algorythm.

We are working with 9x9 sudokus, so we could have 9^81 possible sudokus.
Here's the worst possible sudoku for solving by brute force:

.........
.....3.85
..1.2....
...5.7...
..4...1..
.9.......
5......73
..2.1....
....4...9

'''

counter = [0]
def fillSudokuBruteForce(m, i, j, t):
    counter[0] += 1
    #Trying tu fill the box.
    m[i][j] = t
    #If the solution is viable:
    if satisfact(m):
        #Find the next empty box
        i, j = findGap(m)
        #If we could find an empty box, we have to fill it.
        if i != -1 and j != -1:
            #Try every possible solution, this is brute force.
            for v in xrange(1, 10):
                state = fillSudokuBruteForce(m, i, j, v)
                #If the solution we returned was viable, then we can keep moving.
                #There would be no need of trying more solutions.
                if state:
                    #True flags the correct solution
                    return True
            #Otherwise, if we reached the end of the loop, this means that any of this solutions is viable.
            #Then, the problem is not in this box, we have to go back and change previous solutions.
            m[i][j] = 0
            return False
        
        else:
            #If we couldn't find any empty boxes, this means that sudoku is solved.
            #Return true to flag it.
            return True
    else:
        #If first offered solution isn't suitable, then empty the box again and try a new one. 
        m[i][j] = 0
        return False
    
'''    
Finding empty boxes in our sudoku takes a lineal time over the elements of the matrix.
It means that compelxity is O(n^2) if we are thinking n = number of cols/rows.
'''
def findGap(m):
    for i in xrange (9):
        for j in xrange (9):
            if m[i][j] == 0:
                return i, j
    #This is for an ugly checking.
    #If the sudoku is already full, then we don't have to do anything else.
    #We will flag this using -1 as a value in our indexes.         
    i , j = -1, -1
    return i, j


'''
This only takes one more check than the function FillSudokuBruteForce, so complexity is the same.
This function, particularly, is used to flag some thinks:
       --Determine whether the initial sudoku is correct or not.
       --Determine whether the initial sudoku is already solved or not.
       --Determine, in case the sudoku is correct and unsolved, the time spent solving it.
       --As a last work, it says if the sudoku has solution. It may be correct, but be unsovable. 
'''
def solveBruteForce(m):
    #If the sudoku is valid, proceed to solve:
    if satisfact(m) == True:
        print "Solving sudoku"
        #We need to find where to start to.
        #Notice here the ugly checking: if the sudoku is already full, we don't have to anything.
        #This is  very small optimization. 
        i, j = findGap(m)
        if i != -1 and j != -1:
            #Remember that this is brute force, we need to go through every possibility:
            t0 = time.clock()
            for k in xrange(1, 10):
                state = fillSudokuBruteForce(m, i, j, k)
                if state:
                    print "Sudoku is solved"
                    printSudoku(m)
                    t1 = time.clock()
                    print "Number of recursion calls", counter[0]
                    print "Time used %0.3f ms" %((t1-t0)*1000)
                    return
            #If we reached that point, it means that the sudoku isn't sovable.
            #It may be a correct sudoku (no repeated numbers in cols/rows/blocks) but without solution.
            #An example is given below.
            print "Sudoku isn't solvable"
        else:
            print "Sudoku was already solved"
    else:
        print "Initial sudoku is incorrect"
        
'''
Correct sudoku without solution:
4...5...1
7.1.2.48.
.238.....
9.7.8.5.2
.3.....4.
2.6.4.9.3
.....621.
..91.3..8
1...9...6
'''
#------------------------------------HEURISTIC SOLUTION-----------------------

'''
The first and easiest way to optimize the algorythm is by checking which numbers
are on the rows/cols/blocks. This should erase some checkings. 
'''


'''
This function discards all repeated numbers in a determinated col, row and block where we locate the position (i, j).
Complexity is linear over n, being n = number of cols/rows.
We are checking 9 elements (a block) and 9 other elements (a col), since row is alreay done and we only need the checking
"if not in list...". Since loops aren't nested, complexity is linear.
'''
def givePossibilities(m, i, j):
    #Checking possible numbers in cols and rows:
    descarted = []
    possibilities = []
    
    #This indexes checks our blocks.
    imod = (i/3)*3
    jmod = (j/3)*3  
    #This is quite ugly, but I just want to check one block (not the whole matrix).
    #We can standarize an index and obtain its block by doing the mathematical operation:
    # i* = (i/3)*3
    # j* = (j/3)*3
    #This gives a couple of numbers (x, y), where  x, y are in {0, 3, 6} which are the
    #primary indexes of the blocks.
    
    #Then, we just do all possible combinations on this block.
    for k in xrange(3):
        if m[imod + k][jmod] != 0:
            descarted.append(m[imod + k][jmod])            
        if m[imod + k][jmod +1] != 0:
            descarted.append(m[imod + k][jmod +1])
        if m[imod + k][jmod+2] != 0:
            descarted.append(m[imod + k][jmod+2])
    
    #This checks the col. Since the list is split (each element of the col is in a diferent row
    #and row is a list kind), we have to climb down the rows.
    for k in xrange (9):
        if (m[i][k] != 0):
            descarted.append(m[k][j])
    
    #Finally, we discarded all options that were already located in some position in this row, col and
    #block where the element belongs. We list as possibilities the not discarded elements.
    for k in xrange (1, 10):
        if k not in descarted and k not in m[i]:
            possibilities.append(k)
    return possibilities
            



'''
This function builds up a matrix of possibilities.
Id est, it looks up for every position that is not already filled and gives the possible solutions.
I decided to leave "-1" to flag the elements that are done (so we don't have to modify them, also we don't need
their possibilities).
This checks every box in the sudoku, so complexity is O(n^2) where n = number of cols/rows.
'''
def buildMatrixOfPossibilities(m):
    #Initial matrix that we will modfy. -1 marks a full box.
    possibleSolutions = [[-1]*9 for v in range(9)]
    #For every possible box in the sudoku:
    for i in xrange (9):
        for j in xrange(9):
            #If the box is empty, look up for the possibilities.
            if m[i][j] == 0:
                possibleSolutions[i][j] = givePossibilities(m, i, j)
        
    return possibleSolutions


'''
This function gives us the best option to solve. It is part of my heuristic.
Besides erasing the repeated numbers, it is better to start for the boxes where there are less possibilities.
For example, if you have one box with only one possibility, you can already fill it and it will be a correct solution
(this means, we have to check less cases). 
So, in this part of code, we look through the matrix of possibilities and decide which is the best option to go on.
In the brute force case, we have a function that looks up for the next empty box. Similarly, this looks up for the
next box to fill, but with the condition that it has to be the best possible option
'''
def findBestOption(m):
    #Again, an ugly checking here. If I don't change this list, this means that I can't find any list of possibilities
    #in any position of the matrix.
    #Therefore, this means that all the boxes are filled. Sudoku is done. 
    best = [0]*9
    #Indexes where we find our best option. 
    indi = 0
    indj = 0
    for i in xrange(9):
        for j in xrange(9):
            #Checking that the box isn't already filled. 
            if m[i][j] != -1:
                if len(m[i][j]) <= len(best):
                    best = m[i][j]
                    indi = i
                    indj = j
                
    return best, indi, indj


'''
Recursive function that fills up our sudoku. Asymptotically, its complexity is the same as the brute force.
Worse case will have to look for every possible solution, this means, practically O(n^(n^2 - k)) being k the number of
already filled boxes and n = number of cols/rows. But, in a midterm, it is way faster. 
'''
counterHeuristic = [0]
def fillSudokuHeuristic(m, i, j, t):
    counterHeuristic[0] += 1
    #Filling up with the value. 
    m[i][j] = t
    #If this solution is correct
    if satisfact(m):
        #Rebuild the matrix of possibilities
        possibilities = buildMatrixOfPossibilities(m)
        #Look for the next best option
        best, i, j = findBestOption(possibilities)
        #If could find an unfilled box:
        if best != [0] *9:
            #try the possible solutions of this box:
            for value in best:
                state = fillSudokuHeuristic(m, i, j, value)
                #If one solution returns true, then this is valid
                if state:
                    return True
            #If we reached this point, this means that none of the solutions were right.
            m[i][j] = 0
            return False
        #If we couldn't find any "best" options, that means that we filled all boxes.
        #We are done, return true.
        else:
            return True
    #If matrix didn't pass out the test, this means that the solution was wrong.
    #Backtracking. 
    else:
        m[i][j] = 0
        return False
    

'''
This our primary function. It makes the primary checking, to see if the sudoku is solvable or not.
It has the same complexity that fillSudokuHeuristic. Also, it makes the same checkings described in BruteForce.
'''
def solveSudokuHeuristic(m):
    #Check if the initial sudoku is correct. 
    if satisfact(m) == True:
        print "Solving sudoku"
        #Building up the matrix of possibilities for our non-filled boxes. 
        possibilities = buildMatrixOfPossibilities(m)
        #Finding where to start for. 
        best, i, j = findBestOption(possibilities)
        #As said before, if we didn't modify this element, this means that the sudoku was solved. 
        if best != [0]*9:
            t0 = time.clock()
            #For every possibility, check if the solution is correct and sudoku is solvable:
            for value in best:
                state = fillSudokuHeuristic(m, i, j, value)
                #If we returned here, this means that the solution given was correct. We can end the process. 
                #Print results and measuring parameters. 
                if state:
                    print "Sudoku is solved"
                    printSudoku(m)
                    print "Number of recursion calls", counterHeuristic[0]
                    t1 = time.clock()
                    print "Time used %0.3f ms" %((t1-t0)*1000)
                    return
            #If we reached that point, this means that sudoku wasn't solvable. It may be correct but with no solution
            #as explained above. 
            print "Sudoku wasn't solvable"
        else:
            "Sudoku was already solved!"
    else:
        print "Given sudoku isn't valid."
        

##Testing our solvers:
def sudokuTest():
    print "Non-heuristic solver" 
    solveBruteForce((sudokuParser("sudoku.txt")))
    print
    print "Heuristic solver"
    solveSudokuHeuristic((sudokuParser("sudoku.txt")))
        

sudokuTest()


'''
A little reflexion about the sudoku:

With this sudoku (listed as an "easy" one):
...259.14
.24...93.
7.1..82.5
....8..9.
.5.1.4.8.
.1..7....
1.86..5.9
.75...12.
64.915...

--Non-heuristic solution takes:
136'68 ms to solve it
1365 recursion calls
--Heuristic solution takes:
42'60 ms to solve it
86 recursion calls

This means that we have ereased 1279 recursion calls.
Algorythm is, aproximately, a 31% faster.

With this sudoku (listed as a "medium" one):
..13....9
4...25.7.
..57.....
157.9....
.6.457.8.
....6.957
.....84..
.8.94...3
9....28..

--Non-heuristic takes:
170.361 ms to solve it 
2523 recursion calls
--Heuristic takes:
350.325 ms to solve it
616 recursion calls

This means that we have ereased 1907 checkings!

With this sudoku (listed as a difficult one):
..5.8....
..74.6...
.92....8.
..69...7.
..37485..
.4...23.
.6....95.
...6.34..
....9.8..

--Non-heuristic takes:
2433.790 ms to solve it
35078 recursion calls
--Heuristic takes:
786.927 ms
1478 recursion calls

Notice that these are almost 25 times LESS recursion calls for our heuristic sudoku solver!

Last in the priority of hardness, with this sudoku (listed as an "evil" one):
2.....458
8..4.7...
.5...1...
1.8..4.9.
.........
.9.7..8.4
...1...2.
...9.3..5
675.....9

--Non-heuristic takes:
37355.956 ms which are about 37 seconds to solve this one
and 341526 recursion calls.
--Heuristic solution takes:
1256.368 ms which is only 1'2 seconds
and 1297 recursion calls, which are about 300 times less calls.

'''
