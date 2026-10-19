# 중첩 for문
for i in range(3):
    for j in range(2):
        print(f'i={i}, j={j}')
print ('-' * 30)

for dan in range(2, 10):
    print('  ', dan,'단')
    for i in range(1,10):
        print(f'{dan} * {i} = {dan*i}')
    print()

# 구구단인데 가로로 출력

for i in range(1, 10):
    for dan in range(2, 10):
        print('%d*%d=%2d' %(dan, i, dan * i), end='   ')
        print(f'{dan}*{i}={dan*i:2d}' , end='   ')
    print()
