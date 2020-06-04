# 피보나치 수열
> 정보처리기능사 실기 공부하다가 문득 코드로 만들어보고 싶어서 만들어진 결과물

## 후기
파이썬을 이용한 피보나치 수열 코드를 구글링해보면 엄청 다양하다. 그렇지만 나처럼 허접한 사람이 보기에는 코드를 이해하기가 힘들었다. <br>
그래서 혼자 만들어본거고 시간은 생각보다 별로 걸리지 않았다. 그만큼 완성도가 낮고 코드도 이상하다. 화이팅..?!

```py
# -*- coding: utf-8 -*- 

start_value = int(input('몇부터: ')) # 변수 그대로의 뜻
last_value = int(input('몇까지: ')) # 변수 그대로의 뜻

fibonacci_list = []; # 합을 구하기 위해 리스트 생성
fibonacci_list.extend((start_value, start_value)) # 변수에 시작되는(연속되는) 값(2개) 추가
fibonacci_list.append(sum(fibonacci_list)) # 연속되는 값 더해서 추가

for n in range(last_value): # 반복문
    s = fibonacci_list[n+1] + fibonacci_list[n+2] # 연속되는 2개 항을 합해서 변수에 추가
    fibonacci_list.append(s) # 위에서 구한 연속되는 2개 항의 합을 변수에 추가

sum_fibonacci_list = sum(fibonacci_list) # 변수 `fibonacci_list` 의 총합 새로운 변수에 추가
print(fibonacci_list) # 피보나치 수열 리스트 출력
print('다 더해서 {} 입니다.'.format(sum_fibonacci_list)) # 총합 출력
```