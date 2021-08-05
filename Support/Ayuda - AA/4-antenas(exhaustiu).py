#M = [
#	[0,0,1,0],
#	[0,0,1,0],
#	[1,1,0,1],
#	[0,0,1,0]
#]

M = [
[0,0,1,1,0,1,0],
[0,0,0,1,0,0,0],
[1,0,0,0,0,1,0],
[1,1,0,0,0,0,1],
[0,0,0,0,0,0,1],
[1,0,1,0,0,0,0],
[0,0,0,1,1,0,0]
]

# exhaustiu:
# variable i: nivell a l'arbre, indica a més nombre d'antenes col-locades
# variable x: on col-loquem les antenes
# variable y: ciutats cobertes 
# variable z: nombre de ciutats cobertes
def exhaustiu(i, x, y, z):
    global N, min_i, min_x
    if (z == N):
        if (i < min_i):
            min_i = i
            min_x = x[:]
        return
    for k in range(N):
        # Busquem una ciutat no coberta
        if not y[k]:
           # Si la ciutat k no esta coberta hi posem 
           # una antena
           w = x[:]
           w[k] = True
           # Calculem les ciutats cobertes. Marquem
           # primer la ciutat k on col-loquem l'antena. 
           q = y[:]
           q[k] = True 
           # Marquem els veins i calculem el nombre de ciutats
           # cobertes
           t = z + 1
           for p in range(N):
              # Ens preguntem si la ciutat es veina.
              # La marquem nomes si no esta coberta
              # (la ciutat veina pot estar coberta 
              # per una altra antena)
              if M[k][p] and not q[p]:
                  q[p] = True
                  t = t + 1
           # Fem la crida recursiva
           exhaustiu(i+1, w, q, t) 

def main(M):
    global min_i, min_x, N
    N = len(M)
    # Variable per indicar on col-loquem les antenes
    x = [False for i in range(N)]
    # Variable per indicar les ciutats cobertes
    y = [False for i in range(N)]
    # Inicialitzacio. Posem atenes a totes les ciutats.
    min_i = N
    min_x = [True for i in range(N)]
    # Funcio exhaustiu
    exhaustiu(0, x, y, 0)
    # Generem resultat
    s = ""
    for i in range(N):
        if (min_x[i]):
            s = s + str(i+1) + ","
    print "En total fan falta " + str(min_i) + " antenes"
    print "S'han de colocar a " + s

main(M)

