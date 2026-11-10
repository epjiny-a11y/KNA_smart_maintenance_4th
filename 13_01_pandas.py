import pandas as pd

F_SHOT = 'data/13_diecasting_shot.csv'
F_SMALL = 'data/13_diecasting_small.csv'

# 열 골라내기
# - 열 이름

df = pd.read_csv(F_SMALL)

print('이름으로 앞 3개:', df['실린더압력'].head(3).tolist())            # [214.0, 217.0, 215.0]

# 단일 열 선택
# - df['실린더압력']
# - 결과 값은 Series

print(df['실린더압력'])
# 0     214.0
# 1     217.0
# 2     215.0

# 복수 열 선택
# - 여러 열은 이름들을 리스트로 묶어서 넣는다
# - 결과 값은 DataFrame

print(df[['형체력', '실린더압력']])

print('실습 1')

import pandas as pd

F_SMALL = 'data/13_diecasting_small.csv'

df = pd.read_csv(F_SMALL)

print(df['형체력'].head(3), type(df))

col = df[['형체력', '실린더압력']]

print("자료형:", type(col))
print("크기:", col.shape)

print(df[["형체력"]])

# 행 선택
# - 라벨과 위치 번호의 차이
# - 라벨: 그 행에 붙은 이름표 = 인덱스 값
# - 위치 번호: 맨 위에서부터 몇 번째인지, 항상 0부터

sorted = df.sort_values('형체력', ascending=False)

print('정렬 후 인덱스 앞 4개:', sorted.index[:4].tolist())          # 정렬 후 인덱스 앞 4개: [22, 17, 27, 12]
print('정렬 후 iloc[0] 샷:', int(sorted.iloc[0]['샷']))             # 정렬 후 iloc[0] 샷: 23
print('정렬 후 loc[0] 샷:', int(sorted.loc[0, '샷']))               # 정렬 후 loc[0] 샷: 1

# 여러 행 선택
print(df.loc[0:4].shape)                                            # (5, 8)
print(df.iloc[0:4].shape)                                           # (4, 8)

# 행, 열 동시 선택
# df.loc[행,열] - 열 이름 사용 O / df.iloc[행,열] - 열이름 사용 X -> 숫자로 접근

print(df.loc[0:4, ['실린더압력', '형체력']].shape)                  # (5, 2)
print(df.iloc[0:5, [2, 6]].shape)                                  # (5, 2)

print('실습 2')

df = pd.read_csv(F_SMALL)

print(df.loc[0, '샷'])
print(df.iloc[0]['샷'])

df2 = df.sort_values('형체력', ascending=False)

print(df2.loc[0, '샷'])
print(df2.iloc[0]['샷'])

print(df2.index[0])

print('실습 3')

df = pd.read_csv(F_SMALL)

print('칸 이름:', list(df.columns))          # 2, 6

df1 = df.loc[0:4, ['실린더압력', '형체력']]
print(df1.shape)

df2 = df.iloc[0:5, [2, 6]]
print(df2.shape)

print(df1.equals(df2))                      # True  

print('실습 4')

F_SHOT = 'data/13_diecasting_shot.csv'

df = pd.read_csv(F_SHOT)

print('전체', df.shape)
print(df.columns.tolist())

a = df.loc[0:9, ['설비ID', '비스킷두께', '품질등급']]
print('골라낸 표', a.shape)

b = df.iloc[0:5, :]
print(b.shape)