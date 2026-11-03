historico_inserir = []
historico_voltar = []
site_atual = []

print("digite 'A' um site p visitar")
print("digite 'B' para VOLTAR")
print("digite 'F' para finalizar")
print("digite 'sair' para fechar o navegador\n")

while True:
    print(f"\n[ Site Atual: {site_atual if site_atual else 'Nenhum'} ]")
    comando = input("digite um comando ou um site (B/F/sair)").strip()

    if comando.lower() == 'sair':
        break 

    elif comando.upper() == 'B':
        if len(historico_voltar) > 0:
            if site_atual: 
                historico_inserir.append(site_atual)

            site_atual = historico_voltar.pop()
        else: 
            print("n tem como voltar")

    elif comando.upper() == 'F':
        if len(historico_inserir) > 0:
            if site_atual: 
                historico_voltar.append(site_atual)

            site_atual = historico_inserir.pop()
        else: 
            print("n tem como inserir")

    else:
        if site_atual: 
            historico_voltar.append(site_atual)

        site_atual = comando 

        historico_inserir.clear()
        