# Evaluation challenge for the discipline of Fundamentals of Computational Problems I.
# In the course of Information system at Federal Rural University of Pernambuco.
# Student: José Vitor - @jszvitor
# Teacher: Cícero Garrozi - 

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
    
    def stack(self):
        return self.items

def parChecker(symbols):
    s = Stack()
    index = 0
    while index < len(symbols):
        symbol = symbols[index]
        if symbol == '(' or symbol == '[' or symbol == '{':
            s.push(symbol)
        else:
            if (not s.isEmpty()) and symbol == ')' and s.stack()[-1] == '(':
                s.pop()
            elif (not s.isEmpty()) and symbol == ']' and s.stack()[-1] == '[':
                s.pop()
            elif (not s.isEmpty()) and symbol == '}' and s.stack()[-1] == '{':
                s.pop()
            elif symbol == ')' or symbol == ']' or symbol == '}':
                s.push(symbol)
                break
        index += 1
    if s.isEmpty():
        return True
    else:
        return False

def main():
    cadeia = input().lower()
    result = parChecker(cadeia)
    try:
        if result == 1:
            print('string bem formada')
        elif result == 0:
            print('string mal formada')
    except Exception as e:
        print('[!] Error [!]{}'.format(e))

if __name__ == "__main__":
    main()
