import pandas as pd

# 그룹 통계와 상관관계
# - 그룹 통계 -> 원본 행과 그룹 기준 비교 -> 두 기준 표 -> 상관관계

F = 'data/14_hydraulic.csv'
F_QC = 'data/14_hydraulic_qc.csv'

df = pd.read_csv(F)
qc = pd.read_csv(F_QC)

print(round(df['온도'].mean(), 2))
print(round(df['온도'].std(), 2))

print(df.groupby('냉각기상태')['온도'].mean().round(2))
# 고장    54.67
# 저하    45.46
# 정상    35.89
print(df.groupby('냉각기상태')['온도'].std().round(2))
# 고장    3.76
# 저하    1.47
# 정상    0.36

# 분산 / 표준편차
v = df.groupby('냉각기상태')['온도'].var()
std = df.groupby('냉각기상태')['온도'].std()
print(v.round(2))
# 고장    14.13
# 저하     2.15
# 정상     0.13
print(std.round(2))
# 고장    3.76
# 저하    1.47
# 정상    0.36
print((std ** 2).round(2))
# 고장    14.13
# 저하     2.15
# 정상     0.13

# agg - 여러 통계 한번에 표로 모으기
# - 리스트: 같은 대상에 여러 통계
# - 딕셔너리: 열별 통계
# - named aggregation: 결과 열의 이름까지 지정

print(df.groupby('냉각기상태')['온도'].agg(['mean', 'std', 'max']).round(2))
print(df.groupby('냉각기상태')[['온도', '진동']].agg(['mean', 'std', 'max']).round(2))

# 이름 붙이기
summary = df.groupby('냉각기상태').agg(
    평균온도=('온도', 'mean'),
    평균진동=('진동', 'mean')
)
print(summary.round(2))

# 열별로 다른 통계 목록 지정
summary2 = df.groupby('냉각기상태').agg({
    '온도': ['mean', 'std'],
    '진동': ['mean', 'max']
})
print(summary2.round(2))

print('실습 1')

import pandas as pd

F_QC = 'data/14_hydraulic_qc.csv'

qc = pd.read_csv(F_QC)

print(qc['검사결과'].value_counts())

result = qc.groupby('검사결과').agg({
    '온도': ['mean', 'std', 'max'],
    '냉각효율': ['mean']
})

print(result.round(2))

# 불합격 그룹은 합격 그룹보다 평균 온도가 높고, 평균 냉각효율은 낮음.

# transform - 그룹 통계를 원래 행에 붙이기
# - 원래 행 인덱스와 모양을 유지한다

# 같은 그룹의 평균 붙이기
print(df.groupby('냉각기상태')['온도'].mean().shape)                # (3,)
print(df.groupby('냉각기상태')['온도'].transform('mean').shape)     # (120,)

marked = df.copy()
marked['그룹평균'] = marked.groupby('냉각기상태')['온도'].transform('mean')
marked['편차'] = marked['온도'] - marked['그룹평균']
print(marked[['냉각기상태', '온도', '그룹평균', '편차']].head(3).round(2))

# pivot_table - 두 기준 표를 한 번에
# - margins=True -> 전체 집계 추가
# - 값이 없는 조합의 평균을 0으로 메우지 않도록

temp_table = pd.pivot_table(df, index='밸브상태', columns='운전부하', values='온도',
                            aggfunc='mean', margins=True, margins_name='전체')

# - index: 결과표의 행을 나누는 기준
# - columns: 결과표의 열을 나누는 기준
# - values: 각 칸에서 계산할 측정값
# - aggfunc: 그 측정값으로 요약
# - margins=True: 전체 집계 행, 열 추가
# - margins_name: 추가 집계 이름 표시

print(temp_table.round(2))

print('실습 2')

df2 = df.copy()

df2['그룹평균'] = df2.groupby('냉각기상태')['온도'].transform('mean')

df2['편차'] = df2['온도'] - df2['그룹평균']

print(df2[['냉각기상태', '온도', '그룹평균', '편차']].head(3))

max_row = df2['편차'].abs().idxmax()

print('절댓값 최대행의 편차:', round(df2.loc[max_row, '편차'], 2))
print(df2.loc[max_row, '냉각기상태'])

table = pd.pivot_table(
    df2,
    values='온도',
    index='밸브상태',
    columns='운전부하',
    aggfunc='mean',
    margins=True
)

print(table.round(2))
print('전체 평균 포함 표', table.shape)

# corr = 두 지표의 상관계수 구하기
print(round(df['온도'].corr(df['진동']), 3))            # 0.931
print(round(df['온도'].corr(df['압력']), 3))            # 0.284
print(round(df['온도'].corr(df['냉각효율']), 3))        # -0.951    

print('실습 3')

F = 'data/14_hydraulic.csv'

df = pd.read_csv(F)

print(round(df['온도'].corr(df['진동']), 3))
print(round(df['온도'].corr(df['압력']), 3))
print(round(df['온도'].corr(df['냉각효율']), 3))

cols = ['온도', '진동', '압력', '냉각효율']

result = df[cols].corr()
print(result.round(3))

# 가장 강한 짝: 온도-냉각효율 -0.951
# 가장 약한 짜기 압력-냉각효율 -0.131

print('실습 4')

num = df.select_dtypes(include='number')

corr = num.corr()

pair_table = corr.stack()
pair_table = pair_table[
    pair_table.index.get_level_values(0) <
    pair_table.index.get_level_values(1)
]

print('전체 센서 조합:', len(pair_table), '개')

strong = pair_table[pair_table.abs() >= 0.4]
print('절댓값 0.4 이상:', len(strong), '개')

very_strong = pair_table[pair_table.abs() >= 0.95]
print('절댓값 0.95 이상:', len(very_strong), '개')

top5 = very_strong.reindex(
    very_strong.abs().sort_values(ascending=False).index
).head(5)

print('상위 5개 조합:')
print(top5)