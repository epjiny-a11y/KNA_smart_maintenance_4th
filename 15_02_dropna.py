import pandas as pd

F_PROC = 'data/15_사출성형_공정.csv'
F_LOG = 'data/15_사출성형_로그.csv'

df = pd.read_csv(F_PROC)
fl = pd.read_csv(F_LOG)

# dropna: 행 삭제, 열 삭제
# - axis: 제거할 축을 선택, axis = 1 -> 열 전체가 빠지게 됨
rows_removed = df.dropna()
cols_removed = df.dropna(axis=1)
print(rows_removed.shape)
print(cols_removed.shape)
print(df.shape)

# - how: 하나라도 비면, 전부 비면
# - any, all
print(df.dropna(how='any').shape)           # (76, 22)
print(df.dropna(how='all').shape)           # (250, 22)

# - thresh: 유효값 최소 개수
print(df.dropna(thresh=20).shape)           # (162, 22)

# - subset: 중요한 열만 검사 (해당 열 결측 검사)
# - 다른 열의 결측이 남아 있어도 지정한 조건을 충족하면 유지한다
print(df.dropna(subset=['배럴온도1']).shape)

print('실습 1')

import pandas as pd

F_PROC = 'data/15_사출성형_공정.csv'

df = pd.read_csv(F_PROC)

print(df.shape)

rows_removed = df.dropna()
print(df.dropna(how='any').shape)

cols_removed = df.dropna(axis=1)
print(cols_removed.shape)

print('실습 2')

print(df.dropna(how='all').shape)
print(df.dropna(thresh=20).shape) 
print(int(df['불량여부'].isna().sum()))
print(df.dropna(subset=['불량여부']).shape)

print('실습 3')

feature_cols = df.columns.drop(['측정시각', '불량여부', '사출기'])

ratio = df[feature_cols].isna().mean() * 100

drop_cols = ratio[ratio >= 40].index.tolist()

print('제거할 열:', drop_cols)

result = df.drop(columns=drop_cols)

print('제거 한 결과의 크기:', result.shape)
print('정답 열 보존:', '불량여부' in result.columns)
print('시간 열 보존:', '측정시각' in result.columns)
print('사출기 열 보존:', '사출기' in result.columns)

print('실습 4')

# 1. 원본 데이터
original = df.copy()

# 2. 결측값이 있는 행 제거
row_drop = df.dropna()

# 3. 결측률 20% 이상인 입력 열 제거
feature_cols = df.columns.drop(['측정시각', '불량여부', '사출기'])

ratio = df[feature_cols].isna().mean() * 100
drop_cols = ratio[ratio >= 20].index.tolist()

thresh20 = df.drop(columns=drop_cols)

# 4. 각 데이터의 남은 행 수와 손실률 계산
print('원본:', len(original), '행')

print('행 제거:', len(row_drop), '행',
      '손실률:', round((1 - len(row_drop) / len(original)) * 100, 1), '%')

print('thresh20:', len(thresh20), '행',
      '손실률:', round((1 - len(thresh20) / len(original)) * 100, 1), '%')

# 5. 불량 개수와 비율 비교
for name, data in [('원본', original),
                   ('행 제거', row_drop),
                   ('thresh20', thresh20)]:

    bad = (data['불량여부'] == 1).sum()
    bad_ratio = bad / len(data) * 100

    print(name, '불량:', bad, '개',
          '비율:', round(bad_ratio, 1), '%')