# 판매가 (float)
sell_coffee = 1800.0
sell_triangle = 1400.0
sell_banana = 1800.0
sell_lunch = 4000.0   # 3500 400원 → 4000원으로 가정
sell_cola = 1500.0
sell_shrimp = 2000.0

# 구입가 (float)
buy_coffee = 500.0
buy_triangle = 900.0
buy_banana = 800.0
buy_lunch = 3500.0
buy_cola = 700.0
buy_shrimp = 1000.0

# 잔액 (float)
balance = float(input('현재 잔액을 입력하세요 : '))

# 구입 개수 (int)
n_buy_triangle = int(input('삼각김밥 구입 개수 : '))
n_buy_lunch = int(input('도시락 구입 개수 : '))

# 판매 개수 (int)
n_coffee = int(input('캔커피 판매 개수 : '))
n_triangle = int(input('삼각김밥 판매 개수 : '))
n_banana = int(input('바나나우유 판매 개수 : '))
n_lunch = int(input('도시락 판매 개수 : '))
n_cola = int(input('콜라 판매 개수 : '))
n_shrimp = int(input('새우깡 판매 개수 : '))

# 구입 비용
cost = buy_triangle * n_buy_triangle + buy_lunch * n_buy_lunch

# 총매출
total = (sell_coffee * n_coffee
         + sell_triangle * n_triangle
         + sell_banana * n_banana
         + sell_lunch * n_lunch
         + sell_cola * n_cola
         + sell_shrimp * n_shrimp)

# 최종 잔액 = 기존 잔액 - 구입 비용 + 총매출
final = balance - cost + total

print(f'구입 비용: {cost:.0f}원')
print(f'총매출: {total:.0f}원')
print(f'최종 잔액: {final:.0f}원')