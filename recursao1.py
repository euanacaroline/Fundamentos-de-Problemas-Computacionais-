#atrecursao 
# fazer uma função q cheque se o numero é divisivel por 7 usando apenas /10 

entrada = int(input(" "))
def divisivel7 (numero): 
    if numero <= 70: 
        if numero in (0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70):
            return "s"
        else: 
            return "n"
        
    ultimo_dig = numero % 10 
    n_restante = numero //10 
    dig_format = ultimo_dig * 5 
    soma = n_restante + dig_format 

    return divisivel7(soma)

print (divisivel7(entrada))