

# 문 : 주사위를 3개를동신에 던져서 동일한 숫자가 나오면 탈출하는 게임
# 출력. 주사위에 나온 숫자와 횟수 출력 
'''
import random
count = 0
while True:
    x = random.randint(1,6)
    y = random.randint(1,6)
    z = random.randint(1,6)
    count += 1

    print(f'{count} : {x}, {y}, {z}')

    if x == y == z:
        print(f'\n세 주사위를 모두 {x}! 탈출성공')
        print(f'총 {count}를 던졌습니다.')
        break
'''
# 문 : 주사위의 숫자 맞추기
import random
count = 0
while True:
    count += 1
    print('게임',count, '회')
    x = random.randint(1,6)
    user = int(input('주사위의 숫자는 어떤 숫자 일까요? '))
    if x == user:
        print('정답입니다.' , count, '회에 맞추셧습니다.')
        break
    else:
        print('틀렸습니다.' 'x' '입니다. 다시합시다 \n')
        continue    


