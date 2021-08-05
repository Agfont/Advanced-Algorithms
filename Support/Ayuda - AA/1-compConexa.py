# coding: latin-1

import networkx as nx
from collections import deque

# Funcio principal a cridar

def components_connexes(G):
  n = G.number_of_nodes()
  H = [-1]*(n+1)
  c = 0
  for u in range(1,n+1):
    if H[u] == -1:
      c = c + 1
      exploracio(G, u, H, c)
  print "En total hi ha " + str(c) + " components connexes"
  print "Vector resultant " + str(H[1:n+1])

# Es presenten a continuacio dues formes 
# d'implementar l'exploracio. Totes dues
# son valides.

# Exploracio fent servir una funcio recursiva

def dfs(G,u,H,c):
  H[u] = c
  for v in G.neighbors(u):
    if (H[v] == -1):
      dfs(G,v,H,c)

# Una segona forma d'implementar l'exploracio
# es mitjancant cues. A la funcio principal
# cal canviar la crida a "dfs" per "exploracio"

def exploracio(G,u,H,c):
  H[u] = c
  cua = deque([ ])
  cua.append(u)
  while (len(cua) != 0):
      v = cua.pop()
      for neigh in G.neighbors(v):
          if H[neigh] == -1:
              H[neigh] = c
              cua.append(neigh)


