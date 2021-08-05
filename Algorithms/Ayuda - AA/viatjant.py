  
# Mirem si una empresa esta lliure 

def node_lliure(k, x):
  return not y[k]

# Calculem el cost d'assignacio d'empreses
# amb projectes

def cost_assignacio(x):
  global N, M
  z = 0
  for k in range(N):
    if not empresa_lliure(k, x):
      z = z + M[k][x[k]]
  return z

# Anem a aproximar el cost minim d'assignacio.
# Amb un algorisme vorac obtindrem una fita
# superior del cost que estem buscant

def vorac():
  global min_x, min_z
  min_x = [0, 1, 2, 3]
  min_z = cost_assignacio(min_x)

# Cerca exhaustiva
# variable i: index del projecte a assignar a alguna empresa
# variable x: assignacio actual d'empreses amb projectes.
#             x[k] indica el projecte que hem assignat a l'empresa k
# variable z: cost de l'assignacio actual d'empreses 

#def exhaustiu(i, x, z):
#  global min_z, min_x, N
  # Mirem si ja hem assignat tots els projectes
  # i comprovem si el cost de l'assignacio que
  # tenim es inferior al que tenim actualment.
 # if (i == N):  
  #   if (min_z > z): 
   #     min_x = x[:]
    #    min_z = z 
    # return
  # Analitzem les empreses lliures i els 
  # assignem el projecte i
#  for k in range(N):
 #    if (empresa_lliure(k, x)):
        # La empresa k esta lliure i li assigno
        # el projecte i.
  #      q = x[:]
   #     q[k] = i
        # Calculem el cost de l'assignacio actual
    #    z = cost_assignacio(q)
        # Aqui fem la crida recursiva. Observar que
        # la cridem per trobar una empresa lliure
        # a la qual poguem assignar el projecte i+1
     #   exhaustiu(i+1, q, z)
     
def exhaustiu(i,x,w):
    if i==N:
        z = cast(x)
        if z < min_z:
            min_z = z
            min_x = x[:]
        return 
    for r in range(N):
        if node_lliure(r,x):
             w = y[:]
             w[k] = True
             exhaustiu(i+1,q,w)
def main():
   global M, N, M_, min_z, min_x ,y,k
   M  = [[0,2,3,4,5],[2,0,60,7,8],[3,60,0,9,100],[4,7,9,0,11],[5,8,100,11,0]]
   N  = len(M)
   # Fem un calcul vorac
   # Indicarem amb -1 que la empresa esta lliure
   x = [-1 for i in range(N)]
   y = [False for i in range(N)]
   # Iniciem la crida recursiva
   x[0] = 0
   y[0] = True
   exhaustiu(1, x,y)
   print "L'assignacio final es ", min_x, "i te cost", min_z

main()
