# 리스트
# 형식: 이름 = [값1, 값2, ...]
# - 리스트는 여러 값을 '순서대로' 하나의 이름에 담는다.

temps = [25, 26, 24, 27, 26]            # 숫자 리스트
machines = ['펌프', '모터', '압축기']   # 글자 리스트 ('' 필수)
mixed = ['펌프', 87, True]              # 종류가 달라도 한 리스트에 담을 수 있음
result = []

print(len(temps))                       # 5
print(len(result))                      # 0

print('실습 1')
print(temps)                            # [25, 26, 24, 27, 26]
print(len(temps))                       # 5
print(result)                           # []
print(len(result))                      # 0

print('실습 2')
temps = [22, 26, 27, 24, 25, 23]
print(temps[0])                         # 22
print(temps[2])                         # 27
print(temps[5])                         # 23

print('실습 3')
lines = [120, 118, 116, 114, 112, 102]
x = lines[0]
y = lines[5]
print(x + y)                            # 222
print((x + y) / 2)                      # 111.0

print('실습 4')
temps = [22, 24, 27, 20, 23, 25, 26, 28, 30, 21]
print(temps[:3])                        # [22, 24, 27]
print(temps[-3:])                       # [28, 30, 21]
print(len(temps[:3]))                   # 3

print('실습 5')
num = [3, 4, 5, 6, 5, 4, 6, 7, 8, 7, 5, 3]
print(num[:6])                  # [3, 4, 5, 6, 5, 4]
first = num[:6]
print(num[-6:])                # [6, 7, 8, 7, 5, 3]
second = num[-6:]
print(len(first), len(second))  # 6 6

# 값 바꾸기 / in 존재 확인
# 형식: 리스트[번호] = 새 값 / 값 in 리스트
nums = [25, 26, 24, 28, 27]
nums[2] = 99
print(nums)                     # [25, 26, 99, 28, 27]
print('모터' in machines)       # True

# 값 추가 - append, insert, extend
# 형식: 리스트.append(값) / 리스트.insert(위치, 값) / 리스트.extend(다른 리스트)
data = [25, 26, 24]
data.append([28])
data.insert(1, 99)
data.extend([30, 31])
print(data)

print('실습 6')
temps = [25, 26, 240, 28, 27]
print(240 in temps)             # True
idx = temps.index(240)
temps[idx] = 24
print(temps)                    # [25, 26, 24, 28, 27]
print(240 in temps)             # False

print('실습 7')
x = []
x.append(30)
print(x)                        # [30]
x.insert(0, 28)
print(x)                        # [28, 30]
x.extend([31, 32])
print(x)                        # [28, 30, 31, 32]

# 값 삭제 - remove, pop, del
# 형식: 리스트.remove(값) / 꺼낸 값 = 리스트.pop(위치) / del 리스트[위치]
d = [25, 26, 24, 28, 27]
d.remove(24)                    
print(d)                        # [25, 26, 28, 27]
got = d.pop(1)
print(got, d)                   # 26 [25, 28, 27]
del d[0]
print(d)                        # [28, 27]

# 정렬, 탐색 - sort, reverse / count, index
# 형식: 리스트.sort()   .reverse()  .count(값)  .index(값)
x = [27, 24, 30 ,22, 26]
x.sort()   
print(x)                        # [22, 24, 26, 27, 30]
x.sort(reverse=True)
print(x)                        # [30, 27, 26, 24, 22]
x.reverse()
print(x)                        # [22, 24, 26, 27, 30]

r = ['정상', '이상', '정상', '정상', '이상']
print(r.count('정상'), r.index('이상'))     # 3 1

print('실습 8')
x = [999, 25, 26, 24, 28, 26]
x.remove(999)
print(x)                        # [25, 26, 24, 28, 26]
y = x.pop(1)
print(y)                        # 26
del x[0]
print(x)                        # [24, 28, 26]

print('실습 9')
temps = [26, 22, 30, 24, 28, 24, 27]
temps.sort()
print(temps)                             # [22, 24, 24, 26, 27, 28, 30]
temps.reverse()
print(temps)                             # [30, 28, 27, 26, 24, 24, 22]
print(temps.count(24), temps.index(24))  # 2 4