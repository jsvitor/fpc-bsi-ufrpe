# classes Biblioteca e Livro:
# - A Biblioteca contem uma lista de livros disponiveis e uma lista de livros alugados
# - A biblioteca possui um metodo para alugar um livro. Caso o livro jah esteja alugado a pessoa nao poderah alugar este livro.
# - A biblioteca possui um metodo para devolver o livro.
# - A biblioteca possui um metodo que devolve o nome do livro mais alugado.

class Livro:
    codigo = None
    nome = None
    autor = None
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

    def alugar(self, livro):
        ok = True
        mensagem = None
        if livro in self.disponiveis:
            for i in self.disponiveis:
                if i == livro:
                    i.incrementaAluguel()
                    self.alugados.append(i)
                    self.disponiveis.remove(i)
                    break
        elif livro in self.alugados:
            ok = False
            mensagem = "O livro ja esta alugado, infelizmente voce nao podera alugar"
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

###exemplo de execucao:
##>>> l = Livro(123, "Calculo 1", "Stwart")

##>>> b = Biblioteca()

##>>> b.inserir(l)

##>>> b.alugar(l)
##(True, None)

##>>> l2 = Livro(456, "Fisica", "Tipler")

##>>> b.inserir(l)

##>>> b.inserir(l2)

##>>> b.alugar(l)
##(True, None)

##>>> b.alugar(l)
##(False, 'O livro ja esta alugado, infelizmente voce nao podera alugar')

##>>> b.devolver(l.codigo)
##(True, None)

##>>> b.livroMaisAlugado()
##(True, 'O livro mais alugado e: Calculo 1 (2 alugueis)')

##>>> b.devolver(l.codigo)
##(True, None)

##>>> b.devolver(l.codigo)
##(False, 'O livro nao esta alugado')

##>>> b.devolver(l2.codigo)
##(False, 'O livro nao esta alugado')

##>>> b.alugar(l2)
##(True, None)

##>>> b.alugar(l2)
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

