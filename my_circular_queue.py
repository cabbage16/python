class CircularQueue:
    def __init__(self, capacity = 10) -> None:
        self.capacity = capacity
        self.list = [None] * capacity
        self.front = 0
        self.rear = 0

    def is_empty(self) -> bool:
        return self.front == self.rear

    def is_full(self) -> bool:
        return (self.rear+1) % self.capacity == self.front

    def enqueue(self, item) -> None:
        if self.is_full():
            print("Error: Queue is full")
            return
        
        self.rear = (self.rear+1) % self.capacity
        self.list[self.rear] = item

    def dequeue(self) -> int:
        if self.is_empty():
            print("Error: Queue is empty")
            return
        
        self.front = (self.front+1) % self.capacity
        return self.list[self.front]


    def peek(self) -> int:
        if self.is_empty():
            print("Error: Queue is empty")
            return
        
        return self.list[(self.front+1) % self.capacity]
    
    def clear(self):
        while not self.is_empty():
            self.dequeue()

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
    
queue = CircularQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue)
print(queue.dequeue())
print(queue)