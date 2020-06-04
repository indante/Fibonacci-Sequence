# -*- coding: utf-8 -*- 

start_value = int(input('몇부터: '))
last_value = int(input('몇까지: '))

fibonacci_list = [];
fibonacci_list.extend((start_value, start_value))
fibonacci_list.append(sum(fibonacci_list))

for n in range(last_value):
    s = fibonacci_list[n+1] + fibonacci_list[n+2]
    fibonacci_list.append(s)

sum_fibonacci_list = sum(fibonacci_list)
print(fibonacci_list)
print('다 더해서 {} 입니다.'.format(sum_fibonacci_list))
