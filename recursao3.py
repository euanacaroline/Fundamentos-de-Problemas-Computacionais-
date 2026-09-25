def soma_dig(n): 
    if n < 10: 
        return n 

    return (n%10) + soma_dig(n//10)

print (soma_dig(89))