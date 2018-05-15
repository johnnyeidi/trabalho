import math # floor
from random import randint #para gerar numeros aleatorios
import time #Calcular o tempo

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
	esquerda = 1
	direita = 1
	maior = A[0]
	Sol = 0

	for i in range(0, r, 1):
		Sol = 0
		for j in range(i, r, 1):
			Sol = Sol + A[j]
			if (Sol > maior) :
				maior = Sol
				esquerda = i
				direita = j

	return maior


def main ():
  
	#V1 = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
	y_axis1 = []
	y_axis2 = []
	y_axis3 = []
	x_axis = []
	start_time = time.time()

	for i in range(100,20100,100):
		print(i)
		V1 = []
		V2 = []
		V3 = []

		x_axis.append(i)

		for j in range(i):
			valor = randint(-10*i, 100*i)
			V1.append(valor)
			V2.append(valor)
			V3.append(valor)

		#Tempo Solidez V1
		start_time = time.time()
		tam = solidezV1(V1, 0, len(V1))
		end_time = time.time()
		del V1[:]
		y_axis1.append(end_time - start_time)

		#Tempo Solidez V2
		start_time = time.time()
		tam = solidezV3(V2, 0, len(V2))
		end_time = time.time()
		del V2[:]
		y_axis2.append(end_time - start_time)

		#Tempo Solidez V3
		start_time = time.time()
		tam = solidezV3(V3, 0, len(V3))
		end_time = time.time()
		del V3[:]
		y_axis3.append(end_time - start_time)
		
	try:
		nome_arquivo = 'saida.txt'
		arquivo = open(nome_arquivo, 'r+')
	except FileNotFoundError:
		arquivo = open(nome_arquivo, 'w+')

	arquivo.write("		n")
	arquivo.write("								solidezI")
	arquivo.write("								solidezII")
	arquivo.write("								solidezIII\n")
	arquivo.write("-----------------------------------------------------------------------------------------------------------\n")

	for i, item1, item2, item3 in zip(x_axis, y_axis1, y_axis2, y_axis3):
		arquivo.write("%5s        %26s        %26s        %26s\n" % (i,item1, item2, item3))

	arquivo.close()
  
main()