# 연산자
# - 산술, 비교, 논리 연산자

# 산술 연산자
# 형식: +, -, *, /, // (몫), % (나머지), ** (거듭제곱)

# 우선순위
# - 곱셈, 나눗셈 등이 우선, 괄호를 이용하여 변경 가능

# 복합 할당
# 형식: score += 10 <-> score = score + 10
score = 100
score += 10
print(score)
# -=, *=, /=

# 문자열 연산
# +, * 가능
print('안녕' + '하세요')    # 안녕하세요
print('-' * 4)  # ---- -> 반복
# 주의) 자료형이 같은 것끼리 연산 할 수 있다

print('실습1')
a = 10
b = 3
print(a + b)        #13
print(a - b)        #7
print(a * b)        #30
print(a / b)        #3.33...
print(a // b)       #3 (몫)
print(a % b)        #1 (나머지)
print(a ** b)       #1000 (거듭제곱)

print('실습2')
# 점수 3개 저장
score1 = 80
score2 = 90
score3 = 100

# 평균 계산
averege = (score1 + score2 + score3) / 3
print(averege)     # 평균: 90

# 정사각형 넓이 계산
side = 5
area = side ** 2
print(area)     # 정사각형 넓이: 25

# 직육면체 부피 계산
width = 3
length = 4
height = 5
volume = width * length * height
print(volume)       # 직육면체 부피: 60

# 비교 연산자
# 형식: == (같다)  != (다르다)  < > <= >=
print(5 == 5)   # True
print('정상' == '정상') # True
print('A' == 'a')   # False

# 논리 연산자
# - and: 모두 참이어야 함, or: 하나만 참이어도 참, not: 반대
print(True and False)   # False
print(True or False)    # True
print(not True)         # False

print('실습 3')
a = 5
b = 3

print(a == b)       # 같다: False
print(a != b)       # 다르다: True
print(a > b)        # 크다: True
print(a < b)        # 작다: False
print(a >= b)       # 이상: True
print(a <= b)       # 이하: False

print('실습 4')
# 온도 범위 확인
temp = 85
temp_ok = temp >= 60 and temp <= 90
print(temp_ok)      # 온도 정상 여부: True

# 압력 범위 확인
press = 5
press_ok = press >= 3 and press <= 7
print(press_ok)     # 압력 정상 여부: True

print('실습 5')
# 초기 재고 수량
stock = 100
print(stock)        # 초기재고: 100

# 입고 50개
stock += 50
print(stock)        # 입고 후 재고: 150

# 출고 30개
stock -= 30
print(stock)        # 출고 후 재고: 120

# 반품 5개
stock += 5
print(stock)        # 반품 후 재고: 125

print('실습 6')
# 불량률 계산
total = 500
error = 23
error_rate = error / total * 100
print(error_rate, '%')      # 불량률: 4.6%

# 가동률 계산
run_time = 21
total_time = 24
running_rate = run_time / total_time * 100
print(running_rate, '%')        # 가동률: 87.5%

print('실습 7')
total_minutes = 500
hours = total_minutes // 60
minutes = total_minutes % 60
print(hours,'시간', minutes,'분')       # 가동 시간: 8시간 20분