#함수명 = lambda 매개변수: 수행코드 



square1 = lambda x : x**2

print(square1(10))



test1 = lambda : print('test1')
test1()


a = (lambda x: x**2)(3)
print(a)
print((lambda x: x**2)(3))


# 맨뒤의 ()는 앞의 함수를 호출하는 명령어
(lambda : print('test2'))()

def fun1():
    return 1 



fun1()


list1 = [(lambda x,y,z : x + 2*y + z**2)(1,2,3)]
print(list1)
print((lambda x,y,z : x + 2*y + z**2)(1,2,3))

print([(lambda x : x**2)(a) for a in range(1,6)])
[1,4]

list2 = [(lambda x : x**2)(a) for a in range(1,6)]
print(list2)