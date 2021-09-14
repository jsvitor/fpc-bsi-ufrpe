def sum_value_of_complexity(array):
  amount = 0
  for i in array:    
    if i == 'IO': amount += 30
    
    elif i == 'MEM': amount += 10

    elif i == 'PROCSUM': amount += 1
    
    elif i == 'PROCMULT': amount += 10

  return amount

def complexity_verify(array):
  amount = 0; # amount of algorithm complexity by time unity
  # The "array" is a list and has a set of algorithm instructions where the complexity will be calculated
  # example:
  #         input --> array = ['INICIO', 'IO', 'LOOP', '10', 'PROCSUM', 'FIMLOOP', 'FIM']
  #         output -> 40
  if 'INICIO' in array[0]:
    instruction = 0
    # scrolls through the list analyzing each operation
    while instruction < len(array):
      if array[instruction] == 'FIM': break

      elif array[instruction] == 'INICIO': instruction += 1
      
      elif array[instruction] == 'FIMLOOP': instruction += 1
      
      elif array[instruction] == 'IO':
        amount += 30
        instruction += 1

      elif array[instruction] == 'MEM':
        amount += 10
        instruction += 1

      elif array[instruction] == 'PROCSUM':
        amount += 1
        instruction += 1

      elif array[instruction] == 'PROCMULT':
        amount += 10
        instruction += 1

      elif array[instruction] == 'LOOP':
        position = instruction + 1; repetition = int(array[position])
        position += 1; end = array.index('FIMLOOP')
        array[end] = 'was_an_end'
        # print('end', end)
        # return the sum of its internal operations.
        # slice the list in the loop operations: array[position:end]
        loop_complexity = sum_value_of_complexity(array[position:end])
        # print(array[position:])
        amount += repetition * loop_complexity # multiply the loop value by the sum of its internal operations.
        # On the next iteration, the position will be jumped to the next position after the 'LOOPFIM'
        position -= 2; end += 1; instruction += ( end - position )
        # print(instruction)

      else:
        return 'error'
      # print('instruction', instruction)

  else:
    pass

  return amount


def main():
  algorithm_list = input().split() # 
  print(complexity_verify(algorithm_list))


if __name__ == "__main__":
  main()
