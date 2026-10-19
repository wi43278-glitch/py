st1 =  '                He likes apples, and she does, too likes            likes            '

# 공백 제거 
print(st1)
print(st1.strip())


#오른쪽만 공백제거

print(st1)
print(st1.rstrip())

#왼쪽 제거
print(st1.lstrip())

#문자열 바꾸기
print(st1.replace('like', 'love', 1 ))


#빈칸 제거
print(st1.replace(' ', ''))


print(st1.replace(' ', '', 1))