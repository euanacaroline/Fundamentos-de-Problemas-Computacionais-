import sys

def insertion_sort(A): 
    for j in range (1, len(A)):
        chave = A[j]
        i = j - 1
        while i >= 0 and A[i] > chave: 
            A[i+1] = A[i]
            i = i-1 
        A[i + 1]= chave 
    return A 
    
entrada = input(" digite os numero separad: ")   
lista = [int(x) for x in entrada.split()]

insertion_sort(lista)
print(*lista)



