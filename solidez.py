#implementa a solução dinâmica para a solidez do vetor, usa a solução da firmeza para divisão do problema em subestruturas ótimas
def solidezV3(A, p, r) :
	firmeza = [None]*r
	firmeza[p] = A[p]

	for i in range(p+1, r):
		if firmeza[i-1] > 0 :
			firmeza[i] = firmeza[i-1] + A[i]
		else:
			firmeza[i] = A[i]

	x = firmeza[p]

	for i in range(p+1, r):
		if firmeza[i] > x:
			x = firmeza[i]

	return x

#função que retorna o

#implementa a solução para o problema da solidez usando a técnica da divisão e conquista
def solidezV2(A, p, r):
	firmeza = A[:]

	if p == r:
		return A[p]

	else:
		q = int((p+r) / 2)
		x = solidezV2(A, p, q)
		y = solidezV2(A, q+1, r)
		z = solidezV2_meio(A, p, q, r)

		return max(x, y, z)

def solidez(A, p, r):
	pass
	