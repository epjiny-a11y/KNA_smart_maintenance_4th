import pandas as pd

F_SHOT = 'data/13_diecasting_shot.csv'

# 조건 필터링과 정렬
df = pd.read_csv(F_SHOT)
print(df.shape)        

# 배열에서 하던 것
arr = df['비스킷두께'].values
print('배열에서 조건 참 개수:', int((arr >= 16).sum()))           # 74

# 표에서 하는 것
print('표에서 조건 참 개수:', int((df['비스킷두께']>= 16).sum()))   # 74

# 조건 -> boolean Series
s = df['비스킷두께'] >= 16
print(s.head(3).tolist())                                         # [False, False, False]

print(int(df['비스킷두께'].isna().sum()))                           # 14
print(int((df['비스킷두께'] < 16).sum()))                           # 200 - 74 - 14 = 112

print('실습 1')

import pandas as pd

F_SHOT = 'data/13_diecasting_shot.csv'

df = pd.read_csv(F_SHOT)
print(df.shape)  

s = df['비스킷두께'] >= 16
print('조건 True:', int((arr >= 16).sum()), '개')

df2 = df[s]

print('추출:', len(df2), '행')

print('16 미만:', int((df['비스킷두께'] < 16).sum()), '행')
print('결측:', int(df['비스킷두께'].isna().sum()), '행')            

# 복합 조건
both = df[(df['비스킷두께'] >= 16) & (df['사이클타임'] >= 25)]
either = df[(df['비스킷두께'] >= 16) | (df['사이클타임'] >= 25)]

print(len(both), len(either))                          # 72 86

# 부정 조건: ~
print(len(df[~(df['품질등급'] == '불량')]))             # 180

# isin: 값이 포함되어 있는지
print(len(df[df['품질등급'].isin(['주의', '불량'])]))    # 38, | 사용과 같은 결과

# between: 사이를 의미(양쪽 경계 모두 포함)
print(len(df[df['비스킷두께'].between(10, 16)]))         # 117

# 문자열 조건
# - 숫자 열에는 쓸 수 없음
# - str.contains: 해당 문자열을 포함하는 값
print(len(df[df['설비ID'].str.contains('A')]))          # 111, A라인 전체

# - str.split, str.replace, str.strip ...
print(df['설비ID'].head(1).tolist())                    # ['DIE-A-01']
print(df['설비ID'].str.split('-').head(1).tolist())     # [['DIE', 'A', '01']]

print('실습 2')

F_SHOT = 'data/13_diecasting_shot.csv'

df = pd.read_csv(F_SHOT)

both = df[(df['비스킷두께'] >= 16) & (df['사이클타임'] >= 25)]
print('그리고', len(both), '줄')

either = df[(df['비스킷두께'] >= 16) | (df['사이클타임'] >= 25)]
print('또는', len(either), '줄')

print('불량이 아닌 행', len(df[~(df['품질등급'] == '불량')]), '줄')

print('실습 3')

F_SHOT = 'data/13_diecasting_shot.csv'

df = pd.read_csv(F_SHOT)

print('목록 매칭', len(df[df['품질등급'].isin(['주의', '불량'])]), '줄')
print('범위 검사', len(df[df['비스킷두께'].between(10, 16)]), '줄')
print('글자 포함', len(df[df['설비ID'].str.contains('A')]), '줄')
print('정확히 일치', len(df[df['설비ID'] == 'DIE-A-01']), '줄')

# 정렬, 복사본
# 정렬 - sort_values
# - 기본값은 작은 값부터인 오름차순
# - 한 열로 정렬해도 모든 열이 행 단위로 함께 이동한다
asc = df.sort_values('비스킷두께')
print(asc['비스킷두께'].head(3).tolist())           # [2.0, 2.0, 4.0]

# 내림 차순
dec = df.sort_values('사이클타임', ascending=False)
print(dec['사이클타임'].head(3).tolist())           # [6170.0, 652.3, 125.9]

# 다중 키 정렬
two = df.sort_values(['품질등급', '비스킷두께'], ascending=[True, False])
print(two['샷'].head(3).tolist())                   # [198, 192, 197]

# copy
x = df[df['품질등급'] == '불량'].copy()
print(x.shape)                                      # (20, 8)
x['위험등급'] = '높음'
print(x.shape)                                      # (20, 9)

print('실습 4')

F_SHOT = 'data/13_diecasting_shot.csv'

df = pd.read_csv(F_SHOT)

df1 = df.sort_values('비스킷두께', ascending=False)
print('두께 상위샷', df1['샷'].head(5).tolist())

df2 = df.sort_values(['품질등급', '사이클타임'], ascending=[True, False])
print('가나다순 다중 정렬 첫 샷', df2['샷'].iloc[0])

print(df['샷'].head().tolist())

print('실습 5')

F_SHOT = 'data/13_diecasting_shot.csv'

df = pd.read_csv(F_SHOT)

print(df.shape)

con = (df['품질등급'].isin(['주의', '불량']) & (df['비스킷두께'] >= 16))
df1 = df[con]
print('조건 통과', len(df1), '줄')

df2 = df1.sort_values('비스킷두께', ascending=False)
print('샷', df2['샷'].iloc[0])
print(df2['비스킷두께'].iloc[0])
print(df2['품질등급'].iloc[0])

miss = df[(df['품질등급'].isin(['주의', '불량']) & (df['비스킷두께'].isna()))]
print('미포함 결측 샷', len(miss), '줄')