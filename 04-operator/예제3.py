py = 4.5
os = 2.0
AI = 4.0

py_credit = 3.0
os_credit = 2.5
AI_credit = 3.0

total_credit = py_credit + os_credit + AI_credit
average = (py * py_credit + os * os_credit + AI * AI_credit) / total_credit
print(f'총 이수 학점 : {total_credit}학점')
print(f'평균학점: {average:.2f}')   