# 대입연산자
num1 = 10
num1 += 10 # num1 = num1 + 10 과동일
print(num1)


num1 -= 10 
num1 *= 10 # 100
num1 /= 2 # 50
num1 %= 9 # 5
num1 //= 3
print(num1) 

num1 = 10
num1 **= 3
print(num1) 


pound = int(input('파운드를 입력하세요 : '))
kg = int(input('킬로그램을 입력하세요: '))
print(f'{kg} = {pound} * 0.453592')
print(f'{pound} = {kg} * 2.204623')