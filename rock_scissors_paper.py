import random

victory = 0
defeat = 0
draw = 0

while True:
    player = (input("가위,바위,보 중 하나를 입력하세요.(종료하려면 break를 입력하세요.)"))
    computer  = random.choice(('가위', '바위', '보'))

    if player == '가위' or player == '바위' or player == '보':
        if player == computer:
            print("컴퓨터:",computer)
            print("비겼습니다")
            draw += 1

        elif player == '가위' and computer == '보' or player == '바위' and computer == '가위' or player == '보' and computer == '바위':
            print("컴퓨터:",computer)
            print("이겼습니다")
            victory += 1

        else:
            print("컴퓨터:",computer)
            print("졌습니다")
            defeat += 1

    elif player == 'break':
        print(f"게임 종료\n이긴횟수: {victory}\t진 횟수: {defeat}\t비긴횟수: {draw}")
        break

    else:
        print("잘못된 입력을 하셨습니다. 가위, 바위, 보 중에 하나를 입력해야하고 제대로 입력했는지 확인해 주십시오.")