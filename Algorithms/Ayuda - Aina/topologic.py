#Practica realitzada per Aina Ferra Marcus

import networkx as nx


'''
Complexity analysi:
Initially, looking up for the root element means that we have a cost of O(n^2). We have two iterative calls of nodes, it is a bit
lesser than n^2 because in some cases, when we call the "neighbors" method, we don't go through all the nodes in the list. So we
don't acomplish the n*n complexity.
On the other hand, the topologic algorythm takes O(n^2) because we have two iterative calls (again, calling neighbors, so it's a bit lesser than n^2).
The other iterative call is added, so it takes, aproximately O(2n^2) which is aproximated for O(n^2).
'''

def topologic(D):
    g = nx.read_adjlist(D, create_using=nx.DiGraph(), nodetype = int)
    
    nodes = g.nodes()
    #Getting the root.
    rootG = root(g)
    #We want to obtain the order of the tree. Root must be at the beginning, then
    #we can analyze the tree without watching over the root (since it's already visited)
    solution = [rootG]
    nodes.remove(rootG)
    #We want to know how long is our graph. That is, we will compare the length of the solution found with the length of our graph. 
    #Our solution must have the same number of elements as in the graph.
    #Therefore, means that we did something wrong.
    lenGraph = len(g)
    #Preparing our working extra attribute "already" to see if we already visited that node.
    startAlready(g)
    
    while len(solution) < lenGraph:
        #Starting algorythm.
        #We take a node and wath over their neighbors.
        #But if we already visited the node, then we shouldn't visit it again!
        for node in nodes:
            for elem in g.neighbors(node):
                if not g.node[elem]['already']: 
                    g.node[elem]['already'] = True
        #Then we must look over all nodes and check:
        for node in nodes:
            #if we already visited them, we do nothing.
            #But if they aren't visited, then we must put them in the list.
            #This checkng is necessary for non-connex components.
            #Once checked, we must remove them from the original graph so we don't repeat them.
            if not g.node[node]['already']:
                solution.append(node)
                nodes.remove(node)
                
    print solution
                
    
    
    
def root(g):
    lst = g.nodes()
    #We look over all nodes in our list.
    for i in g.nodes():
        #For every node, we visit its neighbors.
        for j in g.neighbors(i):
            #Neighbors are not the root of our graph so we "remove" them.
            #Putting a "-1" means removing them but without the cost of the function remove.
            #Moreover, we put a "-1" because we are working with formed int graphs, so -1 is not a computable value.
            try:
                #Finding out which position in the list of nodes is placed at.
                pos = lst.index(j)
                lst[pos] = -1
            except:
                pass
    #All elements but the root should be target as "-1".
    #The root is the only element which is not listed as a neighbour, since it's the start of the graph.
    for node in lst:
        if node != -1:
            #Root found, return it.
            return node
            
            
def startAlready(G):
    for  i in G.nodes():
        G.node[i]['already'] = False
        
topologic("dades.txt")