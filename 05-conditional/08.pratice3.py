

# 사용자로부터 2수 입력을 받고, 연산자도 입력받음
num1 = int(input('첫 번째 정수를 입력하시오 : '))
num2 = int(input('두 번째 정수를 입력하시오 : '))
op = input('연산자를 입력하시오 (+, -, *, /, //, %, **) : ')

# 연산 결과를 출력하기
# +, -, *, /, //, %, **

if op == '+':
    print(f'{num1} + {num2} = {num1 + num2}')
elif op == '-':
    print(f'{num1} - {num2} = {num1 - num2}')
elif op == '*':
    print(f'{num1} * {num2} = {num1 * num2}')
elif op == '/':
    if num2 == 0:
        print('0으로 나눌 수 없습니다.')
    else:
        print(f'{num1} / {num2} = {num1 / num2}')
elif op == '//':
    if num2 == 0:
        print('0으로 나눌 수 없습니다.')
    else:
        print(f'{num1} // {num2} = {num1 // num2}')
elif op == '%':
    if num2 == 0:
        print('0으로 나눌 수 없습니다.')
    else:
        print(f'{num1} % {num2} = {num1 % num2}')
elif op == '**':
    print(f'{num1} ** {num2} = {num1 ** num2}')
else:
    print('지원하지 않는 연산자입니다.')



# 숫자를 입력받아

# 숫자를 입력받아
tmp = int(input("숫자를 입력하시오 : "))

# 양수, 홀수(짝수)인지
# 음수, 홀수(짝수)인지
if tmp > 0:
    print('양수입니다.')
elif tmp < 0:
    print('음수입니다.')
else:
    print('0입니다.')

if tmp % 2 == 1:
    print('홀수입니다.')
else:
    print('짝수입니다.')

print('-' * 30)
if tmp == 0:
    print('0입니다 ')
else:
    sign = '양수' if tmp > 0 else '음수'
    parity = '짝수' if tmp % 2 == 0 else '홀수'

    print(sign, '입니다')
    print(parity, '입니다.')