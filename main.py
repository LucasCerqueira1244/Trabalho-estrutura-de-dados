import matplotlib.pyplot as plt
import timeit

matriz = [[1, 1, 1, 0, 0, 0],
          [0, 1, 0, 0, 0, 0],
          [1, 1, 1, 0, 0, 0],
          [0, 0, 2, 4, 4, 0],
          [0, 0, 0, 2, 0, 0],
          [0, 0, 1, 2, 4, 0]]


#Criar uma lista para armazenar o valor e suas coordenadas:
posicao = []

for i, linha in enumerate(matriz):
    for j, valor in enumerate(linha):
        posicao.append((valor, (i, j)))

#Ordenar a lista de forma crescente:
posicao_ordem = sorted(posicao)

#Imprimir as coordenadas de cada elemento em ordem crescente de valor:
for elemento in posicao_ordem:
    print(f'Valor: {elemento[0]}, Coordenadas: {elemento[1]}')

#Contador para calcular quantos elementos estão presentes na matriz:

cont_1 = 0
cont_2 = 0
cont_4 = 0

#Contando elementos de número 1:
for linha in matriz:
    for valor in linha:
        if valor == 1:
            cont_1 += 1
            soma = valor * cont_1

#Contando elementos de número 2:
for linha in matriz:
    for valor in linha:
        if valor == 2:
            cont_2 += 1
            soma2 = valor * cont_2

#Contando elementos de número 4:
for linha in matriz:
    for valor in linha:
        if valor == 4:
            cont_4 += 1
            soma4 = valor * cont_4


print(f'Foram encontrados: {cont_1} elementos de número 1 e seu total é {soma}\n'
      f'Foram encontrados: {cont_2} elementos de número 2 e seu total é {soma2}\n'
      f'Foram encontrados: {cont_4} elementos de número 4 e seu total é {soma4}')

# Define uma função que calcula o número de operações para um tamanho de entrada específico
def num_operacoes(n):
    matriz = [[1] * n for _ in range(n)]
    posicao = []
    for i, linha in enumerate(matriz):
        for j, valor in enumerate(linha):
            posicao.append((valor, (i, j)))
    posicao_ordem = sorted(posicao)
    cont_1 = sum(linha.count(1) for linha in matriz)
    soma_1 = 1 * cont_1
    cont_2 = matriz.count(2)
    soma_2 = 2 * cont_2
    cont_4 = matriz.count(4)
    soma_4 = 4 * cont_4
    return cont_1 + cont_2 + cont_4

# Cria um array com os tamanhos de entrada
tamanhos = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Cria um array com o número de operações para cada tamanho de entrada
operacoes = []
for tamanho in tamanhos:
    # Mede o tempo de execução do algoritmo para o tamanho de entrada atual
    tempo = timeit.timeit(lambda: num_operacoes(tamanho), number=100)
    operacoes.append(tempo)

# Plota o gráfico
plt.plot(tamanhos, operacoes, label='Complexidade de tempo')
plt.xlabel('Tamanho da entrada (número de elementos na matriz)')
plt.ylabel('Número de operações')
plt.title('Gráfico da notação Big O (O(n^2))')
plt.legend()
plt.show()
