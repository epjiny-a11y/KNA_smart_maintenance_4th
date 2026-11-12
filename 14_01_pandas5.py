import pandas as pd

F = 'data/14_hydraulic.csv'
F_QC = 'data/14_hydraulic_qc.csv'

df = pd.read_csv(F)
qc = pd.read_csv(F_QC)

print(df.shape, qc.shape)           # (120, 8) (200, 11)

# 빈도와 그룹 집계
# - 값 별로 세기와 그룹 별로 집계하기

# 1. 빈도
# - value_counts
# - pd.cut

print(df['냉각기상태'].value_counts())
# 냉각기상태
# 고장    40
# 저하    40
# 정상    40
# Name: count, dtype: int64

print(df['밸브상태'].value_counts())
# 밸브상태
# 정상    61
# 지연    20
# 경미    20
# 심각    19
# Name: count, dtype: int64

# 개수 -> 비율: normalize
counts = df['result'].value_counts()
ratios = df['result'].value_counts(normalize=True)
print(counts)                           # 정상 67 / 고장 53
# print(ratios.round(3))
print((ratios * 100).round(1))          # 정상 55.8 / 고장 44.2

print('실습 1')

import pandas as pd

F = 'data/14_hydraulic.csv'

df = pd.read_csv(F)

print(df.shape)

print(df['밸브상태'].value_counts())
ratios = (df['밸브상태'].value_counts(normalize=True))
print((ratios * 100).round(1))

print(df['운전부하'].value_counts())
ratios2 = (df['운전부하'].value_counts(normalize=True))
print((ratios2 * 100).round(1))

counts = df['밸브상태'].value_counts()

print('최다:', counts.idxmax(), counts.max())
print('최소:', counts.idxmin(), counts.min())

# pd.cut
band = pd.cut(df['온도'], bins=[0, 40, 50, 200], labels=['낮음', '보통', '높음'], right=True)
print(band.value_counts(sort=False))
# 온도
# 낮음    41
# 보통    40
# 높음    39
# Name: count, dtype: int64

print('실습 2')

F_QC = 'data/14_hydraulic_qc.csv'

qc = pd.read_csv(F_QC)

print(qc.shape)

counts = qc['검사결과'].value_counts()
print(counts)

ratio = qc['검사결과'].value_counts(normalize=True)
print(ratio.round(3))

print('불합격이 전체의 약', round(ratio['불합격'] * 100, 1), '%')

print('실습 3')

print('진동 최솟값:', df['진동'].min())
print('진동 최댓값:', df['진동'].max())

df['진동구간'] = pd.cut(df['진동'], bins=[0, 0.6, 0.7, 10], labels=['약함', '보통', '강함'])

print(df['진동구간'].value_counts())
print('구간 미지정 개수:', df['진동구간'].isna().sum())

counts = df['진동구간'].value_counts()

print('최대 구간:', counts.idxmax())
print('최소 구간:', counts.idxmin())

# 그룹 집계
# - 분할 -> 적용 -> 결합 구조
# - groupby

means = df.groupby('냉각기상태')['온도'].mean()
print(means.round(2))
# 고장    54.67
# 저하    45.46
# 정상    35.89

print(df.groupby('냉각기상태')['온도'].max())
# 고장    57.8
# 저하    51.2
# 정상    36.4

# 여러 키 그룹 코드
keys = ['냉각기상태', '운전부하']
print(df.groupby(keys)['온도'].mean().round(2))
# 냉각기상태  운전부하
# 고장     고부하     55.51
#        저부하     54.05
# 저하     고부하     44.07
#        저부하     45.58
# 정상     고부하     35.89

# crosstab
print(pd.crosstab(df['냉각기상태'], df['운전부하']))
# 운전부하   고부하  저부하
# 냉각기상태          
# 고장      17   23
# 저하       3   37
# 정상      40    0

print('실습 4')

F_QC = 'data/14_hydraulic_qc.csv'

qc = pd.read_csv(F_QC)

counts = df['냉각기상태'].value_counts()
print(counts)

mean = df.groupby('냉각기상태')['온도'].mean()
print(mean.round(2), '평균')

max = df.groupby('냉각기상태')['온도'].max()
print(max, '최댓값')

dif = mean.max() - mean.min()
print('차이', round(dif, 2), '도')

print('실습 5')

F = 'data/14_hydraulic.csv'

df = pd.read_csv(F)

counts = df.groupby('밸브상태')['밸브상태'].count()
print('전체', counts)

bad = df[df['result'] == '고장']

bad_counts = bad.groupby('밸브상태')['result'].count()
print('고장 건수', bad_counts)

rat = (bad_counts / counts).fillna(0)
print('고장 비율', rat.round(3))

print(rat.idxmax())
print(round(rat.max(), 3))

# 심각 19건중 14건이 고장 - 비율 0.737