"""
Fundamentals of Computational Problems I -
Information System at Rural Federal University of Pernambuco
Student: https://github.com/jsvitor
problem:
    1 – Inserir no início da lista;
    2 – Inserir no fim da lista;
    3 – Remover do início da lista;
    4 – Remover do fim da lista
  exemplo 1
  input:
    2 1 2 2 2 3 2 4 2 5 2 6 1 7 4 4
  output:
    7 => 1 => 2 => 3 => 4
  exemplo 2
  input: 2 3 1 2 1 4 2 7
  output: 4 = > 2 => 3 => 7

solution:
    adicionar os dados de entrada a uma lista
    teremos uma lista de entrada - onde os dados serão tratados e uma lista que será formada pelo script
    percorrer essa lista de entrada, e a partir dela e formando a lista com a classe List
    onde na primeira passada, o dado encontrado é uma instrução
    e deve ser passado por condicionais
    se for uma instrução 1 ou 2, deve ser executada as operações correspondetes e 
    na próxima passada, deve pular o próximo valor
    se for do uma instrução do tipo 3 e 4, deve passar para o próximo normalmente?
    no final imprimir o retorno do método getAsText()
"""

# import sys;
from Lista import List;


def getInstructions(array):
  """
    recebe um array com instruções para criação de uma lista usando a classe List.
  """
  LISTA = List();
  instruction = i = 0;

  while instruction < len(array):
    try:
      if array[i] == '1':
        LISTA.insertAtBegin(array[ i + 1 ]) # é pegar o próximo
        i += 2
      elif array[i] == '2':
        # inserir no fim da lista
        LISTA.insertAtEnd(array[ i + 1])
        i += 2
      elif array[i] == '3':
        # remover do início da lista
        LISTA.removeFromBegin()
        i += 1
      elif array[i] == '4':
        # remover do final da lista, como se fosse um pop(-1)
        LISTA.removeFromEnd()
        i += 1
    except Exception:
      return LISTA.getAsText()
  
  return LISTA.getAsText()

def main():
  # tratamento da entrada e chama a função para executar a função
  input_list = input().split(); # 2 1 2 2 2 3 2 4 2 5 2 6 1 7 4 4
  print(getInstructions(input_list))


if __name__ == '__main__': main()
