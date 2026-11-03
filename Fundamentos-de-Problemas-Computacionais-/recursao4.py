def divisivel3(n):
    if n < 10: 
        if n in (0, 3, 6, 9):
            return True 
        else: 
            return False 

    soma = (n%10) + (n//10)
    return divisivel3(soma)

print(divisivel3(97))