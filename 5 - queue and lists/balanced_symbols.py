# Evaluation challenge for the discipline of Fundamentals of Computational Problems I.
# In the course of Information system at the Federal Rural University of Pernambuco.
# Student: José Vitor - @jsvitor
# Teacher: Cícero Garrozi -

import sys


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
            if (not s.isEmpty()) and symbol == ')' and s.peek() == '(':
                s.pop()
            elif (not s.isEmpty()) and symbol == ']' and s.peek() == '[':
                s.pop()
            elif (not s.isEmpty()) and symbol == '}' and s.peek() == '{':
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
    # string = input().lower()
    string = sys.argv[1].lower()
    result = parChecker(string)
    try:
        if result == 1:
            print('well-formad string')
        elif result == 0:
            print('malformed string')
    except Exception as e:
        print('[!] Error [!]{}'.format(e))


if __name__ == "__main__":
    main()

# $ python .\balancedSymbols.py "( ( [ ] ) [ ( ) ] ) [ (  ]"
# $ malformed string
#
# $ python .\balancedSymbols.py "( ( [ ] ) [ ( ) ] ) [ ( ) ]"
# $ well-formed string
