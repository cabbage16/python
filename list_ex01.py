a_list = [1, 2, 3, 4, 5]
print(a_list[:2]) # 리스트 슬라이싱. 콜론으로 구분. 콜론 앞에 값이 없으면 처음부터
print(a_list[2:]) # 콜론 뒤에 값이 없으면 끝까지

b_list = []
b_list.append(1) # 리스트의 맨 마지막에 값을 추가하는 내장함수
b_list.append(2)
b_list.append(3)
print(b_list)

c_list = [1, 3.14, "hello", [1, 2, 3]] # 배열과 다르게 타입이 달라도 가능
print(c_list)
print(c_list[1:3]) # 리스트 슬라이싱. [m:n]이면 m번 인덱스부터 n-1번 인덱스까지

d_list = [1, 2, 3, 4, 5]
print(d_list)
d_list[0] = 5 # 배열처럼 인덱스를 이용해서 값을 바꾸기 가능
print(d_list)