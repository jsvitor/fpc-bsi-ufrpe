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
        
