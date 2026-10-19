# 문 무한반복으로 구구단 중 출력할 단수를 입력받아 출력
# 출력 후 구구단을 계속할 것인지 확인 'y' 'n' 


while True:
    num1 = int(input('숫자입력 '))
    for x in range(1,10):
        print(f'{num1} * {x} = {num1*x}\n')
    if num1 =='y' or num1 == 'Y':
        continue
    else:
        print('계산 종료')
        break