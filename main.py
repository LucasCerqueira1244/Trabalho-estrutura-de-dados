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