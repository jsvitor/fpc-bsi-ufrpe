"""
Fundamentals of Computational Problems I -
Information System at Rural Federal University of Pernambuco
Student: jsvitor

problem:
f(n) = “b”, se n = 0
f(n) = “a”, se n = 1
f(n) = f(n-1) + f(n-2), se n > 1
"""

def words_of_fib(n):
  # n: nth term
  if n == 0:
    return 'b'
  elif n == 1:
    return 'a'
  else:
    return  f'{words_of_fib( n - 1 )}{words_of_fib( n - 2 )}'

def main():
  nth_term = int(input())
  print(words_of_fib(nth_term))

if __name__ == '__main__':
  main()

# print(words_of_fib(0)) # output: b
# print(words_of_fib(3)) # output: aba
# print(words_of_fib(5)) # output: abaababa
