import random, time

WORD_LIST = [
    "안녕하세요",
    "Hello, World!",
    "밤돌 밤돌~ 이로 이로~",
    "집 가고 싶다",
    "이 문장은 14글자 입니다",
    "김예진 바보",
    "이지우 바보"
]

random.shuffle(WORD_LIST)

for i in WORD_LIST:
    start_time = time.time()
    user_input = input(i+'\n').strip()

    if len(user_input) > len(i):
        user_input = user_input[:len(i)]
    if user_input == 'exit':
        break

    time_taken = time.time() - start_time
    correct_chr = 0

    for index, c in enumerate(user_input):
        if c == i[index]:
            correct_chr += 1

    accuracy = correct_chr / len(i)
    print(f"타속: {int((correct_chr / time_taken) * 60)}타 정확도: {accuracy: .2%} 오타율: {1 - accuracy:.2%}")

print("bye")