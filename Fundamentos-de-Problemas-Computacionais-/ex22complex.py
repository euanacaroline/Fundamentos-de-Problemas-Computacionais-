# crie um algorítmo que imprima "ORDENADO" caso esteja na ordem crescente

vetor = list(map(int, input(" ").split()))
n = len(vetor)
ordenado = True 

for i in range (n-1): 
    if vetor[i] > vetor[i+1]:
        ordenado = False
        break 

if ordenado:
    print(" ORDENADO")
else: 
    print("  N ORDENADO ")