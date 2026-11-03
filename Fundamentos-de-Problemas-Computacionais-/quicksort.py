entrada = 1, 14, 16, 98, 2, 100, 43, 75
def quicksort(lista): 
    if len(lista) <= 1 :
        return lista 

    primeiro = lista[0]
    meio = len(lista) // 2
    ultimo = lista[-1]
    candidatos = [primeiro, meio, ultimo]
    candidatos.sort()
    pivo = candidatos[1]

    menores, iguais, maiores = [], [], []
 

    for x in lista: 
        if x < pivo: 
            menores.append(x)
        elif x == pivo:
            iguais.append(x)
        else: 
            maiores.append(x)

    return quicksort(menores) + iguais + quicksort(maiores)

print(quicksort(entrada))