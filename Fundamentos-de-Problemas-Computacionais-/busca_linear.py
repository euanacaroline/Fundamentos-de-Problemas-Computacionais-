def busca_linear(vetor, x):
    n = len(vetor)

    for i in range(n):
        if vetor[i] == x: 
            return i 

    return -1 

print(busca_linear([1, 3, 5, 7, 9], 3))