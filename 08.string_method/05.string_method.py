st1 =  'He likes apples, and she does, too likes'

# 가운데 맞춤
print(st1)
print(st1.center(50))
print(st1.center(50) + '*')

# 공백 대신 '-' 

print(st1.center(50,'-'))

# 오른쪽 맞춤
print(st1.rjust(50))

#왼쪽 맞춤
print(st1.ljust(50))
print(st1.ljust(50) + '===')


# expandtabs() : 공백 8개 들어가는 함수

st2 = '1\tand\t2'
print(len(st2))
print(st2.expandtabs(20))
print(len(st2))




