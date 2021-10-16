class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def top(self):
        if not self.is_empty():
            return self.items[-1]

def is_match(a, b):
        return True if a + b in ['()', '[]', '{}']\
            else False


def is_balanced(bal) :
    s = Stack()
    is_balanced = True
    i = 0

    while i < len(bal) and is_balanced:
        p = bal[i]
        if p not in "({[]})":
            i+=1
            continue
        elif p in "([{":
            s.push(p)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, p):
                    is_balanced = False
        i += 1

    if s.is_empty() and is_balanced:
        return True
    else:
        return False

print(is_balanced("({a+b})"))
print(is_balanced("))((a+b}{"))
print(is_balanced("((a+b))"))
print(is_balanced("))"))
print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))

