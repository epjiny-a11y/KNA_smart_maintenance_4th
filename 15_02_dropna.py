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

versions = {'원본': df, '행제거': df.dropna(), 'thresh20': df.dropna(thresh=20)}
comparison_rows = []

for name, frame in versions.items():
    comparison_rows.append({
        '방식': name, '행수': len(frame),
        '손실률_%': (1 - len(frame) / len(df)) * 100,
        '불량수': int(frame['불량여부'].sum()),
        '불량비율_%': frame['불량여부'].mean() * 100
    })

comparison = pd.DataFrame(comparison_rows)
print(comparison.round(1).to_string(index=False))

print('실습 5')

s = df['최대사출압']
mask = s.isna()
print('원래 결측:', mask.sum(), '개')

mean = s.mean()
median = s.median()

df_mean = df.copy()
df_mean['최대사출압'] = df_mean['최대사출압'].fillna(mean)

df_median = df.copy()
df_median['최대사출압'] = df_median['최대사출압'].fillna(median)

print('평균 대체 후 결측:', df_mean['최대사출압'].isna().sum(), '개')
print('중앙값 대체 후 결측:', df_median['최대사출압'].isna().sum(), '개')

print('평균 대체값:', round(mean, 2))
print('중앙값 대체값:', round(median, 2))

print('원래 결측 위치 앞 3개:')
print(df.loc[mask, ['최대사출압']].head(3))

print('평균 대체 결과:')
print(df_mean.loc[mask, ['최대사출압']].head(3))

print('중앙값 대체 결과:')
print(df_median.loc[mask, ['최대사출압']].head(3))

print('관측값 유지:',
      df.loc[~mask, '최대사출압'].equals(
          df_mean.loc[~mask, '최대사출압']
      ) and
      df.loc[~mask, '최대사출압'].equals(
          df_median.loc[~mask, '최대사출압']
      ))

# ffill, bfill

series_demo = pd.Series([None, 73.0, None, None, 75.0])

# ffill = 앞에서 마지막으로 확인한 값으로 채움
print(series_demo.ffill().tolist())             # [nan, 73.0, 73.0, 73.0, 75.0]
# - limit: 연속 결측 구간에서 최대 몇칸을 채울지
# - bfill: 뒤에서 처음 확인되는 값으로 채움
print(series_demo.bfill().tolist())             # [73.0, 73.0, 75.0, 75.0, 75.0]

print('실습 6')

NA_RULES = {'배럴온도': [999], '사출압력': [0], '스크루속도': [-999]}
log = pd.read_csv(F_LOG, na_values=NA_RULES, parse_dates=['측정시각'])        # 측정시각을 날짜, 시간으로 읽도록 지정
log['측정시각'] = pd.to_datetime(log['측정시각'], errors='raise')             # 날짜, 시간 변환 명시적 확인
unknown = log.loc[log['사출기'].isna()].copy()        
known = log.loc[log['사출기'].notna()].copy()

known = known.sort_values(['사출기', '측정시각'])
print(len(known), len(unknown))                 # 15 1
print(int(log.isna().sum().sum()))

# 앞의 값
candidate = (known.groupby('사출기')['배럴온도'].ffill(limit=1))

# 온도가 실제로 있었던 시각만 표시
observed_at = known['측정시각'].where(known['배럴온도'].notna())
print(observed_at)

# 마지막으로 온도가 있었던 시각
last_time = observed_at.groupby(known['사출기']).ffill()

# 현재 기록의 시각 - 마지막으로 온도를 측정한 실제 시각
gap = known['측정시각'] - last_time
print(known['측정시각'], last_time)

can_fill = (known['배럴온도'].isna() & candidate.notna()
            & gap.le(pd.Timedelta('2min')))

# gap.le(pd.Timedelta('2min')))
# - .le: 이하인지 비교
# - pd.Timedelta('2min'): 2분

# 허용 위치에 온도 넣기
known.loc[can_fill, '배럴온도'] = candidate.loc[can_fill]
print(int(can_fill.sum()))

