import time

#This is just for testing:
#n = 8

#This funcion gives all possible movements given a position of the matrix.
#This describes a Knight movement.
#Since we are just returning indexes, this funcion has cost o(1)
def givePossibilities(i, j):
    return [[i+2, j-1], [i+2, j+1], [i-2, j+1], [i-2, j-1], [i+1, j+2], [i+1, j-2], [i-1, j+2], [i-1, j-2]]

#So, given a determinated position in the matrix, the knight may not be able to go to all sorroundeing boxes.
#Why can this happen? Basically, if you are in a corner, you can't jump out of the chessboard.
#This function will check if we are trying to go out of the chessboard.
#Considering that we are just checking an information, this function has complexity o(1).
def satisfact(m, i, j):
    maxIndex = len(m) -1
    #This case flags the end of the chessboard
    if i > maxIndex or j > maxIndex or i < 0 or j < 0:
        return False
    #Else, we are going to a valid box:
    else:
        return True

'''
This is our recursive function that tries possibilities to go through the chessboard.
It implements a backtracking solution by bruteforce:
   -We look up at all possibilities we can go to.
   -Trying one of them.
   -Checking everytime that the way we are trying is correct.
   -If we can end, return a true.
   -If we face a way which we can't end, then return a false and try a new one.
   -If any of the possibilities could end, then return a false and say that the chessboard wasn't unsolvable.
   
But, this algorythm is by brute force. This means that it is poorly optimized. 
Assymptotically, it has O(n!) complexity, being n the size of the chessboard.
Why? Because these are all the possible ways we can do.
We will look at the time it takes to solve some sizes below.
'''
def knightTour(m, i, j, way):
    #If we are not going out of the chessboard.
    if satisfact(m, i, j):
        #if we are trying to go to an already crossed box:
        if m[i][j] == 0:
            #If the way we have done so far has its maximum length
            #this means that we have gone through all possible boxes.
            #Therefore, we could end our trip.
            #Sized could be solved!
            
            if len(way) == len(m[i])*len(m[i]):
                return True
            #Else, we are trying to go to an already crossed box
            #We can't repeat boxes, so return a False and try a new option:
            else:
                return False
        #If the box we are trying to go hasn't been visited:
        else:
            #Flag the box as visited:
            m[i][j] = 0
            #Add this pass to our way:
            way.append([i, j])
            
            #Now we have to move on. Procedure is: looking at options, choosing one, moving on.
            options = givePossibilities(i, j)
            for indexes in options:
                #This funcion returns "true" for valid solutions and "false" for invalid ones.
                #So, if a true is returned here, this means that the solution we are trying is correct.
                #we don't have the need to keep checking other possibilities, we already found a solution
                state = knightTour(m, indexes[0], indexes[1], way)
                if state:
                    return True
            ##Backtracking part:
            #If a true wasn't returned, then, we have to undo this step and try a new one:
            m[i][j] = -1 #This box can be visited again
            way.pop() #Don't go that way
            return False #Solution wasn't correct
    #If we are in this part of the "if" sentences, this means we are trying to go off the chessboard.
    #This is obviously incorrect, so return a False
    else:
        return False
        
    
def knightPas(n):
    #This will be our chessboard.
    #All positions flagged with -1 are valid.
    #We will put a 0 when box is already crossed.
    m = [[-1 for i in range(n)] for j in range (n)]
    
    #Starting first box, coordenate = (0,0)
    way = [[0,0]]
    m[0][0] = 0
    
    #Which ways can I go?
    #This is brute force, so it may give some out-of-the-chessboard ways
    options = givePossibilities(0, 0)
    #This will check the time it takes to solve a given dimension.
    t0 = time.clock()
    for indexes in options:
        #Our recursive function returns a True if the Knight has gone through all the board.
        #So, if a true is returned here, there's no need to check more possibilities.
        state = knightTour(m, indexes[0], indexes[1], way)
        if state:
            t1 = time.clock()
            print "I have gone this way", way
            print "It took me %0.3f ms to figure it out" %((t1-t0)*1000)
            #This return forces the function to end
            return
    #If we could make it out of the "for" sentences, this means that a true was never returned.
    #Therefore, the knight couldn't go through the chessboard.
    t1 = time.clock()
    print "Size asked is unsolvable"
    print "It took me %0.3f ms to figure it out" %((t1-t0)*1000)
    

            
