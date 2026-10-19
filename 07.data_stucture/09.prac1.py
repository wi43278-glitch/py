subjects = ['파이썬', 'AI', '빅데이터', '디자인']
names = ['홍길동', '아무개', '이순신']
score = [
    [79, 75, 90, 86],
    [100, 65, 97, 76],
    [99, 78, 70, 88],
]

# 헤더
print('과정'.ljust(8), end='')
for s in subjects:
    print(s.rjust(8), end='')
print('합계'.rjust(8) + '평균'.rjust(8))
print('-' * 56)

# 학생별 점수, 합계, 평균
for i in range(3):
    total = sum(score[i])
    avg = total / len(score[i])
    print(names[i].ljust(8), end='')
    for point in score[i]:
        print(str(point).rjust(8), end='   ')
    print(str(total).rjust(8) + f'{avg:8.2f}')

print('-' * 56)

# 과목별 합계, 평균
col_sum = [sum(score[i][j] for i in range(3)) for j in range(4)]
col_avg = [c / 3 for c in col_sum]

print('합계'.ljust(8), end='')
for c in col_sum:
    print(str(c).rjust(8), end='')
print()
print('평균'.ljust(8), end='')
for c in col_avg:
    print(f'{c:8.2f}', end='')
print()

# students = [
#     ['홍길동',      67, 87, 59, 100],
#     ['아무개',      98, 78, 84, 67],
#     ['이순신',      47, 80, 68, 98],
# ]

# sub_sum = [0, 0, 0, 0]

# print('과정\t파이썬\tAI\t빅데이터\t디자인\t합계')
# print('-' * 60)

# for row in students:
#     name = row[0]
#     scores = row[1:]
#     for i in range(4):
#         sub_sum[i] += scores[i]

#     s_sum = sum(scores)
#     s_avg = s_sum / len(scores)
#     print(f'{name}\t{scores[0]}\t{scores[1]}\t{scores[2]}\t{scores[3]}\t{s_sum}\t{s_avg:.2f}')

# print('-' * 60)

# sub_avg = [total / len(students) for total in sub_sum]
# #print(f'합계\t{sub_sum[0]}\t{sub_sum[1]}\t{sub_sum[2]}\t{sub_sum[3]}')
# #print(f'평균\t{sub_avg[0]:.2f}\t{sub_avg[1]:.2f}\t{sub_avg[2]:.2f}\t{sub_avg[3]:.2f}')
# print(f'평균\t', end='')
# for avg in sub_avg:
#     print(f'{avg:.1f}', end= '\t')


