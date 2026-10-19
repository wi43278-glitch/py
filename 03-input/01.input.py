# 사용자로부터 입력받기 
#name = input('이름을 입력하세요 : ')
#print(name + '님 환영합니다.')


# input() 함수의 결과는 문자열로 들어옴
#kor = int(input('국어점수를 입력하세요 :'))
#com = int(input('컴퓨터 점수를 입력하세요 :'))
#print(kor + com)

# int형 변환의 우선 순위
# int형 변환의 우선 순위
#kor = int(input('국어점수를 입력하세요 :'))
#com = int(input('컴퓨터 점수를 입력하세요 :'))
#print(kor + com)                          # int + int
#print(int(str(kor) + str(com)))           # 문자열로 이어붙인 후 int 변환
#print('%d + %d = %d' % (kor, com, kor + com))
#print('%s + %s = %s' % (kor, com, kor + com))
#print(f'{kor} + {com} = {kor + com}')





stadium = input('경기장은 어디입니까? : ')
win = input('이긴팀은 어디입니까? : ')
lose = input('진팀은 어디입니까? : ')
score = input('스코어는 몇대몇 입니까? : ')


print("=" * 40)
print(f'오늘 {stadium}에서 야구경기가 열렸습니다')
print(f'{win}와(과) {lose}의 치열한 공방전이 펼쳐졌습니다')
print(f'결국 {win}은(는) {lose}를 "{score}"으로 이겼습니다')


result = '''오늘 %s에서 야구경기기가 열렸습니다
%s과 %s의 치열한 공방전이 펄쳐졌습니다
결국 %s은 %s으로 이겼습니다''' %(stadium,win,lose,win,lose)
print(result)

