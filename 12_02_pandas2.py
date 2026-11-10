import numpy as np
import pandas as pd

F = 'data/12_metro_compressor.csv'
FS = 'data/12_metro_compressor_semicolon.csv'
FD = 'data/12_metro_digital.csv'

df = pd.read_csv(F)

# 데이터 미리보기 및 구조 파악

# 1) 앞 부분 미리보기
# - df.head() > 위에서 5줄, 숫자 지정 가능

print(df.head())

# 2) 뒷 부분 미리보기
# - df.tail() > 밑에서 5줄, 숫자 지정 가능

print(df.tail())

print('실습 1')

import pandas as pd

F = 'data/12_metro_compressor.csv'

df = pd.read_csv(F)

print(df.head())
print(df.tail())
print(df.head(3))
print(df.tail(10))

# 3) 행/열 크기
# df.shape
print(df.shape)         # (행, 열)

# 4) 열 이름 목록
# - df.columns   > 인덱스 형태로 출력
# - df.columns.tolist()  > 목록으로 보기 좋게

print(df.columns.tolist())
# 여기서 나오는 값으로 특정 열의 데이터 값 추출

# 5) 행 번호표
# - df.index

print(df.index)         # RangeIndex(start=0, stop=200, step=1)
# 0부터 시작, 199까지 1씩

# 6) 열별 자료형
# df.dtypes

print(df.dtypes)
print('-------------------------------------')
print(pd.read_csv(FD).dtypes)
# 측정시각       str
# 압축기      int64
# 타워       int64
# 저압스위치    int64
# dtype: object

df2 = pd.read_csv(FD, dtype={'압축기': str})

print('실습 2')

FD = 'data/12_metro_digital.csv'

df = pd.read_csv(FD)

print(df.shape)
print(df.columns.tolist())
print(df.dtypes)
print(df.head())

# 이 표는 120행 4열로 구성된 디지털 신호 데이터이며, 숫자형 열 3개와 문자형 열 1개를 포함하고, 신호 값을 0과 1로 표현한 데이터이다.

# 7) 전체 구조
# - df.info()

print(df.info())
# <class 'pandas.DataFrame'>
# RangeIndex: 120 entries, 0 to 119
# Data columns (total 4 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   측정시각    120 non-null    str  
#  1   압축기     120 non-null    int64
#  2   타워      120 non-null    int64
#  3   저압스위치   120 non-null    int64
# dtypes: int64(3), str(1)
# memory usage: 3.9 KB
# None

# 기초 통계 요약
# - 숫자 열들의 평균/최대/최소 등을 한번에 자동 계산. 글자 열은 자동으로 빠짐

print(df.describe().round(2))

# 특정 조건에서의 통계 필요시

df = pd.read_csv(F)

state = df['가동상태'].values
cur = df['모터전류'].values

print(round(float(np.mean(cur[state == '가동'])), 2))

print('실습 3')

F = 'data/12_metro_compressor.csv'

df = pd.read_csv(F)

print(df.info())            # 전체 200행

# 오일온도    199 non-null / 200 - 199 = 결측 개수 1개

print('실습 4')

F = 'data/12_metro_compressor.csv'

df = pd.read_csv(F)

print(df.describe().round(2))

# 압축압력    배출압력    저장압력    오일온도    모터전류
# 9.17         -0.02       9.17       63.18        2.06
# 9.18         -0.02       9.18       62.90        0.04

state = df['가동상태'].values
cur = df['모터전류'].values

print(round(float(np.mean(cur[state == '가동'])), 2))       # 4.25
print(round(float(np.mean(cur[state == '정지'])), 2))       # 0.04

print('실습 6')

FS = 'data/12_metro_small.csv'

df = pd.read_csv(FS)

print(df.head(3))
print('크기:', df.shape)
print(df.info())
stats = df.describe()

miss = int(df["오일온도"].isna().sum())
print('오일온도 결측:', miss, '건')

mean_current = round(float(stats["모터전류"]["mean"]), 2)
median_current = round(float(stats["모터전류"]["50%"]), 2)
print("모터전류 평균/중앙값:", mean_current, median_current)

# 총 30행 7열로 구성되어 있는 데이터이다.
# 결측값은 1개이다.
# 모터전류의 평균은 1.38이다.
# 모터전류의 중앙값은 0.04이다.
# 평균이 중앙값보다 크므로 일부 큰 전류값이 평균에 영향을 준 것으로 보인다.