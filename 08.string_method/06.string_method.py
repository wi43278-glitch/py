st1 = '12345'
st2 = 'PythonAi'
st3 = 'Python Ai'
st4 = '이정은'
st5 = '1234abcd'

# 숫자만을 구성되어 있는지 검사
print('숫자로만 구성되어 있는가?', st1.isdigit(),st2.isdigit(),st3.isdigit(),st4.isdigit(),st5.isdigit()) 
print('-' * 50)

# 문자로만 구성되어 있는지 검사 공백
print('문자로만 구성되어 있는지?', st1.isalpha(),st2.isalpha(),st3.isalpha(),st4.isalpha(),st5.isalpha())
print('-' * 50)

#숫자나 문자로 구성되어 있는지?
print('숫나자나 문자로만 구성되어 있는지?', st1.isalnum(), st2.isalnum(), st3.isalnum(), st4.isalnum(), st5.isalnum())
print('-' * 50)

# 문자열이 소문자인지 검사?
print('문자열이 소문자인가', st1.islower(), st2.islower(), st3.islower(), st4.islower(), st5.islower())
print('-' * 50)

# 문자열이 공백문자인지 검사
st6 = '           '
print('문자열이 공백문자인인가?', st6.isspace())
print('-' * 50)

# 단어의 첫글자가 대문자인지 ?
print(' 첫글자가 대문자인가?', st1.istitle(),st2.istitle(),st3.istitle(),st4.istitle(),st5.istitle())
print('-' * 50)

# 빈자리를 0으로 채우고싶다
st1 = 'Hello python!!!!'
st2= st1.zfill(20)
print(st1,st2)

