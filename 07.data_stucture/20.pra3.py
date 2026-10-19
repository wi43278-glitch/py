'''

문
로또 프로그램 만들기
사용자로부터 몇회분을 살건지 물어보고 
그 횟수 만큼 번호를 랜덤으로 추출하여 출력하기


'''


import random

try:
    count = int(input('몇 회분을 구매하시겠습니까? : '))
    if count <= 0:
        print('1회 이상 입력해 주세요.')
    else:
        for i in range(1, count + 1):
            numbers = sorted(random.sample(range(1, 46), 6))
            print(f'{i}회 : {numbers}')
except ValueError:
    print('숫자로 입력해 주세요.')