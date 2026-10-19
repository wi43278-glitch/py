# 변수 : 어떤 자료형이든 상관없이 넣을 수 있다.
var1 = 'Hello Python'
print(var1)
print(id(var1)) # 주소를 출력하는 함수 

var1 = 100 
print(var1)
print(id(var1))
print( '-' * 30 )
# 변수명은 예약어를 쓸 수 없다.
# 변수가 무엇을 가르키는지 알 수 있는 이름으로 작명

# 파이썬의 자료의 크리는 상관없다
num1 = 100
num2 = 214214124214421421421421
num3 = 32.4212142142142142
print('num1 type =', type(num1))
print(f'num2 type =', {type(num2)})
print(f'num3 type = {type(num3)}')
print('-' * 30)


a = '박수영 이무기'
b = 'Hello world!!!'
c = True
print(a)
print(b)
print(c)
print('c type =', type(a))
print(f'b type =', {type(b)})
print(f'a type = {type(c)}')
print('-' * 30)

d = 7
e = 9
f = 5

# int d= 1 e=5, f=6
g, h, i = 1, 2, 3
print(g, h, i)

j, k, m = '문자' , False, 3.14
print(j, k, m)