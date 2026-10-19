'''
문1) 카페 주문
메뉴와 사이즈 2개를 입력받음.
만약 사이즈가 입력이 안되서 무조건 small 사이즈임


 문2) 택배 배송정보
 받는사람, 주소, 전화번호를 입력받음.
 순서와 상관없이 받아서 출력



문3) 친구들과 식당에 가서 각자 내 금액의 합계 구하기(tuple)
친구들이 갈 때마다 인원이 달라짐




문)4 회원가입 정보를 입력받기(dict)
사람마다 입력하는 정보의 개수가 다를 수 있음

'''

# 문1) 기본값 매개변수: size를 입력하지 않으면 small
def order_cafe(menu, size="small"):
    print(f"주문: {menu} ({size})")

order_cafe("아메리카노")           # 아메리카노 (small)
order_cafe("라떼", "large")        # 라떼 (large)


# 문2) 키워드 인자: 순서와 상관없이 받기
def delivery(name, address, phone):
    print(f"받는사람: {name}")
    print(f"주소: {address}")
    print(f"전화번호: {phone}")

delivery(phone="010-1234-5678", name="홍길동", address="서울시 강남구")


# 문3) 가변 인자 *args (tuple): 인원수가 달라져도 합계 계산
def total(*args):
    print(type(args))          # <class 'tuple'>
    result = 0
    for x in args:
        result += x
    return result

print(total(8000, 12000))               # 2명
print(total(8000, 12000, 9500, 15000))  # 4명


# 문4) 가변 키워드 인자 **kwargs (dict): 입력 정보 개수가 달라도 OK
def join(**kwargs):
    print(type(kwargs))        # <class 'dict'>
    for key, value in kwargs.items():
        print(f"{key}: {value}")

join(name="홍길동", age=25)
join(name="김영희", age=30, email="a@b.com", phone="010-0000-0000")
 