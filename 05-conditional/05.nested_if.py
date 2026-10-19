
#20세 이상 -> 성년
#15세 ~ 19 > 청소년
#15세 미만  어린이

age = int(input('나이를 입력하세요'))
if age > 20:
    print("성년")
elif age > 15 :
    print('청소년')
else:
    print('어린이')


if age <= 19:
    if age >=15: 
        print('청소년')
    else:
        print('어린이')
else:
    print('성년')

  
 