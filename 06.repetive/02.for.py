# 1~ 100 합계 구하기

sum = 0 
for i in range(1,101):
    sum += i
print(sum)


# 1~100 까지 5의 배수의 합을 구하시오
sum = 0
for y in range(1,101):
    if(y % 5 == 0):
        sum += y

print('1~100까지 5의 배수의 합 :', sum)

sum = 0
for n in range(0,101,5):
    sum += n
    print('1~100까지 5의 배수의 합:' , sum)