print('실습 1')

import pandas as pd

df = pd.read_csv('data/16_diecasting.csv')

print(df.head())

print('데이터 크기', df.shape)

print('컬럼 이름', df.columns.tolist())

print('데이터 정보')
df.info()

print('실습 2')

mini = df['실린더압력'].min()

maxi = df['실린더압력'].max()

range_value = maxi - mini

print('실린더압력 최소', mini)
print('실린더압력 최대', maxi)
print('실린더압력 범위', range_value)

print('실습 3')

sorted_df = df.sort_values('사이클타임', ascending=False)

print('상위 사이클타임')
print(sorted_df['사이클타임'].head(10).to_string(index=False))

candidate = sorted_df[sorted_df['사이클타임'] > 40]

print('설비 점검 후보')
print(candidate['사이클타임'].to_string(index=False))

normal = df[df['사이클타임'].between(20, 35)]

abnormal = df[
    (df['사이클타임'] < 20) |
    (df['사이클타임'] > 35)
]

print('정상 범위: 20~35초')
print('정상:', len(normal), '개')
print('정상 범위 밖:', len(abnormal), '개')

print('실습 4')

avg = df['사이클타임'].mean()
med = df['사이클타임'].median()

print('전체 평균:', round(avg, 2))
print('전체 중앙값:', round(med, 2))

normal = df[df['상태'] == 0]
normal_avg = normal['사이클타임'].mean()

print('정상만 평균:', round(normal_avg, 2))

print('전체 평균과 중앙값 차이:', round(abs(avg - med), 2))
print('정상 평균과 중앙값 차이:', round(abs(normal_avg - med), 2))

print('실습 5')

print('실린더 압력:')
q1 = df['실린더압력'].quantile(0.25)
print('Q1', q1)

q2 = df['실린더압력'].quantile(0.50)
med = df['실린더압력'].median()

print('Q2', q2)
print('중앙값', med)
print('Q2와 중앙값 일치:', q2 == med)

q3 = df['실린더압력'].quantile(0.75)

print('Q3:', q3)
print('가운데 절반 범위:', q1, '~', q3)

print('실습 6')

cols = ['실린더압력', '주조압력', '사이클타임', '비스킷두께', '형체력']

summary = df[cols].describe()
print(summary)

mean = summary.loc['mean']
median = summary.loc['50%']

gap = (mean - median).abs()

print('평균과 중앙값 차이')
print(gap)

result = gap.sort_values(ascending=False)

print('차이가 큰 컬럼 순서')
print(result)

print('이상치 의심 컬럼:', result.head(3).index.tolist())

print('실습 7')

# 1단계. 세 컬럼의 사분위수를 한 번에 구하기
cols = ['실린더압력', '사이클타임', '비스킷두께']

q = df[cols].quantile([0.25, 0.75])

print('사분위수:')
print(q)

# 2단계. 가운데 절반 폭(Q3-Q1) 계산
width = q.loc[0.75] - q.loc[0.25]

print('가운데 절반 폭:')
print(width)

# 3단계. 폭이 좁은 컬럼과 넓은 컬럼 구분
result = width.sort_values()

print('폭이 좁은 순서:')
print(result)

print('폭이 가장 좁은 컬럼:', result.index[0])
print('폭이 가장 넓은 컬럼:', result.index[-1])

print('실습 7')

cols = ['실린더압력', '사이클타임', '비스킷두께']

q = df[cols].quantile([0.25, 0.75])

width = q.loc[0.75] - q.loc[0.25]

print('가운데 절반 폭')
print('실린더압력:', round(width['실린더압력'], 2))
print('사이클타임:', round(width['사이클타임'], 2))
print('비스킷두께:', round(width['비스킷두께'], 2))

result = width.sort_values()

print('폭이 좁은 순서:', result.index.tolist())
print('폭이 가장 좁은 컬럼:', result.index[0])
print('폭이 가장 넓은 컬럼:', result.index[-1])