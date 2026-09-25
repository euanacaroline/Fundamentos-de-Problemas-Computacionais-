# percorre listas ordenadas obrigatoriamente 



vetor = [ ]

x = (" ")

def busca_binaria (vetor, x): 
    inicio = 0 
    fim = len(vetor)-1 

    while inicio <= fim: 
        meio = (inicio + fim)//2 

        if vetor[meio] == x :
            return meio 
        elif vetor[meio] < x: 
            inicio = meio + 1 
        else: 
            fim = meio - 1 

    return -1 

print(busca_binaria([2, 4, 6, 8, 10, 12, 14], 12))
