# 문1 : 정수를 입력받아서 짝수인지 홀수인지 판별
num = int(input('정수를 입력하시오 : '))

if num % 2 == 0:
    print(f'{num}은(는) 짝수입니다.')
else:
    print(f'{num}은(는) 홀수입니다.')


# 문2 : 2개의 정수를 입력받아 큰값과 작은값을 판별하여 출력
# EX) 큰값 : 7 작은값 : 3
a = int(input('첫 번째 정수를 입력하시오 : '))
b = int(input('두 번째 정수를 입력하시오 : '))

if a > b:
    print(f'큰값 : {a} 작은값 : {b}')
elif a < b:
    print(f'큰값 : {b} 작은값 : {a}')
else:
    print(f'두 수가 같습니다. (값 : {a})')


