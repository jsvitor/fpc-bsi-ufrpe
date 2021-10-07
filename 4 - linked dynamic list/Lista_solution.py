#Classe Nodo e Lista
#Algoritmos e Estrutura de Dados
#Prof. Tiago A. E. Ferreira

class Node:
    """ Classe que define um nodo simples de uma Estrutura de dados: (info, NextNodo)"""

    def __init__(self, data):
        """Construtor do Nodo"""
        self.data = data
        self.nextNode = None
    
    def getData(self):
        "Retorna o Dado armazenado no nodo"
        return self.data
    
    def setData(self,data):
        "Atribui valor ao Dado do nodo"
        self.data=data
    
    def getNextNode(self):
        "Retorna a referencia do proximo nodo"
        return self.nextNode
        
    def setNextNode(self,newNode):
        "Ajusta a referencia do proximo nodo"
        self.nextNode = newNode;
    
    
class List:
    """Classe para uma Lista Encadeada:
            Esta classe tem dois ponteiros:
                firstNode: aponta para o primeiro nodo da lista
                lastNode: aponta para o ultimo nodo da lista
            Ao iniciar a lista ambos os ponteiros apontam para NULO"""
    
    def __init__(self):
        "Construtor da Lista"
        self.firstNode = None
        self.lastNode = None
        
    def getAsText(self): #devolve uma string pronta para impressao na tela:
        saida = ""
        if self.isEmpty(): 
            return saida
        else:
            currentNode = self.firstNode
            while currentNode is not None: 
                saida += str(currentNode.getData()) + " => "
                currentNode = currentNode.getNextNode()
        return saida[:-4] #retira o " => " depois do ultimo

    
    def insertAtBegin(self, value):
        "Insere elemento no Inicio da lista"
        newNode = Node(value) # instancia de um novo nodo
        if self.isEmpty(): #Insercao para Lista vazia
            self.firstNode = self.lastNode = newNode
        else:                   #Insercao para lista nao vazia
            newNode.setNextNode(self.firstNode)
            self.firstNode = newNode
    
    
    def insertAtEnd(self, value):
        "Insere emento no Fim da lista"
        newNode = Node(value)  #instancia de um novo nodo
        
        if self.isEmpty():  #Se a lista esta vazia
            self.firstNode = self.lastNode = newNode
        else:
            self.lastNode.setNextNode(newNode)
            self.lastNode=newNode
            
    def removeFromBegin(self):
        "Remove o nodo inicial da lista"
        if self.isEmpty():
            raise IndexError # Remocao de uma Lista Vazia
        firstNodeValue = self.firstNode.getData()
        if self.firstNode is self.lastNode:
            self.firstNode = self.lastNode = None
        else:
            self.firstNode = self.firstNode.getNextNode()
        return firstNodeValue
        
    def removeFromEnd(self):
        "Remove o ultimo nodo da lista"
        if self.isEmpty():
            raise IndexError # Remocao de lista vazia!
        lastNodeValue = self.lastNode.getData()
        if self.firstNode is self.lastNode:
            self.firstNode=self.lastNode=None
        else:
            currentNode = self.firstNode
            while currentNode.getNextNode() is not self.lastNode:
                currentNode = currentNode.getNextNode()
            currentNode.setNextNode(None)
            self.lastNode = currentNode
        return lastNodeValue
    
    def isEmpty(self):
        "A lista esta vazia? True or False"
        return self.firstNode is None


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
# from Lista import List;


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

