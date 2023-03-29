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

# Imprimir as coordenadas de cada elemento em ordem crescente de valor
for elemento in posicao_ordem:
    print(f'Valor: {elemento[0]}, Coordenadas: {elemento[1]}')