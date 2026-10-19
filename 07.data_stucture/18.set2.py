s = {1,2,3,1,2,3,4,1,3,5}

print(2 in s)
print(6 in s)

# 데이터 추가 

s.add(10)
print(s)

# 업데이트 가능

s.update({5,11,25125,121,521})
print(s)

# 개별 삭제 가능
s.remove(2)
print(s)

s.clear()
print(s)