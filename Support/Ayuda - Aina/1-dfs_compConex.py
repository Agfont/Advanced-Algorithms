import networkx as nx
#import matplotlib.pyplot as plt

'''
Example graph.
This should have an articulation point
'''

def graph():
    G = nx.Graph()
    G.add_edge(1, 2)
    G.add_edge(1, 3)
    G.add_edge(2, 3)
    G.add_edge(3, 4)
    G.add_edge(3, 5)
    G.add_edge(4, 5)
    
    return G
'''
For an easily check, just draw the grahp
I let this in comments just in case the draw library isn't installed.
Also it isn't really necessary. Just for informative purposes. 

def draw(G):
    nx.draw(G)
    plt.show()
'''


'''
DFS method
'''
def DFS(G):
    #This is our connex components counter. 
    connexes = 0
    startVisited(G)
    for i in G.nodes():
        if G.node[i]['visited'] == False:
            #Everytime we call a new connex component, add it. 
            connexes += 1
            explore(i, G)
    return connexes
            
def explore(v, G):
    G.node[v]['visited'] = True
    for u in G.neighbors(v):
        if not G.node[u]['visited']:
            explore(u, G)
        
def startVisited(G):
    for i in G.nodes():
        G.node[i]['visited'] = False
        
'''
Let's see what do we do here. 
We go with DFS through node -> that takes n complexity.
Then we go through every node and go with DFS again.
That's, in the worst case, O(n^2).
If we find a connex component before completing the loop, then complexity is reduced.
But guessing the worst case, it will take two loops to complete the algorythm.
O(n + n^2) = O(n^2) complexity. 
'''
def articulacio(G, g):
    #The idea here is: everytime the outter loop of the DFS is called, means
    #we have another connex component.
    #So we modified the DFS algorythm to count out how many connex components we have.
    inicial = DFS(G)
    
    #We will go through the graph removing each node and checking out if the number
    #of connex component has increased. 
    for i in G.nodes():
        G.remove_node(i)
        final = DFS(G)
        #If at least one time the number increased, then we can end
        #We ensure that AT LEAST we have one connex component. 
        if final > inicial:
            print "There's, at least, one connex component. "
            return
        #Else, we return to our initial graph and remove another node
        #We keep searching. 
        else:
            G = g
    #If we ever get to this point, this means that we didn't found a situation
    #Where the number of connex component increased.
    #Basically, we didn't found any connex component. 
    #End of algorythm. 
    print "There aren't any connex component"

articulacio(graph(), graph())     
        