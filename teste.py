def dividir_lista(lista):
    listas_menores = []
    for i in range(0, len(lista), 5):
        lista_menor = lista[i:i+5]
        listas_menores.append(lista_menor)
    return listas_menores

# Exemplo de uso
lista_maior = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
listas_menores = dividir_lista(lista_maior)
for lista_menor in listas_menores:
    print(lista_menor)
