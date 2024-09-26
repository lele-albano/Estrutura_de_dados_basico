# 1. Encontrar Números Pares em uma Lista
# Escreva uma função que receba uma lista de inteiros como entrada
# e retorne uma nova lista contendo apenas os números pares.
def encontrar_pares(numeros):
    return [num for num in numeros if num % 2 == 0]

numeros = [1, 2, 3, 4, 5, 6]

pares = encontrar_pares(numeros)
print("Números pares", pares)


# 2. Soma dos Elementos de uma Lista
# Escreva uma função que receba uma lista de inteiros
# e retorne a soma de todos os elementos.
def soma_elementos(numeros):
    return sum(numeros)

numeros = [10, 20, 30]

resultado = soma_elementos(numeros)
print("A soma dos elementos é:", resultado)


# 3. Remover Duplicatas de uma Lista
# Escreva uma função que receba uma lista de inteiros
# e retorne uma nova lista sem duplicatas.
def remover_duplicatas(numeros):
    return list(set(numeros))

numeros =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10]
resultado = remover_duplicatas(numeros)
print("Nova lista:", resultado)
