print('실습 1')
temps = [32, 25, 35, 28, 31]
for temp in temps:
    if temp >= 30:
        print('고온:', temp)

print('실습 2')
hours = [8, 4, 6, 12, 10, 3, 9]
for hour in hours:
    if hour >= 5 and hour <= 10:
        print(hour)

# 최대, 최소
temps = [25, 32, 28, 36, 27, 31]
biggest = temps[0]
for t in temps:
    if t > biggest:
        biggest = t                 # 더 큰값일 때 갱신
print(biggest)                      # 36

# 빈 리스트 채우기
doubled = []
for t in temps:
    doubled.append(t * 2)
print(doubled)                      # [50, 64, 56, 72, 54, 62]

print('실습 3')
temps = [32, 36, 31, 28, 25]
total = 0
count = 0
for t in temps:
    if t >30:
        total += t
        count += 1
if count > 0:
    print('합:', total)
    print('개수:', count)
    print('고온 평균:', total / count)

print('실습 4')
temps = [32, 35, 31, 33, 25, 28]
hot = []
for t in temps:
    if t > 30:
        hot.append(t)
print('개수:', len(hot))
print('원본 리스트:', temps)
print('새 리스트:', hot)

print('실습 5')
temps = [25, 26, 24, 28, 27]
Fahrenheit = []
for t in temps:
    result = t * 1.8 + 32
    Fahrenheit.append(result)
print('섭씨:', temps)
print('화씨:', Fahrenheit)

# 중첩 리스트 - 리스트 안에 리스트
# 표(행, 열)처럼 한 줄에 여러 값이 묶인 데이터. 바깥 반복은 '행', 안쪽 인덱스로 '열'
rows = [['펌프', 25], ['모터', 32], ['압축기', 28]]
for row in rows:
    print(row[0], '온도', row[1])

print('실습 6')
temps = [25, 32, 35, 28, 31, 36, 24, 33, 29, 27]
total = 0
hot = []
for t in temps:
    total += t
    if t > 30:
        hot.append(t)
average = total / len(temps)
hot_total = 0
for h in hot:
    hot_total += h
hot_average = hot_total / len(hot)
print('전체 평균:', average)
print('고온 개수:', len(hot))
print('고온 평균:', hot_average)