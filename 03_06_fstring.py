# f-string - 문자열 안에 변수 바로 끼우기
# 형식: f'~~~ {변수} ~~~'

name = '홍길동'
age = '25'
print(f'{name}님은 {age}살입니다')          # 홍길동님은 25살입니다

# 숫자도 str 변환 없이 바로 들어감
print(f'온도: {25.5}')
# 중괄호 안에 계산식 가능                   # 온도 25.5
hours = 3           
print(f'{hours * 60}분')                    # 180분

# 소수점 자리수 조정
# 형식: {값(변수):.2f} -> 소수점 2째 자리까지 출력 (자동 반올림)
value = 25.34567
print(f'측정값: {value:.2f}')               # 측정값: 25.35
print(f'측정값: {value:.1f}')               # 측정값: 25.3

print('실습 1')
x = 'PUMP_A'
y = '87'
print(f'설비 {x}, 온도 {y}도')              # 설비 PUMP_A, 온도 87도

print('실습 2')
x = 87
y = 85
z = 89
print(f'평균{(x + y + z) / 3}')             # 평균 87.0

print('실습 3')
x = 87.456
print(f'{x:.1f}' + '/' + f'{x:.2f}')        # 87.5/87.46

print('실습 4')
data = ' 5 , senor_2 , WARNING , 0.78912 '
log = data.strip().split(',')
code = log[0].strip()
sensor = log[1].strip()
status = log[2].strip()
value = float(log[3].strip())
print(f'[센서 {sensor}]상태 {status.lower()},측정값 {value:.2f}')    # [센서sensor_2]상태 warning,측정값 0.79