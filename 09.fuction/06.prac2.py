'''
문 1 : 매개변수로 2개의 숫자와 연산자를 입력받아 출력

문 2 : 국어, 영어 점수를 사용자로 부터 입력받아
        함수로 평균을 입력받아 평균의 학점을 return 하기

문 3: 로또를 함수로

문 4 :
입력한 비밀번호가 비밀번호 규칙에 맞으면 생성되고,
규칙에 맞지 않으면 다시 생성하도록 메시지를 출력하는 프로그램을 작성
1. 8글자 이상이어야 함
2. 문자 및 숫자로만 생성해야 하며 기호는 불가능

새로운 비밀번호를 입력하세요 : abcd
오류. 비밀번호가 규칙에 맞지 않습니다

새로운 비밀번호를 입력하세요 : abcd1234$$$
오류. 비밀번호가 규칙에 맞지 않습니다

새로운 비밀번호를 입력하세요 : 1234abcd
비밀번호가 생성 되었습니다
'''

def cc(num1, num2, op):
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 == 0:
            result = '0으로 나눌 수 없습니다'
        else:
            result = num1 / num2
    else:
        result = '지원하지 않는 연산자입니다'
    return result

val1 = int(input('숫자입력:'))
val2 = int(input('숫자입력:'))
oper = input('연산입력:')
print(cc(val1, val2, oper))

print(cc(1, 2, '+'))

# 문제 2번
def get_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'

def jumsu(n):
    result = []
    for i in range(n):
        kor = int(input(f'{i+1}번 국어 점수 입력: '))
        eng = int(input(f'{i+1}번 영어 점수 입력: '))
        avg = (kor + eng) / 2
        result.append((avg, get_grade(avg)))
    return result

print(jumsu(2))

#문제 3번 

import random

def randum(count):
    for i in range(1, count + 1):
        numbers = sorted(random.sample(range(1, 46), 6))
        print(f'{i}회 : {numbers}')

try:
    count = int(input('몇 회분을 구매하시겠습니까? : '))
    if count <= 0:
        print('1회 이상 입력해 주세요.')
    else:
        randum(count)
except ValueError:
    print('숫자로 입력해 주세요.')

# 문제 4번 


def check_pw(pw):
    return len(pw) >= 8 and pw.isalnum()

while True:
    pw = input('새로운 비밀번호를 입력하세요 : ')
    if check_pw(pw):
        print('비밀번호가 생성 되었습니다')
        break
    else:
        print('오류. 비밀번호가 규칙에 맞지 않습니다')
        print()    


