pilha = []

def inserir(x):
    pilha.insert(0 , x)

def remover():
    pilha.pop(0)

inserir('1')
inserir('2')
inserir('3')

remover()
remover()

print("Pilha final:", pilha)
