def fatorial(n):
    if n < 1: 
        return "Não foi possível realizar o fatorial"
    elif n ==1: 
        return  1 
    else : 
       return n * fatorial(n-1)

print (fatorial(99))