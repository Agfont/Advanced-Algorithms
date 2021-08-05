import copy

def parseMatrix(fileName):
    pass

ma = [[11, 12, 18, 40], [14, 15, 13, 22], [11, 17, 19, 23], [17, 14, 20, 28]]
#ma = [[1, 13, 3, 18], [3, 5, 9, 20], [5, 10, 2, 17], [7, 2, 10, 21]]

#Function that obtains the upper bound given a matrix of values.
def obtainBounds(m):
    upperBoundB = 0
    dim = len(m)
    for i in range(dim):
        upperBoundF += m[i][i]
    
    return upperBoundF


#Function that assigns a product with a company.
#In this case, we mark this ""crossing"" the rows and cols of product and company.
#Id est, we mark them as False (we can't use them anymore)
#leftOver is our matrix of booleans, that gives us information about the free products and companies lefts
def assignProduct(leftOver, i, j):
    dim = len(leftOver) 
    for v in range (dim):
        leftOver[i][v] = False
        leftOver[v][j] = False
                

#This function returns the possible matchings given a company.
#Uses the leftOver matrix
def possibleMatchings(leftOver, wanted):
    dim = len(leftOver)
    possibilities = []
    for i in range(dim):
        for j in range(dim):
            if i == wanted and leftOver[i][j]:
                possibilities.append([i, j])
                
    return possibilities

#This function recalculates the lowerBounds given a matrix.
#We have to know that some companies will have their product assigned.
#Calculates the minimum value possible having some other values predeterminated.
def recalculateBound(patron, left, way):
    lowerBound = 0
    dim = len(patron)
    aux = 0
    
    #Values that we already have assigned. 
    for indexes in way:
        lowerBound += patron[indexes[0]][indexes[1]]
        
    
    #Looking for the minimum value possible (minimum has to iterate for rows)
    for j in range (dim):
        minimum = float("inf")
        for i in range (dim):
            if patron[i][j] < minimum and left[i][j]:
                minimum = patron[i][j]
        if minimum < float("inf"):
            aux += minimum
    
    #LowerBound is: products we already assigned + minimum value left
    return (aux + lowerBound)

#Undoing the assignament done before.
def undoAssignment(leftOver, way):
    dim = len(leftOver)
    
    #Redoing the matrix of booleans.
    leftOver = [[True for i in range (dim)] for j in range(dim)]
    
    #Just mark whatever we have on our way. The rest are still Trues. 
    for v in way:
        assignProduct(leftOver, v[0], v[1])
     
    #Returning this matrix, because we didn't work with pointers here.  
    return leftOver                   
 
#Principal function that will call our recursive one.        
def matching(m):
    
    ##Inicialitzations:
    dim = len(m)
    upperBound = obtainBounds(m)
    leftOver = [[True for v in range (dim)] for k in range (dim)]
    options = possibleMatchings(leftOver, 0)
    #We will look where is better to start in starters. 
    starters = []
    #Way that we do and undo, and optimum way:
    way = []
    opt = []
    #If we don't find any better bounds, then the initial bound is the best way to solve the problem.
    #Since our first bound is the diagonal, that will be our optimum initial way. 
    for i in range (dim):
        opt.append([i, i])
  
    for indexes in options:
        #Try this way:
        way.append(indexes)
        #Assign this option
        assignProduct(leftOver, indexes[0], indexes[1])
        #Recalculate this bound
        lower = recalculateBound(m, leftOver, way)
        #Store information
        starters.append([lower, indexes[1]])
        #Undo assignment
        way.pop()
        leftOver = undoAssignment(leftOver, way)
        #Undo way
    starters.sort()
    
    #Now starters is sorted knowing [[bownd, product], ...]
    #We will start for elements whose bound is lower
    #Also, if this bound is greater than the upperBound, we don't even look at it.
    for indexes in starters:
        if indexes[0] < upperBound:
            #Trying this possible branch:
            assignProduct(leftOver, 0, indexes[1])
            way.append([0, indexes[1]])
            #Recursive function returns a value (cost of assigning this products) and the optimum way.
            lower, opt = tryBestMatching(m, leftOver, 1, upperBound, way, opt)
            #If the value is lower than our upperBound, make this our new upperBound.
            if lower < upperBound:
                upperBound = lower
            #Undo assignments and way to try other ways:
            way.pop()
            leftOver = undoAssignment(leftOver, way)
            
    print opt, upperBound
        

#Recursive function:    
def tryBestMatching(m, left, i, UB, way, opt):
    #If way has its maximum length this means that we have ended our assingments.
    if i == (len(m) -1):
        #Assign last product
        assignation = possibleMatchings(left, i)
        assignProduct(left, i, assignation[0][1])
        #Append that to the way
        way.append(assignation[0])
        #Calculate the cost of this way
        lower = recalculateBound(m, left, way)

        #If the cost is lesser than the upperBound, then this is our newest upper bound.
        #This will be our optimum way.
        if lower < UB:
            #This is because of pointers problems =(
            aux = copy.deepcopy(way)
            way.pop()
            return lower, aux
        #If not, return what we already had.
        else:
            way.pop()
            return UB, opt
    
    #If not, we can still match things. Do as explained before:
    #see which matchings we can do and start for the best:
    options = possibleMatchings(left, i)
    possibilities = []
    for option in options:
        way.append(option)
        assignProduct(left, i, option[1])
        lower = recalculateBound(m, left, way)
        possibilities.append([lower, option[1]])
        way.pop()
        left = undoAssignment(left, way)
  
    possibilities.sort()

    for possibility in possibilities:
        if possibility[0] < UB:
            assignProduct(left, i, possibility[1])
            way.append([i, possibility[1]])
            upper, opt = tryBestMatching(m, left, i+1, UB, way, opt)
            #If the cost returned is lesser than the upperBound, this becomes our upperBound
            if upper < UB:
                UB = upper
            #Undo to try new branches:
            way.pop()
            left = undoAssignment(left, way)            
    
    return UB, opt

matching(ma)