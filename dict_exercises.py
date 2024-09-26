# 1. Contagem de Frequência
# Escreva uma função que receba uma lista de palavras
# e retorne um dicionário onde as chaves são as palavras
# e os valores são o número de vezes que cada palavra aparece na lista.
def contagem_palavras(palavras):
    contagem = {}
    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1

        else:
            contagem[palavra] = 1
    return(contagem)

palavras = ['gato', 'cachorro', 'gato', 'peixe', 'gato', 'cachorro']
resultado = contagem_palavras(palavras)
print("Contagem de palavras da minha lista", resultado)


# 2. Atualizar Valores de um Dicionário
# Escreva uma função que receba um dicionário com valores inteiros
# e duplique cada valor.
def duplicar_valores(meu_dict):
    novo_dict = {}

    for chave, valor in meu_dict.items():
        novo_dict[chave] = valor * 2
    return(novo_dict)

meu_dict_original = {"a": 10, "b": 20, "c": 30}
resultado = duplicar_valores(meu_dict_original)

print("Meu dicionário original", meu_dict_original)
print("Meu novo dicionário", resultado)


# 3. Mesclar Dois Dicionários
# Escreva uma função que receba dois dicionários
# e os mescle em um novo dicionário.
# Se houver conflito de chaves, o valor do segundo dicionário deve sobrescrever o do primeiro.
def mesclar_dicionarios(dict1, dict2):
    dicionario_mesclado = {**dict1, **dict2}
    return(dicionario_mesclado)

dicionario_1 = {"a": 1, "b": 2}
dicionario_2 = {"b": 3, "c": 4}

resultado = mesclar_dicionarios(dicionario_1, dicionario_2)
print(resultado)
