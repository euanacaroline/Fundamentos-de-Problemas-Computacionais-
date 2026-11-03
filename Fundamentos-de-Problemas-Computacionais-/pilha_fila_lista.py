entrada = input()
pilha = []
valido = True

for char in entrada: 
    if char in "([{":
        pilha.append(char)
    elif char in ")]}": 
        if len(pilha) == 0: 
            valido = False 
            break 

        topo = pilha.pop()

        if (char == ')' and topo != '(') or \
           (char == ']' and topo != '[') or \
           (char == '}' and topo != '{'): 
            valido = False 
            break 

if valido and len(pilha) == 0: 
    print("Casamento perfeito")
else: 
    print("Casamento imperfeito")



