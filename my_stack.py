class Stack:
    def __init__(self, capacity = 5) -> None:
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
            return "Error: Stack is empty"
        
        self.top -= 1
        return self.list[self.top+1]
    
    def peek(self) -> int:
        if self.isEmpty():
            return "Error: Stack is empty"
        
        return self.list[self.top]  

stack = Stack()

while not stack.isFull():
    stack.push(int(input("정수 입력: ")))

while not stack.isEmpty():
    print(stack.pop())