# Programa que busca el cami més curt per solucionar el problema del viatger utilitzant ramificació i poda

def fita2(x,v):
  # Calculem primer la fita ignorant nodes
  z1_ = 0
  l  = len(x)
  # La matriu p emmagatzema els nodes que estan
  # lliures. Si el node k no esta lliure, x[k] indica
  # el node que li hem assignat. p[k] es True si
  # el node esta lliure, False si esta assignat a
  # alguna node.
  p  = [True for k in range(l)]
  for k in range(l):
     if not node_lliure(k, v):
        p[v[k]] = False
  # Calculem la fita ignorant nodes. Es a dir,
  # busquem els nodes lliures i li assignem
  # el cost del cami que el fa mes economic.
  # Cal fer un minim per columnes. 
  for k in range(l):
     if p[k]:
       # NOTA: busquem la primera node no assignada
       # a un cami
       j = 0
       while not node_lliure(j, x):
         j+=1
       # NOTA: li assignem el minim
       min_c = M[j][k]
       # NOTA: Ara busquem entre la resta de nodes
       # no assignades de la mateixa columna
       j+=1
       while j < l:
          if not node_lliure(j, v):
             min_c = min(min_c, M[j][k])
          j+=1
       z1_ += min_c
  # Ara calculem la fita ignorant els nodes. Busquem
  # els nodes lliures i li assignem el cost del
  # cami mes economic. 
  z2_ = 0
  for k in range(l):
     if node_lliure(k, v):
        # NOTA: busquem el primer node lliure
        # de l'node k
        j = 0
        while not p[j]:
           j+=1
        # NOTA: li assignem el minim
        min_c = M[k][j]
        j+=1
        # NOTA: Ara busquem entre la resta de camins
        # de la mateixa node, pero nomes entre els
        # nodes no assignats.
        while j < l:
           if not p[j]:
              min_c = min(min_c, M[k][j])
           j+=1
        z2_ += min_c
  return max(z1_, z2_)

# Aquesta funcio retorna True si la node k esta lliure
#
# variable k: node per la qual volem saber si esta lliure
# variable x: vector on tenim associades les ciutats amb els camins

def node_lliure(k, v):
  return not v[k]

def cost_assignacio(x):  
  global N, M
  cost = 0 
  k = 0 
  while k < N-1 and x[k+1] != -1:
    cost += M[x[k]][x[k+1]] 
    k += 1 
  cost += M[x[k]][x[0]]

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
# variable i: index del cami a assignar a alguna node
# variable x: assignacio actual de ciutats amb camins.
#             x[k] indica el cami que hem assignat a la ciutat k
# variable z: cost de l'assignacio de ciutats amb camins que hem fet

def branch_and_bound(i, x, z,v):
  global min_z, min_x, N, total_crides, solucions_camins, solucions_costos
  # Creem una cadena de caracters en blanc
  # per imprimir de forma bonica per pantalla
  s = ""
  for k in range(i+1):
     s += "   "
  # Mirem si ja hem assignat tots els camins
  # i comprovem si el cost de l'assignacio que
  # tenim es inferior al que tenim actualment.
  if (i == N) and (min_z > z): 
     min_x = x[:]
     min_z = z 
     print s + "---> Solucio", min_x, "amb cost", min_z
     solucions_camins.append(x[:])
     solucions_costos.append(z)
     return
  # Analitzem les ciutats lliures i els 
  # assignem el cami i
  for k in range(1, N):
     if (node_lliure(k, v)):
        # La node k esta lliure i li assigno
        # el cami i.
        q = x[:]
        q[i] = k   #insertem el node lliure  k  a la posicio i
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
        # a la qual poguem assignar el cami i+1
        total_crides+= 1
        branch_and_bound(i+1, q, z,w)
        print s + "Surto ", q

def main():
   global M, N, min_z, min_x, total_crides,solucions_camins, solucions_costos
   M = [[0, 2, 3, 4, 5],[2,0, 60, 7, 8],[3, 60, 0, 9, 100],[4, 7, 9,0, 11],[5, 8, 100, 11, 0]]
   N  = len(M)
   solucions_camins = []
   solucions_costos= []
   # Indicarem amb -1 que la node esta lliure
   x = [-1 for i in range(N)]
   v = [False for i in range(N)]
   # Fem un calcul heuristica
   heuristica()
   x[0] = 0
   v[0] = True
   # Amb total_crides comptem el nombre de crides recursives que fem
   total_crides = 1;
   # Iniciem la crida recursiva
   branch_and_bound(1, x, 0,v)
   print "Els diferents camins son:"
   resultats()
  #  print "L'assignacio final es ", min_x, "i te cost", min_z
   print "En total hem fet", total_crides, "crides a la funcio branch_and_bound"

#Funcio que imprimeix tots els resultats millors 
def resultats():
  global solucions_camins, solucions_costos, min_z
  for i in range(len(solucions_costos)):
    if solucions_costos[i] ==min_z:
      for p in solucions_camins[i]:
        print p+1,"-->",
      print solucions_camins[i][0]+1, "amb cost", min_z
      
      
main()
