

# classes Biblioteca e Livro:
# - A Biblioteca contem uma lista de livros disponiveis e uma lista de livros alugados
# - A biblioteca possui um metodo para alugar um livro. Caso o livro jah esteja alugado a pessoa nao poderah alugar este livro.
# - A biblioteca possui um metodo para devolver o livro.
# - A biblioteca possui um metodo que devolve o nome do livro mais alugado.
# - A biblioteca tera' uma funcao que devolve uma lista de livros alugados ordenados pela data de devolucao

from datetime import date

def converter_data(data_str):
    partes = data_str.split("/")
    return (int(partes[2]), int(partes[1]), int(partes[0]))

class Livro:
    codigo = None
    nome = None
    autor = None
    dataAluguel = None
    dataDevolucao = None
    __qtdeAlugueis = 0

    def __init__(self, codigo, nome, autor):
        self.codigo = codigo
        self.nome = nome
        self.autor = autor
        
    def incrementaAluguel(self):
        self.__qtdeAlugueis += 1
    def getQtdeAlugueis(self):
        return self.__qtdeAlugueis

class Biblioteca:
    alugados = []
    disponiveis = []

    def inserir(self, livro):
        self.disponiveis.append(livro)

    def alugar(self, codLivro, dataDevolucao): #dataDevolucao eh uma string no formato dd/mm/aaaa
        ok = True
        mensagem = None
        #if livro in self.disponiveis:
        for i in self.disponiveis:
            if i.codigo == codLivro:
                i.incrementaAluguel()
                i.dataAluguel = date.today()
                i.dataDevolucao = dataDevolucao
                self.alugados.append(i)
                self.disponiveis.remove(i)
                break
        else:
            ok = False
            mensagem = "O livro nao existe"
        return (ok, mensagem)

    def devolver(self, codLivro):
        ok = True
        mensagem = None
        for livro in self.alugados:
            if livro.codigo == codLivro:
                self.disponiveis.append(livro)
                self.alugados.remove(livro)
                break
        else:
            ok = False
            mensagem = "O livro nao esta alugado"
        return (ok, mensagem)

    def livroMaisAlugado(self):
        ok = True
        mensagem = None
        maior = 0
        nome = None
        for livro in self.disponiveis:
            if livro.getQtdeAlugueis() > maior:
                maior = livro.getQtdeAlugueis()
                nome = livro.nome
        for livro in self.alugados:
            if livro.getQtdeAlugueis() > maior:
                maior = livro.getQtdeAlugueis()
                nome = livro.nome
        if maior == 0:
            ok = False
            mensagem = "Nenhum livro foi alugado ainda"
        else:
            mensagem = "O livro mais alugado e: %s (%d alugueis)"%(nome, maior)
            return (ok, mensagem)
            
    def livrosOrdenadosPorDataDeDevolucao(self):
        lista = self.alugados[:]
        n = len(lista)

        for i in range(n-1):
            for j in range(0, n -1 -i):
                d1 =  converter_data(lista[j].dataDevolucao)
                d2 =  converter_data(lista[j+1].dataDevolucao)

                if d1 > d2:
                    lista[j], lista[j+1] = lista[j+1], lista[j]

        return lista
    
entrada = input()
dados = entrada.split(",")
b = Biblioteca()
qtd_livros = int(dados[0])
posicao = 1 

for _ in range(qtd_livros):
    codigo = int(dados[posicao])
    nome = dados[posicao + 1]
    autor = dados[posicao + 2]

    l = Livro(codigo, nome, autor)
    b.inserir(l)
    posicao += 3

while posicao < len(dados):
    cod_aluguel = int(dados[posicao])
    data_devolucao = dados[posicao + 1]
    b.alugar(cod_aluguel, data_devolucao)
    posicao += 2

resultado = b.livrosOrdenadosPorDataDeDevolucao()
codigos = [str(livro.codigo) for livro in resultado]
print(" ".join(codigos))

###exemplo de execucao:
##>>> l = Livro(123, "Calculo 1", "Stwart")

##>>> b = Biblioteca()

##>>> b.inserir(l)

##>>> b.alugar(l, "10/01/2023")
##(True, None)

##>>> l2 = Livro(456, "Fisica", "Tipler")

##>>> b.inserir(l2)

##>>> b.alugar(l2, "01/02/2023")
##(True, None)

##>>> b.alugar(l)
##(False, 'O livro ja esta alugado, infelizmente voce nao podera alugar')

##>>> b.devolver(l.codigo)
##(True, None)

##>>> b.alugar(l, "30/01/2023")
##(True, None)

##>>> b.devolver(l.codigo)
##(True, None)

##>>> b.livroMaisAlugado()
##(True, 'O livro mais alugado e: Calculo 1 (2 alugueis)')

##>>> b.devolver(l2.codigo)
##(True, None)

##>>> b.devolver(l.codigo)
##(False, 'O livro nao esta alugado')

##>>> b.devolver(l2.codigo)
##(False, 'O livro nao esta alugado')

##>>> b.alugar(l2, "01/02/2023")
##(True, None)

##>>> b.alugar(l2, "01/02/2023")
##(False, 'O livro ja esta alugado, infelizmente voce nao podera alugar')

##>>> b.devolver(l2.codigo)
##(True, None)

##>>> def getNome(livro):
##>>>     return livro.nome

##>>> b.disponiveis.sort(key=getNome)

##>>> for l in b.disponiveis:
##     print(l.nome)
##Calculo 1
##Calculo 1
##Fisica