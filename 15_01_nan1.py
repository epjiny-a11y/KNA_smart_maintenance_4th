import pandas as pd

F_PROC = 'data/15_사출성형_공정.csv'
F_LOG = 'data/15_사출성형_로그.csv'

df = pd.read_csv(F_PROC)
fl = pd.read_csv(F_LOG)

# 결측 처리
# - 종류: NaN, None, NA, NaT
# - 표현은 달라도 isna()로 결측 여부 확인 가능

s = pd.Series([10, None, 20])
print(s.mean())         # 15.0 -> NaN 값이 있다고 해서 계산이 멈추지 않음 (10 + 20) / 2
print(s + 1)            # 11.0, NaN, 21.0

print('실습 1')

print(fl.shape)

print('NaN 전체', fl.isna().sum().sum())

print('압력0:', (fl['사출압력'] == 0).sum(), '개')
print('속도 -999', (fl['스크루속도'] == -999).sum(), '개')
print('온도999:', (fl['배럴온도'] == 999).sum(), '개')