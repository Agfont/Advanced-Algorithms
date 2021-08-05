def mochila_dinamica(peso_maximo, lista_pesos, lista_valores):    
    #No hace falta que los pesos y los valores esten ordenados
    
    #Vector de soluciones. Podria ser una matriz, pero un vector es suficiente. 
    vector = [0]*(peso_maximo + 1)
    #vector_objetos = [[0]*len(lista_valores)]*(peso_maximo+1)
    vector_objetos = [[0]*(peso_maximo + 1) for x in range(len(lista_pesos))]
    
    for i in range(1, (peso_maximo + 1)):
        engadido = 0
        aux = 0
        for j in range (0 ,len(lista_valores)):
            if i - lista_pesos[j]>= 0:
                valor = i - lista_pesos[j]
                if lista_valores[j] + vector[valor] > vector[i]:
                    vector[i] = lista_valores[j] + vector[valor]
                    engadido  = j
                    aux=valor
        for j in range (0 ,len(lista_valores)):
            vector_objetos[j][i] += vector_objetos[j][aux]
        vector_objetos[engadido][i] += 1
            
        
    for i in range(0, peso_maximo +1):
        print "peso", i, "valor", vector[i]
    
    print vector_objetos
                                         

        
mochila_dinamica(7, [1, 2, 4], [1, 4, 6])