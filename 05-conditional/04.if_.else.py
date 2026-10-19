jumsu = 81

if jumsu >= 90 :
    print('A학점')
else : 
    if jumsu >= 80 :
        print('B학점')
    else :
        if jumsu >= 70:
            print('C학점')
        else :
            if jumsu >= 60:
                print('D학점')
            else:
                print('F학점')
                
tmp = int(input('정수를 입력하시오'))

if tmp > 100:
    print('100점을 초과할순없습니다')
elif tmp < 0:
    print('점수가 -가 될수없습니다.')
if tmp >= 90:
    print('A학점')
elif tmp >= 80:
    print('B학점')
elif tmp >= 70:
    print('C학점')
elif tmp >= 60:
    print('D학점')
else: 
    print('F학점')

