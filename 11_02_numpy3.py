import numpy as np

F = 'data/11_hydraulic_cooler.csv'

def col(c):
    return np.genfromtxt(F, delimiter=',', skip_header=1, usecols=c)

# isnan - 결측값 위치 찾기
# - 결측값: 값이 빈 칸 -> 0이 아니라 값을 모름

x = np.array([2.0, np.nan, 4.0])
print(np.isnan(x))                  # [False  True False]
print(np.isnan(x).sum())            # 1

# nanmean, nanstd - 결측값을 무시한 통계
temp = np.array([70.1, np.nan, 71.2, 70.8])
print(np.mean(temp))                # nan
print(round(np.nanmean(temp), 2))   # 70.7

# nanmean, nanmax, nanmin

print('실습 1')

import numpy as np

F = 'data/11_hydraulic_cooler.csv'

def col(c):
    return np.genfromtxt(F, delimiter=',', skip_header=1, usecols=c)

vib = col(2)

miss = np.isnan(vib)
count = miss.sum()
ratio = miss.mean()
avg = np.nanmean(vib)

print('결측', count, '건')
print('비율', ratio)
print('결측 제외 평균', round(avg, 3))
print('일반 평균', vib.mean())

# 백분위수, 사분위수, - percentile, quantile
# - 데이터를 크기순으로 줄 세웠을 때 특정 위치의 값
# - 25, 50, 75 백분위수 -> 1사분위, 중앙값, 3사분위
# - 평균과 달리 극단적인 이상값에 휘둘리지 않음

vib_s = np.array([2.0, 2.2, 2.5, 2.8, 3.0, 6.5])
print(np.round(float(np.percentile(vib_s, 25)), 2))         # 2.28
print(np.round(float(np.percentile(vib_s, 75)), 2))         # 2.95

# 여러 자리 한번에
print(np.round(np.percentile(vib_s, [25, 50, 75]), 2))      # [2.28 2.65 2.95]

# quantile: 25 -> 0.25
print(np.round(float(np.quantile(vib_s, 0.25)), 2))         # 2.28

# 사분위 기반 이상치 범위 - IQR

q1, q3 = np.percentile(vib_s, [25, 75])
iqr = q3 - q1
upper = q3 + 1.5 * iqr
print(vib_s[vib_s > upper])                                 # [6.5]

# 평균/표준편차로 정규화 - z-score
# - 부호의 의미: 양수는 평균보다 위, 음수는 아래
# - 방향 무시하고 크기만 보려면 절댓값 필요

z = (vib_s - np.mean(vib_s)) / np.std(vib_s)
print(vib_s[np.abs(z) > 2])

print('실습 2')

F = 'data/11_hydraulic_cooler.csv'

def col(c):
    return np.genfromtxt(F, delimiter=',', skip_header=1, usecols=c)

temp = col(1)

miss = np.isnan(temp)
clean = temp[miss == False]

q1 = np.percentile(clean, 25)
q3 = np.percentile(clean, 75)
iqr = q3 - q1
upper = q3 + 1.5 * iqr

out = clean[clean > upper]

print('상한', round(upper, 1))
print('걸리는 값', out)
print(len(out), '건')

print('실습 3')

F = 'data/11_hydraulic_cooler.csv'

def col(c):
    return np.genfromtxt(F, delimiter=',', skip_header=1, usecols=c)

data = col((0, 1))

cyc = data[:, 0]
temp = data[:, 1]
avg = np.nanmean(temp)
std = np.nanstd(temp)

# 표준화
z = (temp - avg) / std
mask = np.abs(z) > 2

print(cyc[mask].astype(int))
print('최대 Z-score:', round(np.nanmax(z), 2))

print('실습 4')

F = 'data/11_hydraulic_cooler.csv'

def col(c):
    return np.genfromtxt(F, delimiter=',', skip_header=1, usecols=c)

cyc = col(0)
temp = col(1)

avg = np.nanmean(temp)
std = np.nanstd(temp)

upper = avg + 3 * std

mask = temp > upper
alarm = cyc[mask]

print('3시그마 상한', round(upper, 2))
print('경보 사이클', alarm.astype(int))
print('경보 개수', len(alarm))

# 센서 간 상관관계 - corrcorf
# - 세기는 절댓값이 정함. +0.99와 -0.99는 세기가 똑같고 방향만 반대
# - 양수: 한쪽이 오르면 다른 한쪽도 오름 / 음수는 반대
# - 0에 가까움 -> 관계가 없는 상태

temp = np.array([70, 72, 74, 76, 78])
vib = np.array([2.0, 2.2, 2.5, 2.7, 3.0])
print(round(float(np.corrcoef(temp, vib)[0, 1]), 3))            # 0.998

# 2D 배열 axis별 통계 활용
# 행은 센서, 열은 시점인 행렬 axis로 방향을 정해 통계
# axis = 1 - 각 행을 옆으로 > 센서별 통계
# axis = 0 - 각 행을 아래로 > 시점별 통계

data = np.array([[70., 72., 74.], [2.0, 2.2, 2.5]])
print(np.round(np.mean(data, axis = 1), 2))                     # [72.    2.23]
print(np.round(np.mean(data, axis = 0), 2))                     # [36.   37.1  38.25]

print('실습 5')

F = 'data/11_hydraulic_cooler.csv'

def col(c):
    return np.genfromtxt(F, delimiter=',', skip_header=1, usecols=c)

temp = col(1)
ce = col(3)

corr = np.corrcoef(temp, ce)

print('상관계수 행렬')
print(corr)

result = corr[0, 1]

print('상관계수', round(result, 2))

print('실습 6')

F = 'data/11_hydraulic_cooler.csv'

def col(c):
    return np.genfromtxt(F, delimiter=',', skip_header=1, usecols=c)

M = np.stack([col(1), col(2), col(3), col(4)])
print(M.shape)  # (4, 50)
print(np.round(np.nanmean(M, axis = 1), 1))    
print(np.round(np.nanstd(M, axis = 1), 1))      

print('실습 7')

F = 'data/11_hydraulic_cooler.csv'

def col(c):
    return np.genfromtxt(F, delimiter=',', skip_header=1, usecols=c)

cyc = col(0)
temp = col(1)

avg = np.nanmean(temp)
cs = np.cumsum(temp - avg)
idx = np.argmin(cs)

print(int(cyc[idx]), '번과', int(cyc[idx + 1]), '번 사이가 경계 후보')

print('실습 8')

F = 'data/11_hydraulic_cooler.csv'

def col(c):
    return np.genfromtxt(F, delimiter=',', skip_header=1, usecols=c)

cyc = col(0)
temp = col(1)
ce = col(3)
status = col(5)

z_temp = (temp - np.nanmean(temp)) / np.nanstd(temp)
z_ce = (ce - np.nanmean(ce)) / np.nanstd(ce)

z_temp = np.abs(z_temp)
z_ce = np.abs(z_ce)
score = z_temp + z_ce

top = np.argsort(score)[-3:][::-1]

print(score.shape)          # (50,)

print(f'최고 점수 {int(cyc[top[0]])}번({score[top[0]]:.2f})')
print('상위 세 시점', cyc[top].astype(int))
print('교육용 상태 라벨(47~50번)은', *cyc[status == 1].astype(int), sep=' ')