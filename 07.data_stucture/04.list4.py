str_list = ['국어','영어','수학','국사','컴퓨터']
print(str_list.index('영어'))
#print(str_list.index('파이썬'))


a = "수학"

if a in str_list:
    print(str_list.index(a))
else:
    print('데이터 없음')


str_list.append('파이썬')
print(str_list)

str_list.insert(2, '인공지능')
print(str_list)
print('--' *30 )
# 데이터 정렬
# sorted : 데이터 정렬
print(sorted(str_list)) # 오름차순
print(sorted(str_list, reverse = True))
print(str_list)
print( '-' * 50)

# sort : 데이터 원본이 바뀜
str_list.sort()
print(str_list)
print( '-' * 50)

# 데이터 삭제 없는데이터를 넣으면 error
if '세계사' in str_list :
    str_list.remove('세계사')
print(str_list)

#모든 데이터 삭제
str_list.clear()
print(str_list)