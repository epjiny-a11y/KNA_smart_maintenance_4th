import numpy as np

# 인덱싱, 슬라이싱
a = np.array([0,1,2,3,4])
print(a[0], a[-1])          # 0 4
print(a[1:4])               # [1 2 3]
print(a[::2])               # [0 2 4]

print('실습 1')

import numpy as np

rpm = np.array([4603, 4500, 4700, 4800, 4900,
                5000, 5100, 5200, 5300, 4603])

print('맨 앞', rpm[0])
print('맨 뒤', rpm[-1])

print(rpm[1:4])

print(rpm[::2])

print('실습 2')

import numpy as np

sensor = np.array([
    [4603, 120],
    [4700, 125],
    [4800, 130],
    [4900, 135]
])

print(sensor[2])

print(sensor[:, 0])

print(sensor[:, 1])

# 배열 연산
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
print(a + b)            # [11 22 33]
# 같은 위치 값끼리 계산 (반복문 필요 X)
# 사칙연산 모두 같은 방식으로 계산

# 스칼라 연산
# - 숫자 하나를 배열 전체에 적용, 크기를 맞출 필요가 없다
# - 연산 숫자는 수학과 같아 곱하기 먼저
print(a * 10 + 3)

# 브로드 캐스팅
table = np.array([[72, 2.4], [95, 6.8]])
print(table.shape)          # (2, 2)
base = np.array([70, 2.0])  # (, 2)
print(table - base)
# [[ 2.   0.4]
#  [25.   4.8]]

# 한 줄짜리 기준값이 모든 행에 퍼져서 계산됨
# 조건) 작은 쪽 크기가 1이거나 같아야 함

print('실습 3')

import numpy as np

base = np.array([4603, 4700, 4800, 4900, 5000, 5100, 5200, 5300, 5400, 5500])

min = base.min()
max = base.max()

temp = base - min
result = temp / (max - min)

print(np.round(result, 2))

# 비교 연산과 불리언 배열
vals = np.array([70, 95, 71, 88, 73])
print(vals > 75)                        # [False  True False  True False]

# 불리언 인덱싱
# - 조건이 참/거짓인 배열을 만듦 -> 그 배열을 대괄호에 넣기
print(vals[vals > 75])                  # [95 88] / 참인 값만 출력

# np.where(조건, 참일 때 값, 거짓일 때 값)
print(np.where(vals > 85, 1, 0))        # [0 1 0 1 0]

# 다중 조건
print(vals[(vals > 70) & (vals < 90)])  # [71 88 73]

print('실습 4')

import numpy as np

rpm = np.array([1800, 2100, 1500, 2500, 1900, 3000])
cur = np.array([20, 22, 27, 24, 28, 23])

low = rpm < 2000

print('저회전 여부:', low)
print('저회전 회전수:', rpm[low])

warning = (rpm < 2000) | (cur > 25)

print('이상 여부:', warning)
print('이상 회전수:', rpm[warning])

print('저회전 건수:', low.sum())
print('이상 건수:', warning.sum())

print('저회전 비율:', low.mean() * 100, '%')
print('이상 비율:', warning.mean() * 100, '%')
# - low: True False 배열 -> True: 1, False: 0

print('실습 5')

import numpy as np

tor = np.array([8, 9, 7, 11, 10, 6, 12, 9, 8, 10])
mask = tor > 10

print('결과:', mask)

count = mask.sum()

rat = mask.mean()

print('조건에 걸린 시점:', count, '개')
print('비율:', rat)

# 통계
# - 정상을 알아야 이상을 알 수 있다
# ex) 평균을 알아야 평균과 크게 차이가 나는 값이 나왔을 때 이상치 판단 가능
# - 평균, 최대/최소, 표준편차, 분산
# - Numpy 에서 함수 하나로 계산

s = np.array([70, 72, 71, 95, 73])
print('합계:', s.sum())
print('평균:', s.mean())
print('중앙값:', np.median(s))
print('최대:', s.max())
print('최소:', s.min())

# 분산
stable = np.array([70, 71, 70, 72, 71])
unstable = np.array([60, 85, 65, 95, 70])
print(round(stable.var(), 1))               # 0.6
print(round(unstable.var(), 1))             # 170.0

# 표준편차
print(round(stable.std(), 2))
print(round(stable.std(), 2))               # 13.04

# axis 개념 (행, 열 방향)
mat = np.array([[70, 2.1], [72, 2.3]])
print(mat.mean(axis=0))                     # 열별 평균 (센서별)
print(mat.mean(axis=1))                     # 행별 평균 (시점별) -> 지금은 큰 의미 X
print(mat.mean())                           # 전체 평균

print('실습 6')

import numpy as np

table = np.array([
    [4603, 2],
    [4697, 21],
    [3632, 147],
    [58, 5]
])

print(np.round(table.mean(axis=0), 1))
print(np.round(table.std(axis=0), 1))

# 파일에서 배열로 불러오기(np.loadtxt)

rpm_tq = np.loadtxt('data/10_mct_tool.csv',    
                delimiter=',',          # 값을 나누는 기호
                skiprows=1,             # 첫 줄(제목)은 건너뜀
                usecols=(4,5))              
print(rpm_tq.shape)

print('실습 7')

import numpy as np

rpm = np.loadtxt(
    'data/10_mct_tool.csv',
    delimiter=',',
    skiprows=1,
    usecols=4
)

mean = rpm.mean()
std = rpm.std()
min = rpm.min()
max = rpm.max()

print('회전수 평균:', round(mean, 1))
print('표준편차:', round(std, 1))
print('최소:', round(min, 1))
print('최대:', round(max, 1))

print('실습 8')

import numpy as np

tq = np.loadtxt(
    'data/10_mct_tool.csv',
    delimiter=',',
    skiprows=1,
    usecols=5
)

up = tq[tq > 10]
print('골라낸 값:', up)

print('개수:', up.size)
print('평균:', up.mean(), 1)

print('전체 평균:', round(tq.mean(), 1))
print('평균 차이:', round(mean - tq.mean(), 1))

print('실습 9')

import numpy as np

data = np.loadtxt(
    'data/10_mct_tool.csv',
    delimiter=',',
    skiprows=1,
    usecols=(4, 5)
)

print('구조:', data.shape, data.dtype)

rpm = data[:, 0]
low = rpm[rpm <= 2000]

print('이상 시점:', low.size, '개')
print('이상 평균:', round(low.mean(), 1))
print('전체 평균:', round(rpm.mean(), 1))