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
    
    def livrosOrdenadosPeloNome(self, array):
        # array → [{cod, nome, autor}, {cod, nome, autor}, {cod, nome, autor}]
        
        n = len(array)
        ### PROCESSO DE ORDENAÇÃO DO ARRAY DE OBJETOS DO TIPO Livro PELO NOME
        for l in range(n-1):
           for i in range(n-1):
                if array[i].nome > array[i+1].nome:
                    # troca de elementos nas posições i e i+1
                    array[i], array[i+1] = array[i+1], array[i]

        return array




def main():
    """ 
        Entrada: qnt, código,nome,autor
        3,234,Fortaleza Digital,Dan Brown,423,Calculo 1,Stwart,156,Fisica,Tipler

        Saída:
        423 156 234
    """

    #   a) criar um programa principal para tratar as entradas e saídas do programa;

    entry = input().split(',')
    books = entry[1:] # recorta apenas os livros

    #   b) alterar a classe Biblioteca para adicionar o novo método livrosOrdenadosPeloNome
    #   c) no programa principal, criar objetos das classes Livro e Biblioteca usando o código fonte fornecido;
    # criando um objeto do tipo Biblioteca:
    library = Biblioteca()

    ## inserindo os objetos do tipo Livro num objeto do tipo Biblioteca
    count = 0
    while count < int(entry[0]):
        cod, name, author = books[0:3]
        book = Livro(cod, name, author)
        
        # inserindo livro na biblioteca
        library.inserir(book)
        del(books[0:3])
        count += 1
    

    # d) no programa principal, realizar a ordenação das listas de livros alugados e disponiveis
    # separadamente;
    library.disponiveis = library.livrosOrdenadosPeloNome(library.disponiveis)

    library.alugados = library.livrosOrdenadosPeloNome(library.alugados)

    # e) no programa principal, mesclar os resultados das duas listas ordenadas;
    """
    lista = []
    left = library.disponiveis
    right = library.alugados
    top_left, top_right = 0, 0

    for k in range(len(left)+len(right)): """
    def merge(lista, inicio, meio, fim):
        left = lista[inicio:meio]
        right = lista[meio:fim]
        top_left, top_right = 0, 0
        for k in range(inicio, fim):
            if top_left >= len(left):
                lista[k] = right[top_right]
                top_right += 1
            elif top_right >= len(right):
                lista[k] = left[top_left]
                top_left += 1
            # comparando os nomes
            elif left[top_left].nome < right[top_right].nome:
                lista[k] = left[top_left]
                top_left += 1
            else:
                lista[k] = right[top_right]
                top_right += 1
    
    lista = library.disponiveis + library.alugados
    merge(lista, 0, len(library.disponiveis), len(lista))
    # print([x.codigo for x in lista ])


    # f) exibir a saída conforme formato definido.
    cod = ''
    for livro in lista:
        if lista.index(livro) != (len(lista) - 1 ):
            cod += str( livro.codigo ) + ' '
        else:
            cod += str( livro.codigo )

    print(cod)

if __name__ == '__main__':
  main()
