
# 문 : 1~100 까지의 사용자가 넣은 숫자의 배수의 합계를 구하고,
# 갯수가 몇개인지 출력
# 사용자가 넣은값: 7
# ex) 7, 14, 21, 28, 35 .... (합계)


start = int(input('합계를 구할 시작 값입력 : '))
end =  int(input('합계를 구할 끝나는 값 입력하시오 : '))
num = int(input('배수입력 : '))
total = 0
count = 0

for i in range(start, end+1):
    if i % num == 0:
        total += i
        count += 1
        print(i, end=' ')

print()
print(f'{num}의 배수의 합계 : {total}, 갯수는 {count}')

