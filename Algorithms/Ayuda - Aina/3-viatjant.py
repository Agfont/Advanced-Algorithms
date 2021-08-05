import networkx as nx

'''
Since we are working with complete graphs, looking up for the neighbors of a node means looking
up for every other node on the graph.
That means that we have two implicit loops here. Complexity increases to O(n^2).
It may be a bit lesser, but worst case is O(n^2)


-----------Is it optimum?
No, it isn't. Although, on average, it gives the path only a 25% larger than it really is, it isn't optimum.
For instance, considering the graph given below (the one on comments), it says that the optimum route takes 29km
when not choosing the greedy path would give us a 9km route. 
'''
def viatjant(G):
    #There's a precondition for the algorythm to work.
    #We are assuming that it's a complete graph, that means that it is always possible
    #to complete the route, no matter if it's optimum or not. 
    
    
    #Turning all cities to unvisited.
    startVisited(G)
    #Obtaining travelled path and last city visited.
    lstVisited, lastCity  = iterateCities(G)
    #This is not necessary, but interesant for informative purposes. 
    costPath = 0
    
    #We ended up in the last city, but now we must go back to our first city:
    #We have to point out the distance between the last city and our first city.
    lstVisited[len(lstVisited)-1][1] = G.edge[G.nodes()[0]][lastCity]['weight']

    #print lstVisited
    print "Starting with node", lstVisited[0][0]
    for i in range(0, len(lstVisited)-1):
        print "Going through node: ", lstVisited[i+1][0]
        print "It took us: ", lstVisited[i][1]
        costPath += lstVisited[i][1]
    
    print "Reaching node: ", lstVisited[0][0]
    print "It took us: ", lstVisited[len(lstVisited)-1][1]
    costPath += lstVisited[len(lstVisited)-1][1]
    print "It costed us a total of", costPath, "km to complete the route"
    
   

#Algorythm to find the way:   
def iterateCities(G):
    #We will put here all the visited nodes.
    lstVisited = []
    

    #Iterable node that wi will be changing further on.
    #First iterable node is the starting one.
    iterable = G.nodes()[0]
    G.node[G.nodes()[0]]['visited'] = True
    #While there's still unvisited nodes:
    while len(lstVisited) < len(G.nodes()):
        #The city we just visited is our "father" city.
        father = iterable
        #Look up for the nearest neighbor city.
        #We also obtain the path-value between our just visited city and our nearest city.
        #This is for informative purposes, not really necessary for the algorythm.
        iterable, value = obtainNearestCity(G, iterable)
        #Father city and value are put in the list.
        #Father variable is used here because iterable changes at the same time as we obtain value.
        #Since I want to put the city and its value together, I used this auxiliar variable named father. 
        lstVisited.append([father, value])
        #If we couldn't find other cities but the same we are in, then we are done.
        if iterable == father:
            return lstVisited, iterable 
            
  
def startVisited(G):
    for i in G.nodes():
        G.node[i]['visited'] = False
 
'''
This auxiliar function finds the minimum edge we can go to.
We look up for the unvisited neighbors (we can't visit a city twice) and gets the 
nearest city. That's the centre of the greedy algorythm. 
'''
def obtainNearestCity(G, node):
    #Neighbors of this node. 
    lstNeighbors = G.neighbors(node)
    minimumValue = 1000000000
    #This is a checking method. If all other nodes are visited, then we will return the same node we starte with. 
    nearestCity = node
    for i in lstNeighbors:
        #Condition to come up to this city:
        #Minimum cost, not visited city
        if (minimumValue > G.edge[i][node]['weight'] and G.node[i]['visited'] == False):
            minimumValue = G.edge[i][node]['weight']
            nearestCity = G.nodes()[i]
    #We visited a node here, point it true.         
    G.node[nearestCity]['visited'] = True
    #returning the nearestcity and its cost.
    return nearestCity, minimumValue

'''
This function is important since we build the sized-edges here.
We are assuming that the list has the same length as the number of edges.
This is not a general algorythm for building graphs, it builds a concrete one.
'''
def graph(lstvalues):
    
    G = nx.Graph()
    
    G.add_edge(0, 1, weight = lstvalues[0])
    G.add_edge(0, 2, weight = lstvalues[1])
    G.add_edge(0, 3, weight = lstvalues[2])
    G.add_edge(1, 2, weight = lstvalues[3])
    G.add_edge(1, 3, weight = lstvalues[4])
    G.add_edge(2, 3, weight = lstvalues[5])
    
    return G
    
        
viatjant(graph([1, 2, 7, 4, 5, 1]))
#viatjant(graph([1, 2, 23, 4, 5, 1]))