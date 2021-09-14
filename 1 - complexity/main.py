def sum_value_of_complexity(array):
  amount = 0
  for i in array:    
    if i == 'IO': amount += 30
    
    elif i == 'MEM': amount += 10

    elif i == 'PROCSUM': amount += 1
    
    elif i == 'PROCMULT': amount += 10
    
  return amount

def complexity_verify(array):
  amount = 0; # complexity in time unity
  # i is a instruction of the algorithm
  new_array = array.copy()
  # stack = []
  rep_for = 0
  if 'INICIO' in array[0]:
    interaction = 0
    while interaction < len(array):
      if array[interaction] == 'FIM': break

      elif array[interaction] == 'INICIO':
        interaction += 1
      elif array[interaction] == 'FIMLOOP':
        interaction += 1

      elif array[interaction] == 'IO':
        # stack.append('30')
        amount += 30
        interaction += 1
      
      elif array[interaction] == 'MEM':
        # new_array.pop( new_array.index(i) )
        amount += 10
        interaction += 1

      elif array[interaction] == 'PROCSUM':
        #new_array.pop( new_array.index(i) )
        amount += 1
        interaction += 1
      
      elif array[interaction] == 'PROCMULT':
        # new_array.pop( new_array.index(i) )
        amount += 10
        interaction += 1

      elif array[interaction] == 'LOOP':
        position = interaction + 1
        repetition = int(new_array[position])
        # multiplicar o valor do loop pela soma das operações internas dele
        position += 1
        end = array.index('FIMLOOP')
        array[end] = 'was_an_end'
        # print('end', end)
        loop_complexity = sum_value_of_complexity(array[position:end])
        # print(array[position:])
        amount += repetition * loop_complexity
        position -= 2
        end += 1
        # del(array[ position:end ])
        interaction += ( end - position )
        # print(interaction)

      else:
        return 'error'
      # print('interaction', interaction)
      # rep_for += 1
      
      


  else:
    pass

  return amount

def main():
  algorithm_list = input().split() # 
  print(complexity_verify(algorithm_list))


if __name__ == "__main__":
  main()
