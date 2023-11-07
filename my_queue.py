class Queue:
    def __init__(self, capacity = 5) -> None:
        self.capacity = capacity
        self.list = [None]*capacity
        self.front = 0
        self.rear = 0

    def isEmpty(self) -> bool:
        return self.front == self.rear

    def isFull(self) -> bool:
        return (self.rear+1) % self.capacity == self.front

    def enqueue(self, item) -> None:
        if self.isFull():
            print("Error: Queue is full")

        self.rear = (self.rear+1) % self.capacity
        self.list[self.rear] = item

    def dequeue(self) -> int:
        if self.isEmpty():
            return "Error: Queue is empty"
        
        self.front = (self.front+1) % self.capacity
        return self.list[self.front]


    def peek(self) -> int:
        if self.isEmpty():
            return "Error: Queue is empty"
        
        return self.list[(self.front+1) % self.capacity]
    
queue = Queue()

while not queue.isFull():
    queue.enqueue(input("정수 입력: "))

while not queue.isEmpty():
    print(queue.dequeue())