import numpy as np

F = 'data/11_diecasting_series.csv'

ct = np.genfromtxt(F, delimiter=',', skip_header=1, usecols=1)
print(ct.shape, ct.dtype)           # (50,) float64

def col(c):
    return np.genfromtxt(F, delimiter=',', skip_header=1, usecols=c)

# 자리 찾기
# fancy indexing: 여러 위치 한번에 추출 가능 (떨어진 자리도 한번에 가능)

vib = np.array([2.1, 2.3, 2.0, 5.8])
pick = np.array([0, 3])
print(vib[pick])                    # [2.1 5.8]

# 정렬과 정렬 순서
# - sort, argsort: 원래 자리 번호 돌려줌

print(np.sort(vib))                 # [2.  2.1 2.3 5.8]
print(np.argsort(vib))              # [2 0 1 3]

print('실습 1')

import numpy as np

F = 'data/11_diecasting_series.csv'

data = np.genfromtxt(F, delimiter=',', skip_header=1, usecols=(0, 1))

shot = data[:, 0]
ct = data[:, 1]

idx = np.argmax(ct)
num = int(shot[idx])
max = ct[idx]

print(num, '번 샷')
print('사이클 타임', max, '초')
print('배열 인덱스', idx)

# diff
vib = np.array([2.0, 2.1, 2.2, 7.0, 7.1])
change = np.diff(vib)
print(np.round(change, 1))              # [0.1 0.1 4.8 0.1]
print(np.argmax(change))                # 2

print('실습 2')

import numpy as np

F = 'data/11_diecasting_series.csv'

data = np.genfromtxt(F, delimiter=',', skip_header=1, usecols=(0, 1))

num = data[:, 0]
ct = data[:, 1]

diff = np.diff(ct)
change = np.abs(diff)
idx = np.argmax(change)

print('변화 구간', int(num[idx]), '번과', int(num[idx+1]), '번 사이')
print('변화량', round(change[idx], 1), '초')

# clip - 보정
pres = np.array([4.5, 9999.0, 4.6, -1.0])
fixed = np.clip(pres, 0, 10)
print(fixed)                # [ 4.5 10.   4.6  0. ] -> 개수는 변동 X

# cumsum - 누적 합
defects = np.array([0, 1, 0, 2, 3, 5])
print(np.cumsum(defects))

# np.where 심화
vib = np.array([2.1, 3.5, 2.0, 6.2])
label = np.where(vib >= 5, 2, np.where(vib >= 3, 1, 0))         # 5이상: 2, 3이상: 1, 나머지: 0
print(label)

# unique - 중복 정리
# - return_counts 옵션: 각 종류의 개수 확인
status = np.array([0, 0, 1, 0, 2, 1, 0])
kinds, counts = np.unique(status, return_counts=True)
print(kinds)
print(counts)

print('실습 3')

import numpy as np

F = 'data/11_diecasting_series.csv'

data = np.genfromtxt(F, delimiter=',', skip_header=1, usecols=(2))

cyl = data.copy()

cyl[0] = 9999

print('보정 전 평균:', round(cyl.mean(), 1))

fixed = np.clip(cyl, 100, 300)

print('보정 후 평균:', round(fixed.mean(), 1))

print('실습 4')

import numpy as np

F = 'data/11_diecasting_series.csv'

ct = np.genfromtxt(F, delimiter=',', skip_header=1, usecols=(1))

label = np.where(ct >= 1000, 2, np.where(ct >= 50, 1, 0))

kinds, count = np.unique(label, return_counts=True)
print(kinds, count) 
print(count / count.sum())   

# any, all - 조건 충족 여부 판정
# - any: 하나라도 만족하면 True
# - all: 모두 만족해야 True

vib = np.array([2.1, 3.5, 2.0, 6.2])
print(np.any(vib > 5))
print(np.all(vib < 10))

# concatenate, stack - 배열 합치기
am = np.array([2.0, 2.1, 2.2])
pm = np.array([2.3, 2.4, 2.5])
print(np.concatenate([am, pm]))         # [2.  2.1 2.2 2.3 2.4 2.5]
print(np.stack([am, pm]))               
# [[2.  2.1 2.2]
#  [2.3 2.4 2.5]]

print('실습 5')

import numpy as np

F = 'data/11_diecasting_series.csv'

data = np.genfromtxt(F, delimiter=',', skip_header=1)

ct = data[:, 1]
cyl = data[:, 2]
rpm = data[:, 3]
cur = data[:, 4]

M = np.stack([ct, cyl, rpm, cur], axis=0)

print('전체:', M.shape)

last = M[:, -10:]

print('마지막 10개:', last.shape)

print('실습 6')

import numpy as np

F = 'data/11_diecasting_series.csv'

data = np.genfromtxt(F, delimiter=',', skip_header=1, usecols=(0, 1, 2))

shot = data[:, 0]
ct = data[:, 1]
cyl = data[:, 2]

idx = np.argmax(ct)

print('최대', int(shot[idx]), '번', ct[idx])

diff = np.diff(ct)
change = np.abs(diff)
idx2 = np.argmax(change)

print('급변', int(shot[idx2]), '->', int(shot[idx2+1]))

warning = (ct >= 50) | (cyl < 150)

print('경고 비율', warning.mean())

rank = np.argsort(ct)[-3:][::-1]

print('상위 세 시점:', shot[rank].astype(int))