def testingKnight():
    for i in range(1, 7):
        print "Size of the chessboard", i
        knightPas(i)

#testingKnight()

'''
This test gives us this result:
--Size 1:
I considered here that, since the knight isn't able to move, this size is unsolvable
time: 0'017 ms

--Size 2:
Unsolvable
time: 0'016 ms

--Size 3:
Unsolvable
time: 0'0328 ms

--Size 4:
Unsolvable
time: 52'951 ms

--Size 5:
Solvable. Possible way: [[0, 0], [2, 1], [4, 0], [3, 2], [1, 3], [3, 4], [4, 2], [3, 0], [1, 1], [0, 3], [2, 2], [0, 1], [2, 0], [4, 1], [3, 3], [1, 4], [0, 2], [1, 0], [3, 1], [4, 3], [2, 4], [1, 2], [0, 4], [2, 3], [4, 4]]
time: 159'881 ms (less than a second)

--Size 6:
Solvable. Possible way: [[0, 0], [2, 1], [4, 0], [5, 2], [3, 3], [5, 4], [3, 5], [1, 4], [2, 2], [4, 1], [2, 0], [0, 1], [1, 3], [0, 5], [2, 4], [4, 5], [5, 3], [3, 4], [5, 5], [4, 3], [5, 1], [3, 2], [4, 4], [2, 5], [0, 4], [1, 2], [3, 1], [5, 0], [4, 2], [3, 0], [1, 1], [0, 3], [1, 5], [2, 3], [0, 2], [1, 0]]
time = 3737'313 ms (3'7 seconds)

Extrapolating from here, it would take more than half an our to solve a 7x7 chessboard.
And it would take, probably, more than 2 days to solve a 8x8 chessboard.
'''

'''
So, as we have seen, this is a pretty bad algorythm. We could take less solving it by hand that with this algorythm.
Solution is ""simple"": let's introduce an heuristic.

Whan can we improve on this algorythm?
Order of checking / number of checkings.
In fact, if we give the checkings in "givePossibilities(i, j)" in a different ordre, we will notice a significant change in the time to solve the chessboard.
A possible heuristic consists in looking up which movements implies less options:
    --FOR EXAMPLE, moving arround corners implies less options to check (because probably, there will be 4 way we won't be able to go).
    --This erases some checkings and improves the algorythm.
    
Also, this is just a possible improvement. This is a well known studied algorythm with more optimum solutions that the one I'm trying to give here.
'''
##--------------------------Transformation routine
#Given routine:
def boxOfJump(jump):
    row = 1 + (jump - 1)/n
    col = 1 + (jump - 1)%n
    return row, col


##-----------------Anylizing possibilities.
def giveProperPossibilities(row, col, m):
    #we are in a given position of the chess (an integer number defining which box are we in)
    
    #So, as said before, let's see which ways we can go.
    options = givePossibilities(row, col)
    #We will put here our real possibilities:
    possibilities = []
    for op in options:
        #If the box is a valid one, id est, it is on the chessboard:
        if satisfact(m, op[0], op[1]):
            possibilities.append(op)
            
    return possibilities
  
##---------------------------------------------------  
##SMALL TEST          
def testingPossibilities():
    m = [[-1 for i in range(n)] for j in range (n)]
    print giveProperPossibilities(0, 0, m)
    
    print giveProperPossibilities(2, 4, m)
    
#testingPossibilities()
##----------------------------------------------------

