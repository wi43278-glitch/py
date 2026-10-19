# 사칙연산 return 없이 



def plus(x,y):
    print(f'{x}+{y}= {x+y}')

def minus(x,y):
    print(f'{x}-{y}= {x-y}')

def multi(x,y):
    print(f'{x}*{y}= {x*y}')

plus(1,4)
minus(7,4)
multi(10,5)

def plusRe(x,y):
    return x+y

def minusRe(x,y):
    return x-y

def multiRe(x,y):
    return x*y

result = plus(3,8)
print(result)
print(minusRe(result,7))
print(multiRe(4.56,2.77))
