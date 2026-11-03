#divisivel por 3 a partir da soma 

#entrada =int(input(" "))
#def divisivel3(n): 
   # if n < 0 : 
   #     return divisivel3(-soma)
   # if n == 0: 
  #      return True 
  #  if n < 3:
   #     return False 
#
  #  return divisivel3(n - 3)

#print(divisivel3(entrada))


def div3_soma(n):
    n = abs(int(n))

    if n < 10:
        return n in (0, 3, 6, 9)

    soma = sum(int(digito) for digito in str(n))

    return div3_soma(soma)

numero = input(" ")

if div3_soma(numero):
    print("é div 3")
else: 
    print("n é")

print(div3_soma(numero))