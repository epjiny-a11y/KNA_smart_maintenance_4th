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

print('NaN 전체', fl.isna().sum().sum(), '개')

print('압력0:', (fl['사출압력'] == 0).sum(), '개')
print('속도 -999', (fl['스크루속도'] == -999).sum(), '개')
print('온도999:', (fl['배럴온도'] == 999).sum(), '개')

print('실습 2')
print(df.shape)     # (250, 22)
print(df.head(3).to_string(index=False))
print(df.info())
print(df['최대사출속도'].describe())

print('실습 3')

print('변환 전 결측:', fl.isna().sum().sum())

fl2 = pd.read_csv(
    F_LOG,
    na_values={
        '배럴온도': [999],
        '스크루속도': [-999]
    }
)

print('1차 변환 후 결측:', fl2.isna().sum().sum())

fl3 = pd.read_csv(
    F_LOG,
    na_values={
        '배럴온도': [999],
        '스크루속도': [-999],
        '사출압력': [0]
    }
)

print('최종 결측:', fl3.isna().sum().sum())

print('사출기:', fl3['사출기'].isna().sum())
print('온도:', fl3['배럴온도'].isna().sum())
print('압력:', fl3['사출압력'].isna().sum())
print('속도:', fl3['스크루속도'].isna().sum())

print('정답 변화 없음:', fl['불량여부'].equals(fl3['불량여부']))

print('실습 4')

count = df.isna().sum()

ratio = count / len(df) * 100

missing = count[count > 0]

print('결측이 있는 열:', len(missing), '개')

maximum = count[count == count.max()]

for col in maximum.index:
    print(col, count[col], '개', f'({ratio[col]:.1f}%)')

minimum = missing[missing == missing.min()]

for col in minimum.index:
    print(col, count[col], '개', f'({ratio[col]:.1f}%)')

print('실습 5')

count = df.isna().sum()
ratio = count / len(df) * 100

top3 = ratio.sort_values(ascending=False).head(3)

print('결측률 상위 3개 열:')
for col in top3.index:
    print(col, f'{top3[col]:.1f}%')

row_missing = df.isna().sum(axis=1)

complete = (row_missing == 0).sum()
incomplete = (row_missing > 0).sum()

print('완전한 행:', complete)
print('결측 있는 행:', incomplete)

many_missing = (row_missing >= 5).sum()
print('결측 5개 이상인 행:', many_missing)

print('실습 6')

a = df['최대사출속도'].isna()
b = df['감압시간'].isna()

print('최대사출속도 결측:', a.sum())
print('감압시간 결측:', b.sum())

print('앞 10행 결측 위치:')
print(df[['최대사출속도', '감압시간']].isna().head(10))

both = a & b
print('동시 결측:', both.sum(), '행', round(both.mean() * 100, 1), '%')

only_one = (a & ~b) | (~a & b)
print('한 열만 결측:', only_one.sum())

neither = ~a & ~b
print('두 열 모두 관측:', neither.sum())

print('전체 행:', len(df))