st1 = 'He likes apples, and she does, too' 

# 모두다 대문자로 고치시오 
st2 = st1.upper()
print(st1)
print(st2)
print('-'* 30 )

# 다 소문자로
st2 = st1.lower()
print(st1)
print(st2)
print('-'* 30 )

# 대문자는 소문자로 소문자는 대문자로
st2= st1.swapcase()
print(st1)
print(st2)

# 문장의 첫글자를 대문자로 변환
st3 = st2.capitalize()
print(st2)
print(st3)
print('-' * 30)
# 단어의 첫글자를 대문자로
st2= st1.title()
print(st1)
print(st2)