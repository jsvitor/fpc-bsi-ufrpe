"""
Fundamentals of Computational Problems I -
Information System at Rural Federal University of Pernambuco
Student: https://github.com/jsvitor

problem:
  input:
    5 1 2 3 4 5 6 7
  output:
    3
"""
from math import floor

def binary_search_comparison_count(array, element, amount=0):
  # print(array, element)
  n = len(array)
  middle_term_index = floor(n/2)
  amount += 1
  if array == []: return ( amount - 1 )
  
  elif element == array[middle_term_index]: return amount

  elif element < array[middle_term_index]:
    # search on the left of the array
    return binary_search_comparison_count(array[:middle_term_index], element, amount) 

  else:
    next_index = middle_term_index + 1
    return binary_search_comparison_count(array[next_index:], element, amount)


def main():
  inputList = list(map(int, input().split())) # o primeiro elemento é o que deve ser encontrado. fazer um pop nele
  # inputList = list(map(int, '5 1 2 3 4 5 6 7'.split()))
  # inputList = list(map(int,'12 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99'.split()))
  
  search_element = inputList.pop(0)
  print(binary_search_comparison_count(inputList, search_element))


if __name__ == '__main__': main()