import sys
entrada = [int(x) for x in sys.stdin.read().split()]
alvo = entrada[0]
lista = entrada[1:]
def busca_binaria(lista, alvo):
    if len(lista)==0:
        return 0
    meio = len(lista) // 2
    if lista[meio] == alvo: 
        return 1 
    elif alvo < lista[meio]: 
        return 1 + busca_binaria(lista[:meio], alvo)
    else: 
        return 1+ busca_binaria(lista[meio+1:], alvo)
    
print(busca_binaria(lista, alvo))
     