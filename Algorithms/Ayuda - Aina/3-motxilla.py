
'''
We have a simple loop iterating for every item in the list.
That would make a O(n) complexity. 
We try to put one item as many times as possible, so the while inside de primary loop
adds a constant k to our complexity, so it would be O(k*n) average.
Since we sort the elements, this would be, at least, O(nlog(n)).
O(nlog(n) + k*n) = O(nlog(n))
If the items were already  sorted, then the algorythm would take only O(k*n) = O (n)
which is a lineal complexity.

------------Is it optimum?
It offers a pretty accurate solution for lots of situations, but it isn't the optimum solution.
Considering a list of elements
weight = [2, 3], value = [4, 5] => ratio = [2, 1'6]
limit of weight = 3
Our algorythm would give the solution "item of weight 2 and value 4" when the optimum solution is 
"item of weight 3 and value 5". 
'''
def mochila(limit, lstValues, lstWeight):
    #We will build a list with value/weight density.
    ratio = []
    for i in range(0, len(lstValues)):
        ratio.append([float((lstValues[i]/lstWeight[i])),lstWeight[i]])
    
    #Sorting them is O(n * logn). Reverse = true because we want the greater to be ahead. 
    ratio.sort(reverse = True)
    
    #We haven't added any items yet.
    filled = 0
    #We will put here our backpack items. 
    backpack = []
    #We have to check for every ratio if we can put an item to the backpack. 
    for i in range (0, len(ratio)):
        #Moreover, we have to check if we can put more than one single item to our backpack. 
        while ratio[i][1] + filled <= limit:
            backpack.append(ratio[i])
            filled += ratio[i][1]
                
    #Printing the items in the backpack. 
    for i in range (0, len(backpack)):
        print "Item of weight", backpack[i][1], "and value", backpack[i][0]*backpack[i][1]
        

mochila(97, [200, 60, 10], [50, 20, 10])
        
                
            
            
    
        
        