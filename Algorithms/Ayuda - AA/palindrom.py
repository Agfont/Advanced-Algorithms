
# Assignatura : Algorismica Avançada
# Programa que donada una frase busca palindroms dins les paraules

def espalin(pal): # funcio que diu si una paraula es palindroma o no
    for a in range((len(pal)/2)+1):
        if pal[a] != pal[len(pal)-1-a]: # si hi ha algu que no es igual retorna false
            return False;
    return True; # si no hi hagut cap diferencia implica que es palindroma

def buscaiguals(paraula): # donada una paraula, es dedica a buscar les les lletres iguals. Quan les troba envia tot el substring entre lletra i lletra per veure si es palindrom
    palin =[]
    for a in range(len(paraula)-1): # es va recorrent tota la paraula desdel principi fins el final
        e = len(paraula)-1
        while e >a:#i es va comparan des del final fins al principi; s'utilitza un while per que es modifica l'iterador(la longitud de la paraula), i amb un for no es pot modificar l'iterador
            if paraula[a] == paraula[e]: 
                if espalin(paraula[a:e+1]) == True: # si el sibstring es palindrom
                    aux = paraula[a:e+1]
                    palin.append(aux);#s'afegeix a la llista de paraules
                    paraula = paraula[:a]+paraula[e+1:]# i es borra el palindrom de la paraula
                    a = 0
                    e = len(paraula) #es modifica l'iterador per continuar la cerca 
            e = e-1;
    return palin;

def pal():
    entra1 =raw_input("Entra el palídrom:")
    entra = entra1.split(" ")
    t = 0
    while t < len(entra): # bucle per eliminar els espais sobrans en la frase
        a = entra[t]
        if a == '':
            entra.remove("") #s'eliminan els espais i es modifica l'iterador
            t=0
        t = t+1
    for p in range(len(entra)): #per cada paraula de la frase
        aux = buscaiguals(entra[p]) #es busquen els palindroms interns 
        print 'Paraula ', p+1,': ', entra[p]
        if len(aux)>0:
            for i in range(len(aux)):
                print "Palíndrom ",i+1,"(",len(aux[i])," caràcters): ",aux[i]
        else : print 'No conté cap palíndrom'



pal()

