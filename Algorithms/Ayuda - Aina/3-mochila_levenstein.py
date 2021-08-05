def mochila_levenstein(peso_maximo, lista_valores, lista_pesos):
    couples = [0]*(len(lista_pesos))
    '''
    for i in range (0, len(lista_pesos)):
        couples[i] = [lista_pesos[i], lista_valores[i]]
        
    couples.sort()
    print couples
    '''
    
    
    lst_items = [0]*(peso_maximo)
    
    for i in range (1, len(lst_items)):
        print "-------------------"
        print i
        print "jotas"
        aux = [0]*(i+1)
        for j in range (0, i+1):
            try:
                '''
                print "Para sumar", couples[i-1][1]
                #print "Para mirar el maximo", lst_items[i-j]
                aux[j] = lst_items[i-j] + couples[j-1][1]
                '''
                print j
                aux[j] = lst_items[i-j] + lista_valores[j-1]
                print "indice", j, "aux de indice", aux[j]

            except:
                pass   
        lst_items[i] = max(aux)
    
    print lst_items     
            
#mochila_levenstein(5, [3, 1, 2, 5], [2, 2, 3, 1])
#mochila_levenstein(5, [5, 3, 1, 2], [1, 2, 2, 3])
#mochila_levenstein(5, [5, 25, 1, 2], [1, 2, 3, 3])
mochila_levenstein(7, [1, 4, 6], [1, 2, 4])