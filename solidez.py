import math # floor

# implementa a solução dinâmica para a solidez do vetor, usa a solução da firmeza para divisão do problema em subestruturas ótimas
def solidezV3(A, p, r) :
	firmeza = [0]*r
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

# função utilizada na versão 2 do solidez
def solidez_meio(A, p, q, r):

	aux = s = A[q]

	for i in range(q-1, p-1, -1):
		s += A[i]

		if s > aux :
			aux = s

	aux2 = s = A[q+1]

	for j in range(q+2, r+1):
		s += A[j]

		if s > aux2:
			aux2 = s

	return aux + aux2


# implementa a solução para o problema da solidez usando a técnica da divisão e conquista
def solidezV2(A, p, r):
	valores = []

	if p == r:
		return A[p]

	else:
		q = math.floor(((p+r) / 2))
		x = solidezV2(A, p, q)
		y = solidezV2(A, q+1, r)
		z = solidez_meio(A, p, q, r)


		valores.append(x)
		valores.append(y)
		valores.append(z)

		# print(valores)
		return max(valores)

def solidezV1(A, p, r):
	soma = []

	# se o intervalo é unitário
	if p == r:
		return A[p]

	i, j = p, 0

	while (j < r):
		aux = 0
		i = r - j -1
		while (i >= 0):
			aux += A[i]
			i -= 1

		soma.append(aux)

		j += 1
		print(soma)

	j = 0

	while (j < r):
		aux = 0
		i = j
		while (i < r):
	  		aux += A[i]
	  		i += 1

		soma.append(aux)

		j += 1
		print(soma)

	return max(soma)

def main ():
  a = [0, 1, 1, -1,-1]
  print("soma máxima:", solidezV1(a, 0, len(a)))
  
  
main()