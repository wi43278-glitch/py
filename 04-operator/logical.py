num1 =100
num2 =200
x = 7
y = 3
f_result = num1 >= num2 # False
t_reuslt = x >= y  # T
print(f'f_result = {f_result}, t_result = {t_reuslt}')


and_result = f_result and t_reuslt
or_result = f_result or t_reuslt
print(f'f_result and t_result = {and_result}')
print(f'f_result or t_result = {or_result}')

print(f'f_result not = {not f_result}')


xor = f_result ^ t_reuslt
xor2 = f_result ^ f_result
print(xor)
print(xor2)
