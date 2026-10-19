'''
한 과일 가게의 현재 과일 재고 수량이 다음과같이 딕셔너리에 저장되어 있다.
inventory = {
    'apple': 15,
    'banana: 8,
    'orange':20,
    'melon' : 3

}
#문1. 가게에 포도('grape')가12개 새로들어왔다. 추가하기
#문2. 손님이 망고 ('mango)가 있는지 물어보았다. 망고가 잇으면
    # 재고 출력 없으면 '재고가 없습니다' 출력 get()메서드 사용
#문3. 오늘 마검 전, 현재 가게에 남아있는 모든 과일의 이름과 재고 수량을
# 아래 보기와 같은 형식으로 한 줄 씩 출력하는 코드를 작성 ( 단, items() 메서드
# [출력 보기]
# 과일 : apple | 재고: 15개
# 과일 : banana | 재고: 8개

'''

inventory = {
    'apple': 15,
    'banana': 8,
    'orange': 20,
    'melon': 3,
}

# 문1. 포도 12개 추가
inventory['grape'] = 12
inventory['apple'] += 12
in_fr = 'apple'
if 'in_fr' in inventory:
    inventory['in_fr'] += 12
else : 
    inventory['in_fr'] = 12
print(inventory)
print('-'* 30)
# 문2. 망고 재고 확인 (get() 사용)
stock = inventory.get('mango')
if stock:
    print(f'망고 재고: {stock}개')
else:
    print('재고가 없습니다')
print('-' * 30 )
# 문3. 모든 과일의 이름과 재고 출력 (items() 사용)
for name, count in inventory.items():
    print(f'과일 : {name} | 재고: {count}개') 