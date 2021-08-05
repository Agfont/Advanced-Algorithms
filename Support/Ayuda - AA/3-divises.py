def divises(C,M): # funcio que calcula si hi ha alguna divisa amb la qual es pot especulari obtenir un benefici
    n = len(C[0]) # es mira com es de gran la matriu
    Mactual = []
    Manterior = C
    Mtri = []       # es crea una matriu tridemensional on anar guardan totes les matrius de canvi
    Mtri.append(C)
    canvi = False   # en el moment que hi hagi una millora, es para la cerca
    for k in range(n):  # utilitzant l'algoritme de Floyd , es van crean les matrius de canvi
        for i in range(n):  # es recorren totes les files
            Mactual.append([])  # per cada fila es va posant un vector mes on guarda la informacio
            ik = Manterior[i][k]    # per optimitzar saccedeix nomes una vegada a la posicio M[k-1][i][k]
            for j in range(n):      # es recorre per columnes
                if k!= i and k!=j and canvi == False: # per evitar bucles no es permet anar de una moneda a ella mateixa
                    Mactual[i].append(max(ik*Manterior[k][j],Manterior[i][j])) # volem el maxim entre els canvis de moneda o el que tenim
                else:
                    Mactual[i].append(Manterior[i][j])
                    
                if i == j and Mactual[i][i] != Manterior[i][i]: # si hi ha algun canvi en la diagonal, senyal de que hi haura benefici, ja que sempre s'escull el maxim
                    
                    print "Amb ",C[j][j],M[j]," com a maxim es poden obtenir ",C[j][j] * Mactual[i][j],M[j]     # simprimeix el resultat
                    canvi = True   # es marca conforme hi ha hagut un canvi i s'ha d'acabar els recorreguts
                    Manterior = Mactual     # s'actualitzen matrius
                    Mtri.append(Manterior)  # es completa la matriu tridemensional
                    cua = Recorregut(Mtri,k+1,i,j,[])   # sutilitza la matriu tridimensional amb tota la informacio per buscar el passos per poder especular amb aquesta moneda
                    cua.insert(0,j)
                    print "Ho podras fer així:",    # simprimeix per pantalla el cami a seguir
                    for t in range(len(cua)):
                        print M[cua[t]],
                        print "->",
                    print M[j]
                    break                   # es para el recorregut

            if canvi == True: break         
        
        
        Manterior = Mactual     # s'actualitzen les matrius i la matriu tridimensional
        Mactual = []
        Mtri.append(Manterior)
        
        if canvi == True: break     # es para de crear capes a la matriu tridimensional
        
def Recorregut(Mtri,k,i,j,cua): #funcio que busca el recorregut de canvi de moneda
    
    if k == 0:return cua+[j] # si s'ha arribat a la matriu d'inici, es retorna la posicio
    if Mtri[k][i][j] != Mtri[0][i][j] : return cua+Recorregut(Mtri,k-1,i,k-1,cua)+Recorregut(Mtri,k-1,k-1,j,cua) # si hi ha hagut algun canvi, es a dir una multiplicacio, es crida la mateixa funcio per a lanterior matriu 
    else : return cua # si no hi ha hagut canvi 
    
    
