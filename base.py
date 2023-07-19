import sys

print("---진수 변환기---")
print("프로그램을 종료하려면 exit를 입력해주세요.")

while True:
    put = int(input('입력할 진법(2,8,10,16진법만가능):'))

    if not(put >= 2 and put <= 16 or put != 0):
        print("잘못된 입력,또는 출력입니다.")
        continue

    out = int(input('출력할진법(2,8,10,16진법만가능):'))

    if not(out >=2 and out <= 16 or out != 0):
        print("잘못된 입력,또는 출력입니다.")
        continue

    n = int(input('수 입력:'), put)

    sys.stdout.write("출력 결과: ")
    if(out == 2):
        print(format(n, 'b'))

    elif(out == 8):
        print(format(n, 'o'))

    elif(out == 16):
        print(format(n, 'x'))

    else:
        print(format(n, 'd'))