''' 
Exemplo:

Entrada – run.codes:
11 3 9 10 21 31 32 9 4 3 13 14 9 10 13 32 54 23 25
Entrada comentada para melhor visualização:
QTDE_CONTAINERS 11 
TAM_CONTAINER 3
QTDE_INSERCOES 9
9 ELEMENTOS INSERIDOS: 10 21 31 32 9 4 3 13 14 
ELEMENTOS QUE SOBRARAM PARA A BUSCA: 9 10 13 32 54 23 25

11 3 9 | 10 21 31 32 9 4 3 13 14 | 9 10 13 32 54 23 25

Saída:
2 1 1 3 3 1 3


'''


class HashTableUsingOpenAddress():
  ''' 
    A hash table based on open addressing (also known as closed hashing)
    stores all elements directly in the hash table array.
  '''
  def __init__(self, containers_n, container_s):
    self.hash_table = [];
    self.containers_number = containers_n;
    self.container_size = container_s;
    
    # create containers shape
    for container in range(self.containers_number):
      # add container to hash table
      self.hash_table.append( [ None for i in range( self.container_size ) ] );

  def insert_key_element(self, key):
    
    containerIndex = key % self.containers_number;
    iterator = 0;
    while iterator < self.container_size:
      if self.hash_table[ containerIndex ][ iterator ] == None:
        self.hash_table[ containerIndex ][ iterator ] = key;
        break;

      iterator += 1;


  def searchComplexityCounter(self , search_element):
    
    containerIndex = search_element % self.containers_number;
    iterator = 0;
    while iterator < self.container_size:
      element = self.hash_table[ containerIndex ][ iterator ]
      if element == None:
        return iterator + 1
      elif element == search_element:
        return iterator + 1
      else:
        iterator += 1
    
    # 2 1 1 3 3 1 3

    return iterator


def main():
  entry = list(map( int, input().split() ));
  # entry = list(map(int, input().split())); # '11 3 9 10 21 31 32 9 4 3 13 14 9 10 13 32 54 23 25'

  containers_n, container_s, insert_n_elements = entry[0:3];

  # Cria uma instância da classe
  obj = HashTableUsingOpenAddress(containers_n, container_s)

  # deleta os valores da lista de entrada que já estão instanciados em variáveis.
  del(entry[0:3])
  

   # fatiamento da lista referente aos valores que serão inseridos na tabela hash
  for i in entry[ 0 : insert_n_elements ]:
    obj.insert_key_element(i)

  # deleta da lista de entrada os valores que foram inseridos
  del(entry[ 0 : insert_n_elements ])

  # print(entry)
  # percorre o restante da lista passando os elementos a serem pesquisados
  comparisons_number = ''
  for element in entry:
    if entry.index(element) != (len(entry) - 1 ):
      comparisons_number += str( obj.searchComplexityCounter( element ) ) + ' '
    else:
      comparisons_number += str( obj.searchComplexityCounter( element ))

  # print('search 25', obj.searchComplexityCounter( 25 ))
  
  # print(obj.hash_table)
  
  print(comparisons_number)


if __name__ == '__main__':
  main()
