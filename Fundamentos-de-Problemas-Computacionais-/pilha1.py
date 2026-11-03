pilha_acao = []

print(" adicione o que vc quer fazer (passo a passo) e quando quiser finalizar digite 'fim' . ")

while True: 
    acao = input("o que vc quer fazer agr? : ")

    if acao.lower() == 'fim':
        break

    pilha_acao.append(acao)

print("ações executadas: ", pilha_acao)