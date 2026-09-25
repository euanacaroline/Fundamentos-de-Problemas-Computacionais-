

def divisivel8(k):
    if k < 0:
        return divisivel8(-k)
    if k == 0:
        return True 
    if k < 8: 
        return False 
    return divisivel8(k - 8)

print(divisivel8(-90))
print(divisivel8(56))

def div8_mult(k, n=0 ):  
    produto = n * 8 

    if produto == k : 
       return True 
    if produto > k :
        return False 

    return div8_mult(k, n + 1)

print(div8_mult(-8, 0))   