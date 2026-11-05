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