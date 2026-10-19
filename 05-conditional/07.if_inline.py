# 삼항 연산식
'''


if num1 == 2:
    print('2입니다')
else :
    print('2가 아닙니다')
    

'''

num1 = 2
print('2입니다') if num1 == 2 else print('2가 아닙니다')
print('2입니다' if num1 == 2 else '2가 아닙니다')

'''
# 합격과 불합격
scroe : 60
if scroe >= 60:
    result = '합격'
else :
    result = '불합격'

print(result)

# 삼항연사자로

print('합격' if scroe >= 60 else '불합격')
# 삼항연산자를 변수에 저장
result = '합격' if scroe >=60 else '불합격'
print(result)
'''

# 2수 중 큰수 찾기 
num2 = 13
num3 = 222

max_num = num2 if num3 > num3 else num3 
print(f' {num2}과 {num3}중 큰 숫자는 {max_num} 입니다')

#회문 : 왼쪽부터 읽는것과 오른쪽으로 읽었을 때 같은 문자열

str = 'abcdcba'


if str == str[::-1] :
    print(f'{str} : 회문')
else:
    print(f'{str}: 회문 아님')

print(str, ': 회문' if str == str[::-1] else ' : 회문아님')
# print(f"{str} : {' 회문' if str == str[::-1] else ': 회문아님'}")

