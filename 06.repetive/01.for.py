str = 'absadadw'

for x in str:
    print(x)
print ('-' *30)

num = [0,6,4,21]

for i in num:
    print(i)
print ('-' *30 )

'''

range (시작값, 종료값, step) 
range (종료값) -. default 시작값 = 0, step=1
range (시작값,종료값) -> step=1   
'''

for x in range(5):
    print(x)

for x in range(3, 10):
    print(x)

for x in range(1, 10 ,3):
    print(x)

for x in range(1, 20, 2):
    print(x, end=', ') 
print('-' *30 )
for x in range(1, 20,2):
    if x < 19:
        print(x, end= ', ')
    else:
        print(x)