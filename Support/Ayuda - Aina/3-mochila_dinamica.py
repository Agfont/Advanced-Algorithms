def mochila_dinamica(peso_maximo, lista_pesos, lista_valores):    
    #No hace falta que los pesos y los valores esten ordenados
    
    #Vector de soluciones. Podria ser una matriz, pero un vector es suficiente. 
    vector = [0]*(peso_maximo + 1)
    #vector_objetos = [[0]*len(lista_valores)]*(peso_maximo+1)
    vector_objetos = [[ 0 for i in range(peso_maximo+1)] for j in range (len(lista_valores))]

    #recorre los items 
    for i in range(0,len(lista_valores)):
        #recorremos la posicion del vector
        #add = 0
        for j in range(0, (peso_maximo + 1)):
            
            #Si el item cabe dentro de la mochila: 
            if j - lista_pesos[i] >= 0:
                #peso que nos sobra, dado cierto item
                valor = j - lista_pesos[i]
                #si el valor del item mas el valor que nos sobra y podemos meter es mayor
                #modificamos el vector que tenemos
                if lista_valores[i] + vector[valor] > vector[j]:
                    vector[j] = lista_valores[i] + vector[valor]
                    for k in range(0, i):
                        vector_objetos[k][j] = vector_objetos[k][valor]
                    vector_objetos[i][j] = vector_objetos[i][valor] + 1
                    
    for i in range (0, len(vector)):
        print "peso", i, "valor", vector[i]

    print "obxectos engadidos", vector_objetos



mochila_dinamica(7, [1, 2, 4], [1, 4, 6])
                    
                    
