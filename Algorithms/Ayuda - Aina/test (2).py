def parse_sudoku(nombre_fichero):
    matriz = [[0]*9 for v in range(9)]
    fichero = open(nombre_fichero, "r")
    
    lineas_fichero = fichero.readlines()
    
    for line in range(0, len(lineas_fichero)):
        for elem in range (0, len(lineas_fichero)):
            if lineas_fichero[line][elem] != "\n" and  lineas_fichero[line][elem] != ".":
                matriz[line][elem] = int(lineas_fichero[line][elem])
            
            
            
    #print matriz
    return matriz

def transformMatrix(matrix):
    finalMatrix = [[[[-1 for k in range(3) ] for i in range (3)] for v in range (3)] for j in range (3)]
    #print finalMatrix
    for k in range(3):
        for i in range(3):
            for v in range(3):
                for j in range(3):
                    finalMatrix[k][v][i][j] = matrix[k*3+i][v*3+j]
    return finalMatrix

def satisfact(m):
    for k in range (0, 3):
        for i in range (0, 3):
            auxRows = []
            auxCols = []
            auxBlocks = []
            for v in range (0, 3):
                for j in range (0, 3):
                    if (m[k][v][i][j] not in auxRows  or m[k][v][i][j] == 0) and (m[v][k][j][i] not in auxCols  or m[v][k][j][i] == 0) and (m[k][i][v][j] not in auxBlocks or m[k][i][v][j] == 0):
                        auxRows.append(m[k][v][i][j])
                        auxCols.append(m[v][k][j][i])
                        auxBlocks.append(m[k][i][v][j])
                    else:
                        #print "Invalid sudoku"
                        return False
    #print "Success"
    return True               
    
def satisfactNormal(m):
    for i in range (9):
        auxRows = []
        auxCols = []
        for j in range(9):
            if (m[i][j] == 0 or m[i][j] not in auxRows) and (m[j][i] == 0 or m[j][i] not in auxCols):
                auxRows.append(m[i][j])
                auxCols.append(m[j][i])
            else:
                return False
            
            
    for v in range(0, 9, 3):
        auxBlocks = []
        for k in range(3):
            if (m[v][k] == 0 or m[v][k] not in auxBlocks) and (m[v+1][k] == 0 or m[v+1][k] not in auxBlocks) and (m[v+2][k] == 0 or m[v+2][k] not in auxBlocks):
                auxBlocks.append(m[v][k])
                auxBlocks.append(m[v+1][k])
                auxBlocks.append(m[v+2][k])
            else:
                return False
            
    return True
                
def solveBruteForce(m):
    if satisfactNormal(m) == True:
        print "Solving sudoku"
        i, j = findFirstGap(m)
        for k in range(1, 10):
            fillSudokuBruteForce(m, i, j, k)
        print m
    else:
        print "Initial sudoku is incorrect"

def fillSudokuBruteForce(m, i, j, t):
    #Solution without using any heuristic.
    #This means we will try out EVERY possible combination.
    #We won't look up if in the same row, col or block there's the number we are checking.
    
    #First condition, wanted-to-fill box must be empty:
    if m[i][j] == 0:
        #If the box is empty, try the value
        m[i][j] = t
        if satisfactNormal(m):    
            #We know that when i == 8 and j == 8 we are done with our solution.
            if i == 8 and j == 8:
                #done
                return
            #Another special condition:
            #If col == 8, this means we have to pass up to another row.
            elif j == 8 and i != 8:
                i += 1
                j = 0
                #If col != 8 and row != 8, this means we can go through the sudoku normally:
            else:
                j += 1
            
                #Proceed to try out a solution with the next empty box:
                for k in range (1, 10):
                    fillSudokuBruteForce(m, i, j, k)
                return    
        else:
            #If we get here, that means that the given solution is not valid
            #We must "backtrack" to the last solution.
            m[i][j] = 0
            return
    #If the box isn't empty, then we must go to the next empty box.    
    else:
        i, j = findFirstGap(m)
        if i != -1 and j != -1:
            for k in range (1, 10):
                fillSudokuBruteForce(m, i, j, k)
            return
        else:
            return


def findFirstGap(m):
    for i in range (9):
        for j in range (9):
            if m[i][j] == 0:
                return i, j
    i, j = -1, -1
    return i, j











##test([[[[4, 0, 0], [7, 0, 1], [0, 2, 3]], [[0, 5, 0], [0, 2, 0], [8, 0, 0]], [[0, 0, 1], [0, 8, 0], [0, 0, 0]]], [[[9, 0, 7],[0, 3, 0], [2, 0, 6]], [[0, 8, 0], [0, 0, 0], [0, 4, 0]], [[5, 0, 2], [0, 4, 0], [9, 0, 3]]], [[[0, 0, 0], [0, 0, 9], [1, 0, 0]], [[0, 0, 6], [1, 0, 3], [0, 9, 0]], [[2, 1, 0], [4, 0, 8], [0, 0, 6]]]] )

solveBruteForce((parse_sudoku("sudoku2.txt")))