
#n = 4
#M = [
#	[0,0,1,0],
#	[0,0,1,0],
#	[1,1,0,1],
#	[0,0,1,0]
#]

n = 7
M = [
	[0,0,1,1,0,1,0],
	[0,0,0,1,0,0,0],
	[1,0,0,0,0,1,0],
	[1,1,0,0,0,0,1],
	[0,0,0,0,0,0,1],
	[1,0,1,0,0,0,0],
	[0,0,0,1,1,0,0]
]

def factible(a,c):
	for i in range(n):
		if (not c[i] and  not a[i]):
			return False
	return True


def backtracking(i,a,c):
	global z_millor, a_millor
	if i == n:
		if factible(a,c):
			z = 0
			for j in range(n):
				z = z + a[j]
			if (z < z_millor):
				z_millor = z
				a_millor = a[:]
	else:
		a[i] = 1
		cc = c[:]
		for j in range(n):
			if M[i][j]:
				cc[j] = 1
		j = i+1
		backtracking(j,a,cc)
		a[i] = 0
		backtracking(j,a,c)

def main():
        # z_millor es el nombre d'antenes minim necessari
        # a_millor guarda la ciutat on s'han de col-locar les antenes
	global z_millor, a_millor
	# Inicialitzacio de la variable 'a' (es 1
	# si hem de col-locar una antena a la ciutat 
	# i-essima). La variable c guarda les ciutats
	# cobertes per les antenes.	
	a = [0]*n
	c = [0]*n
	# Inicialitzacio amb la pitjor solucio possible.
	# (s'ha de posar una antena a cada ciutat)
	z_millor = n
	a_millor = [1]*n
	# Cridem a la funcio de backtracking
	backtracking(0,a,c)
	# Imprimim resultat
	s = ""
	for i in range(n):
		if a_millor[i]:
			s = s + str(i+1) + ","
	print "En total fan falta " + str(z_millor) + " antenes"
	print "S'han de colocar a " + s

main()

