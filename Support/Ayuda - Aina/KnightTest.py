import time

def givePossibilities(i, j):
    return [[i+2, j-1],[i+2, j+1], [i+1, j+2], [i+1, j-2], [i-2, j+1], [i-2, j-1], [i-1, j+2], [i-1, j-2]]


def giveBetterPossibilities(i, j):
    pass

def satisfact(m, i, j):
    maxIndex = len(m)-1
    if i > maxIndex or j > maxIndex or i < 0 or j < 0:
        return False
    else:
        return True

def knightPass():
    #n = input("Size of chessboard: \n")
    n = 7
    m = [[-1 for i in range(n)] for j in range(n)]

    print "Testing solution"
    
    #Starting conditions, we start at the begining of the chessboard.
    way = [[0, 0]]
    m[0][0] = 0
    
    options = givePossibilities(0, 0)
    t0 = time.clock()
    for indexes in options:
        state = knightTour(m, indexes[0], indexes[1], way)
        if state:
            t1 = time.clock()
            print "The knight has gone this way: "
            print way
            print "It took %0.3f ms" %((t1-t0)*1000)
            return
    print "Sized asked is unsolvable"
    
def knightTour(m, i, j, way):
    #If the indexes are reachable:
    if satisfact(m, i, j):
        #If the box is already visited
        if m[i][j] == 0:
            #And we already have all elements:
            if len(way) == len(m[i])*len(m[i]):
                #We are done
                return True
            #If we don't have all the elements, this solution is just incorrect
            else:
                return False
        #Box wasn't visited, we can flag it.
        else:
            m[i][j] = 0
            way.append([i, j])
            #Obtain the next box
            options = givePossibilities(i, j)
            for indexes in options:
                state = knightTour(m, indexes[0], indexes[1], way)
                if state:
                    return True
            m[i][j] = -1
            way.pop()
            return False
    else:
        return False
    
    
knightPass()