'''
문1: 2개의 수를 넣으면 그사이의 숫자들의합계 구하기
    3, 10을매개변수로 넣으면 3~까지의 합계를 구하기
문2 : 숫자만큼 별찍기
'''


def plus(a, b):
    total = 0
    for i in range(a, b + 1):   
        total += i
    return total

print(plus(3, 10))    

# def star(n):
#     for x in range(n):
#         for y in range(x+1):
#             print('*'+ x+ 1)

# star(5)
# star(5)
# star(5)
# star(5)


def start2(n):
    for i in range(n):
        print('*' *  (i+1))
start2(10)

# (i=0) : 공백 4개, 별1개
# (i=1) : 공백 3개, 별3개
# (i=2) : 공백 2개, 별5개
# (i=3) : 공백 1개, 별7개
# (i=4) : 공백 0개, 별9개

def star_pyramid(rows):
    for i in range(rows):
        space = ' ' * (rows - 1 - i)
        stars = '*' * (2 * i + 1)
        print(space + stars)

star_pyramid(10)