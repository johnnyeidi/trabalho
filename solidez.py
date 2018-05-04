import math # floor

# implementa a solução dinâmica para a solidez do vetor, usa a solução da firmeza para divisão do problema em subestruturas ótimas
def solidezV3(A, p, r) :
	firmeza = [0]*r
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

# função utilizada na versão 2 do solidez
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


# implementa a solução para o problema da solidez usando a técnica da divisão e conquista
def solidezV2(A, p, r):
  
	valores = [0]*r
	
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

		return max(valores)

def solidezV1(A, p, r):
  soma = [0]*r

  # se o intervalo é unitário
  if p == r:
    return A[p]

  i, j = p, 0
  
  while (j < r):
    
    while (i < r) and (A[i] >= 0):
      soma[j] += A[i]
      i += 1
	  
	# se somou até o número máximo de elementos
    if i == r:
      # sai do primeiro laço
      j = r
    # se ainda restam elementos para análise 
    else:
      j += 1
      # incrementa o i para a continuação do cálculo
      i += 1
  
  return max(soma)

def main ():
  a = [1,1,1,0,-1,1]
  print("soma máxima:", solidezV2(a, 0, len(a)))
  
  
main()