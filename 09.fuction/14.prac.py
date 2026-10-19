

prices = [10000, 20000, 30000, 40000]

# 20% 할인된 가격 (원래 가격의 80%)
discount = lambda p: p * 0.8
print(list(map(discount, prices)))



