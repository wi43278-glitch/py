'''
사용자로 부터 정수 4개를입력받아
리스트에 저장하고 합계 출력
'''

numlist = [0,0,0,0]
#numList2 = [0 for a in range(101)]
#print(numList2)

#sum = 0
#numlist[0] = int(input('숫자 : '))
#numlist[1] = int(input('숫자 : '))
#numlist[2] = int(input('숫자 : '))
#numlist[3] = int(input('숫자 : '))
#sum = numlist[0] + numlist[1] + numlist[2] + numlist[3]
#print('합계 : ', sum)

numList = [0,0,0,0]
for x in range(4):
    numList[x] = int(input('숫자 : '))
print('합계: ', sum(numList))    


# numList = []
# sum = 0
# for x in range(4):
#     num = int(input('숫자 : '))
#     numList.append(num)
#     sum += numList[x]
# print('합계: ', sum)
# print(numList)
