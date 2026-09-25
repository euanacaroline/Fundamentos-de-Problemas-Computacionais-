#Crie uma função contar_digitos(n) que retorne a 
# quantidade de dígitos de um número.

def contar_numeros(n):
    if n < 10: 
        return 1 
    else: 
        return 1 + contar_numeros(n//10)

print (contar_numeros(8678))
