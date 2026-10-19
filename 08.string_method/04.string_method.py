st1 =  'He likes apples, and she does, too likes'

# 특정문자 기준으로 문자열을 분리 
# 기본값 : 공백문자 
# 결과값 : 리스트 
print(st1)
print(st1.split())

# ',' 기준으로 분리
print(st1)
print(st1.split(','))

#공백을 기준으로 3번만분리

print(st1.split(' ', 3))
print('-'* 100)
print(st1)
 

print(st1.split(', '.join(st1)))