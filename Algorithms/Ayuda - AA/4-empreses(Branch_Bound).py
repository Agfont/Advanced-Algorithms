# Calculem una fita a partir de les empreses
# que ja han estat assignades a projectes.
# Veure tambe fita2
#
# variable x: assignacio actual d'empreses amb projectes

def fita2(x,v):
  # Calculem primer la fita ignorant nodes
  z1_ = 0
  l  = len(x)
  # La matriu p emmagatzema els projectes que estan
  # lliures. Si el node k no esta lliure, x[k] indica
  # el projecte que li hem assignat. p[k] es True si
  # el projecte esta lliure, False si esta assignat a
  # alguna node.
  p  = [True for k in range(l)]
  for k in range(l):
     if not node_lliure(k, v):
        p[v[k]] = False
  # Calculem la fita ignorant nodes. Es a dir,
  # busquem els projectes lliures i li assignem
  # el cost del node que el fa mes economic.
  # Cal fer un minim per columnes. 
  for k in range(l):
     if p[k]:
       # NOTA: busquem la primera node no assignada
       # a un projecte
       j = 0
       while not node_lliure(j, x):
         j = j + 1
       # NOTA: li assignem el minim
       min_c = M[j][k]
       # NOTA: Ara busquem entre la resta d'empreses
       # no assignades de la mateixa columna
       j = j + 1
       while j < l:
          if not node_lliure(j, v):
             min_c = min(min_c, M[j][k])
          j = j + 1
       z1_ = z1_ + min_c
  # Ara calculem la fita ignorant projectes. Busquem
  # les empreses lliures i li assignem el cost del
  # projecte mes economic. 
  z2_ = 0
  for k in range(l):
     if node_lliure(k, v):
        # NOTA: busquem el primer projecte lliure
        # de l'node k
        j = 0
        while not p[j]:
           j = j + 1
        # NOTA: li assignem el minim
        min_c = M[k][j]
        j = j + 1
        # NOTA: Ara busquem entre la resta de projectes
        # de la mateixa node, pero nomes entre els
        # projectes no assignats.
        while j < l:
           if not p[j]:
              min_c = min(min_c, M[k][j])
           j = j + 1
        z2_ = z2_ + min_c
  return max(z1_, z2_)

# Aquesta funcio retorna True si la node k esta lliure
#
# variable k: node per la qual volem saber si esta lliure
# variable x: vector on tenim associades empreses amb projectes

def node_lliure(k, v):
  return not v[k]

def cost_assignacio(x):  
  global N, M
  cost = 0 
  k = 0 
  while k < N-1 and x[k+1] != -1:
    print M[x[k]][x[k+1]],
    cost += M[x[k]][x[k+1]] 
    k += 1 
  cost += M[x[k]][x[0]]
  print cost
  return cost

# Anem a aproximar el cost minim d'assignacio
# Amb un algorisme heuristica obtindrem una fita
# superior del cost que estem buscant

def heuristica():
  global min_x, min_z,N
  min_x = [i for i in range(N)]
  min_z = cost_assignacio(min_x)

# Cerca per branch and bound (es la funcio exhaustiu dels exemples
# anteriors)
#
# variable i: index del projecte a assignar a alguna node
# variable x: assignacio actual d'empreses amb projectes.
#             x[k] indica el projecte que hem assignat a l'node k
# variable z: cost de l'assignacio d'empreses amb projectes que hem fet

def branch_and_bound(i, x, z,v):
  global min_z, min_x, N, total_crides
  # Creem una cadena de caracters en blanc
  # per imprimir de forma bonica per pantalla
  s = ""
  for k in range(i+1):
     s = s + "   "
  # Mirem si ja hem assignat tots els projectes
  # i comprovem si el cost de l'assignacio que
  # tenim es inferior al que tenim actualment.
  if (i == N) and (min_z > z): 
     min_x = x[:]
     min_z = z 
     print s + "---> Solucio", min_x, "amb cost", min_z 
     return
  # Analitzem les empreses lliures i els 
  # assignem el projecte i
  for k in range(1, N):
     if (node_lliure(k, v)):
        # La node k esta lliure i li assigno
        # el projecte i.
        q = x[:]
        q[i] = k   #insertem el node lliure    a la posicio i
        w = v[:]
        w[k] = True
        # Calculem el cost de l'assignacio actual
        z = cost_assignacio(q)
        # Fitem inferiorment i mirem si paga la pena entrar 
        # recursivament. Observar la condicio, ha de ser
        # z + z_ > min_z (no es correcte fer >=). Provar de
        # calcular al fita amb la funcio fita1 o fita2
        z_ = fita2(q,w)
        if (z + z_ > min_z):
          print s + "No continuo amb", q, "(",z,"+",z_," > ",min_z,")"
          return
        # Imprimim informacio a pantalla
        print s + "Entro ", q, "(",z,"+",z_," <= ",min_z,")"
        # Aqui fem la crida recursiva. Observar que
        # la cridem per trobar una node lliure
        # a la qual poguem assignar el projecte i+1
        total_crides = total_crides + 1
        branch_and_bound(i+1, q, z,w)
        print s + "Surto ", q

def main():
   global M, N, min_z, min_x, total_crides
   M = [[0, 2, 3, 4, 5],[2,0, 60, 7, 8],[3, 60, 0, 9, 100],[4, 7, 9,0, 11],[5, 8, 100, 11, 0]]
   N  = len(M)
   # Fem un calcul heuristica
   
   # Indicarem amb -1 que la node esta lliure
   x = [-1 for i in range(N)]
   v = [False for i in range(N)]
   heuristica()
   x[0] = 0
   v[0] = True
   # Amb total_crides comptem el nombre de crides recursives que fem
   total_crides = 1;
   # Iniciem la crida recursiva
   branch_and_bound(1, x, 0,v)
   print "L'assignacio final es ", min_x, "i te cost", min_z
   print "En total hem fet", total_crides, "crides a la funcio branch_and_bound"

main()
