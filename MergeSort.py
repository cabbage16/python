import random

num = []


while len(num) != 100:
    n = random.randrange(101)
    if n in num:
        n = random.randrange(101)
    else:
        num.append(n)

print("before: " + str(num) + "\n")

for i in range(len(num) - 1):
    for j in range(i + 1, len(num)):
        if num[i] > num[j]:
            num[i], num[j] = num[j], num[i]

print("after: " + str(num))