'''
Since here, we see, through an example, that possibilities are different for position (0,0) that for position (2, 4).
Our heuristic will try to anticipate with which jumps can we minimize the number of possibilities.
'''
def knightPasHeuristic(n):
    m = [[-1 for i in range(n)] for j in range (n)]
    way = []
    
    #Starting at [0, 0], this doesn't change.
    m[0][0] = 0
    way.append([0, 0])
    
    t0 = time.clock()
    
    options = giveProperPossibilities(0, 0, m)
    starters = []
    
    for op in options:
        aux = giveProperPossibilities(op[0], op[1], m)
        starters.append([len(aux), op])
        
                   
    #This starters list defines which pass is better to start.
    #Which criteria do we use to define "better"?
    #The step that will result in less options.
    starters.sort()
    
    #Considering first the jumps that will cause less options to check, try the possible ways: 
    for pos in starters:
        state = knightTourHeuristic(m, pos[1][0], pos[1][1], way)
        #This is same as explained before in the brute force algorythm.
        if state:
            t1 = time.clock()
            print "I have gone this way", way
            print "It took me %0.3f ms to figure it out" %((t1-t0)*1000)
            return True
    t1 = time.clock()
    print "Size asked is unsolvable"
    print "It took me %0.3f ms to figure it out" %((t1-t0)*1000)
    
    
    
'''
This will be our improved recursive function.
As I said before, assymptotically speaking, complexity is O(n!)
But, in a midterm, this is way better. We are implementing here a way to "cross" branches in our recursive tree.
So, if we are looking in some problems in concret, statistically, we improved the efficiency.
'''
def knightTourHeuristic(m, i, j, way):
    #Notice that, since now we only give possibilities that are reachable, the satsfact function isn't called from here.
    #If the box we are trying to reach has already been visited and the way has its maximum length, we are done, return a true.
    if m[i][j]  == 0:
        if len(way) == len(m[i]) * len(m[i]):
            return True
        #If not, we were checking a bad way. Undo this step and try a new one.
        else:
            return False
    #If the box isn't visited, visit it and try its sorrounders.
    else:
        m[i][j] = 0
        way.append([i, j])
        
        #Same as done before:
        #First, check out which possibilities I can go to.
        options = giveProperPossibilities(i, j, m)
        starters = []
        
        #Then, calculate which of this possibilities will generate more or less posibilities at its time.
        #As said before, if jumping to a box will cause a checking of 8 cases
        #And jumping to another box will cause a checking of 2 cases, better take the 2 cases box.
        for op in options:
            aux = giveProperPossibilities(op[0], op[1], m)
            starters.append([len(aux), op])
        #Sorting using length of possibilities as key.   
        starters.sort() 
        
        #Considering the jumps which has less possibilities first, try the options.
        for pos in starters:
            state = knightTourHeuristic(m, pos[1][0], pos[1][1], way)
            #If a true was returned, then the way was already correct.
            if state:
                return True
        #If not, then this way is incorrect. Undo and try a new one.
        m[i][j] = -1
        way.pop()
        return False

            
    
def finalTesting():
    print "Size 8"
    knightPasHeuristic(8)
        
'''    
    for i in range(1, 7):
        print "---------------------------------------"
        print "Size asked is", i
        print "Without heuristic"
        knightPas(i)
        print "With heuristic"
        knightPasHeuristic(i)
        
'''        
    #print "Just with heuristic"
    #print "Size 7"
    #knightPasHeuristic(7)
    
finalTesting()


'''
A final compendium of all this information. First sizes are possible for both algorythm, obtaining:

---Size 1:
-Non Heuristic:
Result: Unsolvable
Time: 0'017 ms
-Heuristic:
Result: Unsolvable
Time: 0'020 ms

---Size 2:
-Non Heuristic:
Result: Unsolvable 
Time: 0'015 ms
-Heuristic:
Result: Unsolvable
Time: 0'017 ms

---Size 3:
-Non Heuristic:
Result: Unsolvable
Time: 0'321 ms
-Heuristic:
Result: Unsolvable
Time: 0'811 ms

---Size 4:
-Non Heuristic: 
Result: Unsolvable
Time: 52'990 ms
-Heuristic: 
Result: Unsolvable
Time: 177'551 ms

---Size 5:
-Non Heuristic: 
Result: Solvable.
Time: 157'428 ms
-Heuristic:
Result: Solvable
Time: 2'499 ms

(Ways are different since it checks in different order!!)

---Size 6:
-Non Heuristic:
Result: Solvable.
Time: 37320'611 ms
-Heuristic:
Result: Solvable
Time: 169'736 ms

(Ways are different!!)

For size 7, non-heuristic solution is not possible without spending too much time.
But heuristic solution takes only 10'065 ms to solve it.

For size 8, improvement is much better, heuristic solution takes only 975'532 ms to solve it.
'''
