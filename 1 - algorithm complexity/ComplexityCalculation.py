# Evaluation challenge for the discipline of Fundamentals of Computational Problems I.
# In the course of Information system at Federal Rural University of Pernambuco.
# Student: José Vitor - @jszvitor
# Teacher: Cícero Garrozi - 
# 02-Complexity - simple version - [run.codes] - 2º implementation

def ComplexityCalc(algorithm):
    result = 0
    stack = []
    if 'inicio' == algorithm[0]:
        algorithm.pop()
        algorithm.pop(0)
        while len(algorithm) > 0 or len(stack) > 0:
            try:
                if algorithm[0] == 'op':
                    stack.append(algorithm[1]); stack.append('+')
                    algorithm.pop(0); algorithm.pop(0)
                elif algorithm[0] == 'loop':
                    stack.append(algorithm[1]); stack.append('*')
                    algorithm.pop(0); algorithm.pop(0)
                elif algorithm[0] == 'fim':
                    while True:
                        if stack[-1] == '*':
                            stack.pop(); result *= int(stack.pop())
                            break
                        elif not(stack[-1] != '+'):
                            stack.pop(); result += int(stack.pop())        
                    algorithm.pop(0)
            except IndexError:
                if stack[-1] == '+':
                    stack.pop(); result += int(stack.pop())
            except Exception as e:
                return e
            else:
                pass
    return result

def main():
    algorithm = input().lower().split() # "INICIO OP 3 LOOP 2 LOOP 10 OP 1 FIM FIM FIM"
    print(ComplexityCalc(algorithm))

if __name__ == "__main__":
    main()
