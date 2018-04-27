import math #floor

#implementa a solução dinâmica para a solidez do vetor, usa a solução da firmeza para divisão do problema em subestruturas ótimas
def solidezV3(A, p, r) :
	firmeza = [None]*r
	firmeza[p] = A[p]

	for i in range(p+1, r):
		if A[i-1] > 0 :
			firmeza[i] = firmeza[i-1] + A[i]
		else:
			firmeza[i] = A[i]

	x = firmeza[p]

	for i in range(p+1, r):
		if firmeza[i] > x:
			x = firmeza[i]

	return x

#função utilizada na versão 2 do solidez
def solidez_meio(A, p, q, r):
	B = [None]*r
	B = A
	aux = s = B[q]

	for i in range(q-1, p, -1):
		s += B[i]

		if s > aux :
			aux = s

	aux2 = s = B[q+1]

	for j in range(q+2, r):
		s += B[j]

		if s > aux2:
			aux2 = aux

	return aux + aux2


#implementa a solução para o problema da solidez usando a técnica da divisão e conquista
def solidezV2(A, p, r):
	B = [None]*r
	B = A
	valores = []
	if p == r:
		return B[p]

	else:
		q = math.floor(((p+r) / 2))
		x = solidezV2(B, p, q)
		y = solidezV2(B, q+1, r)
		z = solidez_meio(B, p, q, r)

		valores.append(x)
		valores.append(y)
		valores.append(z)

		return max(valores)

def solidez(A, p, r):
	pass
	