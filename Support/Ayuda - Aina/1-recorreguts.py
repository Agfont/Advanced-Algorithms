import networkx as nx

'''
Function that tells us how many isolated nodes there are in a given graph g.
Complexity is a linear, we only see each node once (and for each node, we count its neighbors
but we don't visit them). So O(n), where n are the number of nodes. 
'''
def isolated(G):
    isolated = 0
    l = G.nodes()
    
    for node in l:
        if G.neighbors(node) == []:
            isolated += 1
            
    print "We have: ", isolated, "isolated nodes. \n"
    
    
'''
This is the "depth-first-search" called algorythim. Goes through a graph
recursively. Complexity is O(n) where n is the number of edges we have. 
'''
def DFS(G):
    #So, in order not to make extra list, I put a flag here called visited.
    #Function is declared below. 
    startVisited(G)
    print "DFS NODES: \n"
    for i in G.nodes():
        #If the node isn't visited yet, visit it.
        #Everytime this function is called from up here, a new connex component is spotted out.
        if G.node[i]['visited'] == False:
            explore(i, G)
            
    print "---------------END OF DFS NODES \n"
            
def explore(v, G):
    #Point that the node is visited. 
    G.node[v]['visited'] = True
    print v
    #Visit their neighbors.
    #It uses stack technics. 
    for k in G.neighbors(v):
        if  G.node[k]['visited'] == False :
            explore(k, G)

'''
This is our "breadth-first-search" algorythm. Using queue technics we
go through a graph looking everytime for all neighbours before passing to
a next level. Complexity is lineal, O(n) where n is the number of nodes. 
'''
def BFS(G):
    #Auxiliar function in order not to create auxiliar lists.
    print "BFS NODES: \n"
    startDistances(G)
    #First element is the "root" of our graph. 
    #This list acts as our queue. 
    Q = [G.nodes()[0]]
    G.node[G.nodes()[0]]['dist'] = 0
    while Q != []:
        #Taking out the first element. 
        v = Q.pop(0)
        print v
        #If their neighbors aren't visited yet, visit them: 
        #Refresh distances. 
        for node in G.neighbors(v):
            if G.node[node]['dist'] == -1:
                Q.append(node)
                G.node[node]['dist'] = 1
                
    print "-----------------------END OF BFS NODES \n"
                

def startVisited(G):
    for i in G.nodes():
        G.node[i]['visited'] = False
        
def startDistances(G):
    for i in G.nodes():
        G.node[i]['dist'] = -1


''''
Function that builds a test graph
'''
def graph():
    G = nx.Graph()
    
    G.add_edge(1,2)
    G.add_edge(1,6)
    G.add_edge(1,3)
    G.add_edge(3,8)
    G.add_edge(3,6)
    G.add_edge(2,3)
    G.add_edge(6,2)
    G.add_edge(2,4)
    G.add_edge(3,4)
    G.add_edge(3,5)
    G.add_edge(4,5)
    G.add_edge(2,5)
    G.add_edge(4,7)
    
    return G
    
    
    
isolated(graph())
DFS(graph())
BFS(graph())