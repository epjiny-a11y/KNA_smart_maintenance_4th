# for 반복문
# for문 (range 이용한 반복)
# 형식: for 변수 in range(횟수):
for i in range(5):
    print('안녕하세요')

for i in range(5):
    print(i)                 # 0 1 2 3 4

# range(시작, 끝, 증가값)
for i in range(1, 10, 2):    # 1 3 5 7 9
    print(i)
for i in range(5, 0, -1):    # 5 4 3 2 1
    print(i)

print('실습 1')
n = int(input('끝 숫자 N: '))

# 1부터 N까지
for i in range(1, n + 1):
    print(i)

# 짝수만
for i in range(2, n + 1, 2):
    print(i)

# 역순
for i in range(n, 0, -1):
    print(i)

# 누적 변수 패턴 (합계, 갯수, 평균)
total = 0
for i in range(1,6):
    total += i
print('합계:', total)                  # 15

# 조건 만족하는 경우 세기
count = 0
for i in range(1, 11):
    if i > 5:
        count += 1
print('갯수:', count)                  # 5

# 평균
total, count = 0, 0
for i in range(1, 6):
    total += i
    count += 1
if count > 0:
    print('평균:', total/count)        # 3.0

print('실습 2')
n = int(input('끝 숫자 N: '))
total = 0
for i in range(1, n + 1):
    total = total + i
print('합:', total)

# enumerate: 순서 + 값을 함께 준다
temps = [25, 26, 24]
for idx, t in enumerate(temps):
    print(idx + 1, '번째', t)           # 1 번째: 25...

# 중첩 반복 (바깥 한 바퀴마다 안쪽이 처음부터 끝가지)
for dan in range(2, 4):                 # 바깥: 2, 3단
    for su in range(1, 4):              # 안쪽: 1,2,3 (바깥 한 번마다 3번씩)
        print(f'{dan} x {su} = {dan * su}')
    print('------')

print('실습 3')
for dan in range(2, 10):
    for su in range(1, 10):
        print(f'{dan} x {su} = {dan * su}')
    print('------')

print('실습 4')
count = 0
for i in range(5):
    x = int(input('측정값 입력: '))
    if x > 80:
        count += 1
print('초과 개수:', count)