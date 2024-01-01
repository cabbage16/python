class CircularDeque:
    def __init__(self, capacity = 10) -> None:
        self.capacity = capacity
        self.list = [None] * capacity
        self.front = 0
        self.rear = 0


    def is_empty(self) -> bool:
        return self.front == self.rear

    def is_full(self) -> bool:
        return (self.rear+1) % self.capacity == self.front

    def add_front(self, item):
        if self.is_full():
            print("Error: Deque is full")
            return
        
        self.list[self.front] = item
        self.front = (self.front - 1 + self.capacity) % self.capacity

    def delete_front(self):
        if self.is_empty():
            print("Error: Deque is empty")
            return
        
        self.front = (self.front + 1) % self.capacity   
        temp = self.list[self.front]
        self.list[self.front] = None
        return temp

    def get_front(self):
        if self.is_empty():
            return "Error: Deque is empty"
        
        return self.list[(self.front + 1) % self.capacity]

    def add_rear(self, item):
        if self.is_full():
            print("Error: Deque is full")
        
        self.rear = (self.rear+1) % self.capacity
        self.list[self.rear] = item

    def delete_rear(self):
        if self.is_empty():
            return "Error: Deque is empty"
        
        temp = self.list[self.rear]
        self.list[self.rear] = None
        self.rear = (self.rear-1 + self.capacity) % self.capacity
        return temp

    def get_rear(self):
        if self.is_empty():
            return "Error: Deque is empty"
        
        return self.list[self.rear]
    
    def __str__(self) -> str:
        return str(deque.list)

deque = CircularDeque()

deque.add_front(1)
print(deque.list)
print(deque.delete_front())
print(deque.list)