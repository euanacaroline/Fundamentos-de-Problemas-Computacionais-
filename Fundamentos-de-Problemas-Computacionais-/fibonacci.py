def fibonacci(n):
    if n == 1 or n==0: 
        return 1 
    elif n < 0: 
        return "n foi possivel realizar a conta"
    else: 
        return fibonacci(n-1)+ fibonacci(n-2)

print (fibonacci(2))