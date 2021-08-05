import time

#-----------------------Dinamic programming: backpack's problem:
'''
This parser accepts files with 2 cols separated by a space.
First col is for weight, then a space, then second col is for value.
If the file isn't of this kind, it will return an error.
Since it reads every object once, complexity is O(n), being n number of objects
'''
def parseObjects(fileName):
    lstWeight = []
    lstValues = []
    
    fi = open(fileName, "r")
    lines = fi.readlines()
    
    for line in lines:
        lstWeight.append(int(line[0]))
        lstValues.append(int(line[2]))
        
    return lstWeight, lstValues
        
'''
This is our primary algorythm. It gives the maximum value we can get given a maximum weight and a list of items.
Complexity is O(n^2). There's a third nested loop, but it depends of i, which is the item we are iterating with.
Generally, the number of items will be way lesser than our maximum weight. So, in a midterm, this third nested loop
tends to be way less than the two principal ones.
This could be fixed with another loop (not nested on the second one, but on the first one) if we filled the matrix
in cols (filling first maximum weight 1, then maximum weight 2...) instead of filling it by rows (looking how many objects
of kind 1 we can put in all maximum weights, then how many objects of kind 2...).

As explained below, our subproblems will be, at anytime, to fill the cell in the matrix with the higher value possible
fitting always the restriccion of weight.
'''
def dinamicBackpack(maxWeight, lstWeight, lstValues):    
    #We are doing here a similar process as done in Levenstein's algorythm.
    #We form a matrix where we put in every cell the combination that gives us the higher value
    #given a maximum weight. Those will be our "subproblems" to solve in every loop of the algorythm.
    
    #We need two things: a matrix to control value and a matrix to control how many objects do we put in.
    #Controlling value is easier and we just want the last information, so we will work with a simple list
    #and we will keep modifying it as necessary.
    rowMatrix = [0]*(maxWeight + 1)
    #On the other hand, knowing which item have we pulled in is more difficult. So we will need here the matrix.
    #Information is read as:
    #Every row represents a kind of item (id est: item of value 10 and weight 2)
    #Every col represents a maximum weight.
    #Every cell (i, j) represents how many items of kind "i" do we put for the maximum weight "j" 
    addingObjects = [[ 0 for i in range(maxWeight+1)] for j in range (len(lstValues))]

    #Looking for every item:
    for i in range(0, len(lstValues)):
        #Checking for every maximum weight:
        for j in range(0, (maxWeight + 1)):
            
            #First of all, we have to see if this item can be placed given the maximum weight.
            #Id est, if the item weights 3 and our maximum weight is 1, we can't use this one. 
            if j - lstWeight[i] >= 0:
                #left flags the weight that can still be filled.
                #We want for every maximum weight to complete it, if possible.
                #So if we have a maximum weight of 3 and we put an item that wieghts 2, we can still put
                #An item that weighs 1.
                left = j - lstWeight[i]
                #For every weight we will look:
                #If we can put an item with a given weight and its value plus the value of what's left is greater
                #Than what we already had in the matrix, we modify the matrix.
                #This procedure of modifying a matrix is way alike the one in Levenstein's or DTW.
                #We can observe here how do we solve our subproblems: 
                #trying to ensure here that we have the higher value possible. 
                if lstValues[i] + rowMatrix[left] > rowMatrix[j]:
                    rowMatrix[j] = lstValues[i] + rowMatrix[left]
                    #i is the item we are checking.
                    #j is the maximum given weight.
                    #This loop copies all objets we have put in since now
                    #refreshing for our "left" value.
                    for k in range(0, i):
                        addingObjects[k][j] = addingObjects[k][left]
                    #Now, we add the object that we previously saw that was better. 
                    addingObjects[i][j] = addingObjects[i][left] + 1
                    
    print "For our maximum weight of", maxWeight, "we can get a value of", rowMatrix[maxWeight]
    print "Added objects are:"
    counter = 0
    for i in addingObjects:
        print i[maxWeight], "object(s) with size", lstWeight[counter], "and value", lstValues[counter]
        counter += 1
 
'''
Testbench of our funcion. Some examples are given here. 
'''   
def testDinamicBackpack():
    
    ##Parser test. I will put below some tests without using the parser, in case the file is corrupt or something
    ##in order to test more options.
    lstWeight, lstValues = parseObjects("backpack.txt")
    dinamicBackpack(7, lstWeight, lstValues)
    print "------------------------------- \n"
    print "Another example: "
    dinamicBackpack(5, [4, 1, 3], [1, 5, 2])
    print "------------------------------- \n"
    print "Another example: "
    dinamicBackpack(100, [5, 7, 1, 9, 1], [40, 2, 20, 90, 15])
    
testDinamicBackpack()





