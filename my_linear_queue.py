class LinearQueue:
    def __init__(self, capacity = 10) -> None:
        self.capacity = capacity
        self.list = [None] * capacity
        self.front = -1
        self.rear = -1
    
    def is_empty(self) -> bool:
        return self.front == self.rear
    
    def is_full(self) -> bool:
        return self.rear == self.capacity -1
    
    def enqueue(self, item) -> None:
        if self.is_full():
            print("Error: Queue is full")
            return
        
        self.rear += 1
        self.list[self.rear] = item
    
    def dequeue(self) -> int:
        if self.is_empty():
            print("Error: Queue is empty")
            return
        
        self.front += 1
        temp = self.list[self.front]
        self.list[self.front] = None
        return temp
    
    def peek(self) -> int:
        if self.is_empty():
            print("Error: Queue is empty")
            return
        
        return self.list[self.front + 1]
    
    def clear(self):
        while not self.is_empty():
            self.dequeue()
        self.front = -1
        self.rear = -1

    def index(self, target):
        for i, element in enumerate(self.list):
            if element == target: return i
    
        return -1

    def __str__(self) -> str:
        result = ""

        for i in range(self.capacity - 1):
            result += " {0}".format(self.list[i])
            if i == self.front:
                result += "(front)"
            if i == self.rear:
                result += "(rear)"
            result += " |"
                
        result += " {0}".format(self.list[-1])
        if i == self.front:
            result += "(front)"
        if i == self.rear:
            result += "(rear)"

        length = len(result)
        result = "-" * length + "\n" + result
        result += "\n" + "-" * length
        
        return result
    
queue = LinearQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue)
print(queue.dequeue())
print(queue.dequeue())
print(queue)
print(queue.index(1))
print(queue.index(3))

# def init():
#     print('-' * 30)
#     print("""enqueue: 삽입
# dequeue: 삭제 후 반환
# peek: 반환
# clear: 큐 초기화
# reverse: 큐 역순으로 배열
# print: 큐 출력
# exit: 시스템 종료
# ------------------------------""")
    
# queue = LinearQueue()

# init()
# print(">>> ", end="")

# while True:
#     c = input()
    
#     if c == "enqueue":
#         queue.enqueue(int(input("정수를 입력해주세요: ")))
#         init()
    
#     elif c == "dequeue": print(queue.dequeue())

#     elif  c == "peek": print(queue.peek())

#     elif c == "clear":
#         queue.clear()
#         init()
    
#     elif c == "reverse":
#         queue.reverse()
#         init()
    
#     elif c == "print": print(queue)
        
    
#     elif c == "exit": break

#     else: print("Error: Invalid input")
    
#     print(">>> ", end="")