def motxilla1(P,V,K):
	N = len(P)
	pes   = 0
	valor = 0

	for i in range(N):
		z = pes + P[i]
		while (z <= K):
			pes = z
			valor = valor + V[i]
			z = pes + P[i]
	print valor


def motxilla2(P,V,K):
	N = len(P)
	pes   = 0
	valor = 0

	for i in range(N):
		while (pes + P[i] <= K):
			pes = pes + P[i]
			valor = valor + V[i]

	print valor

