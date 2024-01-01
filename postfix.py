class ArrayStack:
    def __init__(self, capacity = 10) -> None:
        self.capacity = capacity
        self.list = [None]*capacity
        self.top = -1

    def isEmpty(self) -> bool:
        return self.top == -1
    
    def isFull(self) -> bool:
        return self.top == self.capacity-1
    
    def push(self, item) -> None:
        if self.isFull():
            print("Error: Stack is full")
            return
        
        self.top += 1
        self.list[self.top] = item
    
    def pop(self) -> int:
        if self.isEmpty():
            print("Error: Stack is empty")
            return
        
        temp = self.list[self.top]
        self.list[self.top] = None
        self.top -= 1
        return temp
    
    def peek(self) -> int:
        if self.isEmpty():
            print("Error: Stack is empty")
            return
        
        return self.list[self.top]
        
    def delete_all(self) -> None:
        while not self.isEmpty():
            self.pop()
    
    def reverse(self) -> None:
        self.list[:self.top+1] = self.list[self.top::-1]
    
    def __str__(self) -> str:
        result = ""
        
        for i in reversed(range(self.capacity)):
            result += "| {0} |".format(self.list[i])
            result += " <- top\n" if i == self.top else "\n"

        return result

def precedence(op):
    '''연산자 우선순위 계산함수'''
    if op in '()': return 0
    elif op in '+-': return 1
    elif op in '*/': return 2
    else: return -1

def Infix2Postfix(expr):
    '''중위표기 -> 후위표기로 바꾸는 함수'''
    s = ArrayStack(100)
    output = []

    for term in expr:
        if term == '(':
            s.push(term)
        
        elif term == ')':
            while not s.isEmpty():
                op = s.pop()
                if op == '(':
                    break
                else:
                    output.append(op)
        
        elif term in "+-*/":
            while not s.isEmpty():
                op = s.peek()
                if precedence(op) >= precedence(term):
                    output.append(op)
                    s.pop()
                else: break
            s.push(term)
        
        else:
            output.append(term)
    
    while not s.isEmpty():
        output.append(s.pop())
    
    return ''.join(output)

print(Infix2Postfix(list(input("수식 입력: "))))