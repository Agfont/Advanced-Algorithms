  
# Mirem si un node esta lliure 

def node_lliure(k, v):  #---- OK -----
  return not v[k]

# Calculem el cost d'assignacio entre nodes
# no cal comprovar si els nodes estan lliures
# perque nomes s'executa al final, es a dir,
# quan ja tenim un vector assignat.

def cost_assignacio(x):  # ----- OK -----
  global N, M
  cost = 0
  k = 0
  while k < N-1:
    cost += M[x[k]][x[k+1]]
    k += 1
  cost += M[x[k]][x[0]]
  return cost

# Anem a aproximar el cost minim d'assignacio.
# Amb un algorisme vorac obtindrem una fita
# superior del cost que estem buscant

def heuristica():
  global min_x, min_z
  min_x = [0, 1, 2, 3, 4]
  min_z = cost_assignacio(min_x)

# Cerca exhaustiva
# variable i: index del projecte a assignar a alguna empresa
# variable x: assignacio actual d'empreses amb projectes.
#             x[k] indica el projecte que hem assignat a l'empresa k
# variable z: cost de l'assignacio actual d'empreses 

def exhaustiu(i, x, v):
  global min_z, min_x, N, total_crides
  # Mirem si ja hem assignat tots els projectes
  # i comprovem si el cost de l'assignacio que
  # tenim es inferior al que tenim actualment.
  s = ""
  for k in range(i+1):
     s = s + "   "

  if (i == N):
    z = cost_assignacio(x)
    if (min_z > z): 
      min_x = x[:]
      min_z = z
      print s + "---> Solucio", min_x, "amb cost", min_z 
    return

  for k in range(1, N):
     if (node_lliure(k, v)):
        q = x[:]
        q[i] = k   #insertem el node lliure a la posicio i
        w = v[:]
        w[k] = True
        print s + "Entro ", q
        total_crides = total_crides + 1
        exhaustiu(i+1, q, w)
        print s + "Surto ", q

def main():
   global M, N, M_, min_z, min_x, v, total_crides
   M = [[0, 2, 3, 4, 5],[2, 0, 60, 7, 8],[3, 60, 0, 9, 100],[4, 7, 9, 0, 11],[5, 8, 100, 11, 0]]
   N  = len(M)
   v = [False for i in range (N)]
   # Fem un calcul vorac
   heuristica()
   # Indicarem amb -1 que la empresa esta lliure
   x = [-1 for i in range(N)]
   x[0] = 0   #node 1
   v[0] = True
   total_crides = 1
   # Iniciem la crida recursiva
   exhaustiu(1, x, v)
   print "L'assignacio final es ", min_x, "i te cost", min_z
   print "En total hem fet", total_crides, "crides a la funcio branch_and_bound"

main()
