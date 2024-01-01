class LinearDeque:
    def __init__(self, capacity = 10): 
        self.capacity = capacity # 크기 초기화
        self.list = [None] * capacity # 리스트 초기화
        self.front = -1
        self.rear = -1 # front, rear 0 초기화

    def is_empty(self): # 비어있으면 true 아니면 false 반환
        return self.front == self.rear

    def is_full(self): # 가득차있으면 true 아니면 flase 반환
        return (self.rear - self.front == self.capacity)

    def add_front(self, item):
        if not self.is_full():
            self.list[self.front] = item # front에 데이터 저장
            self.front = (self.front-1) # front 값 감소
        else:
            print("덱이 가득 찼습니다.")

    def delete_front(self): 
        if not self.is_empty(): # 비어있지 않을 때
            self.front = (self.front+1) # front 크기 줄임
            result = self.list[self.front] # front의 값을 저장
            self.list[self.front] = None # 그 위치 값을 없앰
            
            return result # 저장 값 반환
        else:
            print("덱이 비어 있습니다.")

    def get_front(self):
        if not self.is_empty(): # 비어있지 않을 때
            return self.list[self.front+1] # front의 값을 반환
        else:
            print("덱이 비어 있습니다.")

    def add_rear(self, e): 
        if not self.is_full(): #가득 차 있지 않을 때
            self.rear = (self.rear + 1)# rear을 증가 시킴
            self.list[self.rear] = e # e를 rear에 넣음
        else:
            print("덱이 가득 찼습니다.")

    def delete_rear(self):
        if not self.is_empty(): # 비어있지 않을 때
            result = self.list[self.rear] # rear을 저장
            self.list[self.rear] = None # rear을 none으로 바꿈
            self.rear = (self.rear - 1) # rear값 감소
            return result
        else:
            print("덱이 비어 있습니다.")

    def get_front(self):
        if not self.is_empty(): # 비어있지 않을 때
            return self.list[(self.rear+1) % self.capacity] # rear의 값을 반환
        else:
            print("덱이 비어 있습니다.")

deque = LinearDeque()
deque.add_rear(1)
deque.add_rear(2)
deque.add_rear(3)
print(deque.list)
deque.add_front(10)
print(deque.list)
print(deque.delete_rear())
print(deque.delete_front())
print(deque.list)