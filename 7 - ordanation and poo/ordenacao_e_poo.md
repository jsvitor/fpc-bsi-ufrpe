Ordenação de Livros da Biblioteca
Considere as classes Biblioteca e Livro (em anexo):
- A biblioteca contém uma lista de livros disponíveis e uma lista de livros alugados
- A biblioteca possui um método para alugar um livro. Caso o livro já esteja alugado, a pessoa não
poderá alugar este livro.
- A biblioteca possui um método para devolver o livro.
- A biblioteca possui um método que devolve o nome do livro mais alugado.
A partir das classes já implementadas e disponibilizadas no arquivo biblioteca.py, implemente o
método “livrosOrdenadosPeloNome” na classe Biblioteca que deverá retornar uma única lista com
todos os livros da biblioteca (cada elemento da lista será um objeto livro) ordenados pelo nome de cada
livro.
Atenção: você não deve ordenar somente os nomes dos livros. Eles serão usados para a ordenação,
porém o objeto completo livro deverá ser movimentado pela lista durante a ordenação.
Crie um programa principal para realizar a inserção de livros e retornar a saída, conforme formatos de
entrada e saída abaixo. Neste exercício, você deve: 
a) criar um programa principal para tratar as entradas e saídas do programa;
b) alterar a classe Biblioteca para adicionar o novo método livrosOrdenadosPeloNome
c) no programa principal, criar objetos das classes Livro e Biblioteca usando o código fonte fornecido;
d) no programa principal, realizar a ordenação das listas de livros alugados e disponiveis
separadamente;
e) no programa principal, mesclar os resultados das duas listas ordenadas;
f) exibir a saída conforme formato definido.
REGRA GERAL: cada lista de livros da biblioteca (alugados e disponiveis) deverá ser ordenada
isoladamente usando algum algoritmo estudado em sala (não será permitido usar bibliotecas de
ordenação prontas, mas você poderá usar o código fonte que foi exibido em aula e adaptá-lo se for o
caso). Após a ordenação de ambas, você deverá usar o procedimento de mesclagem similar ao do
algoritmo mergesort para realizar a junção ordenada das duas listas. ATENÇÃO: você não deve
executar o algoritmo mergesort nas duas listas, o que seria extremamente ineficiente; deve usar
somente o procedimento de mesclagem (junção) de duas listas ordenadas, criando uma terceira
ordenada.
Entrada
O arquivo de entrada consiste de um número inteiro indicando a quantidade de livros a serem
cadastrados, seguidos de várias triplas (uma para cada livro) em uma única linha. Todos os valores na
entrada serão separados por vírgula. Cada tripla conterá as informações a seguir nesta ordem: 
código,nome,autor
onde código é o identificador numérico do livro (por ex, código de barras ou ISBN), nome é o título do
livro (string) e autor é o nome do(s) autor(es) do livro em uma única string. 
Saída
Seu programa deverá ordenar alfabeticamente todos os objetos livro da biblioteca considerando somente
o nome do livro no critério de ordenação (vide REGRA GERAL). A saída será composta somente pelos
códigos dos livros já ordenados pelo nome. Ela deverá exibir todos os códigos em uma única linha
separados por espaço entre os códigos. Observe que os códigos não estarão ordenados em ordem
crescente, porém os livros que eles representam estarão ordenados pelo nome. 
Exemplo:
Entrada:
3,234,Fortaleza Digital,Dan Brown,423,Calculo 1,Stwart,156,Fisica,Tipler
Saída:
423 156 234