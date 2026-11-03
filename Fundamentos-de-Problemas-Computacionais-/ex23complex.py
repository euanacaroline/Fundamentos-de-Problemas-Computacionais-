vetor = [int(num) for num in input("Digite o vetor ordenado: ").split()] 

x = int(input("Digite o numero para inserir: "))

def inserir_ordenada (vetor, x):
    i = len(vetor) - 1
    vetor.append (None)

    while i >=0 and vetor[i] > x : 
        vetor[i + 1] = vetor[i]
        i -= 1

    vetor[i + 1] = x
    return vetor 

print (inserir_ordenada(vetor, x))