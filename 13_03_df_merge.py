import pandas as pd

F_SHOT = 'data/13_diecasting_shot.csv'
F_MASTER = 'data/13_diecasting_master.csv'

log = pd.read_csv(F_SHOT)
master = pd.read_csv(F_MASTER)

print(log.shape)
print(master.shape)

three = log.head(3)[['샷', '설비ID', '비스킷두께']]
print(three.to_string(index=False))

print(three.merge(master, on='설비ID').to_string(index=False))
# 샷     설비ID  비스킷두께 라인  도입연도  정격형체력 담당반
#  1    DIE-A-01   10.0     A      2018     280     1반
#  2    DIE-B-01   11.0     B      2020     320     2반
#  3    DIE-B-01   11.0     B      2020     320     2반

# merge 기본 사용법
# - on: 두 표를 잇는 키 열
# - 행은 예측불가, 열 수는 예측 가능

# - how: 어느쪽을 다 남길 것인가
# - (기본) how= 'inner'
# - how='left' : 왼쪽은 다 남기고 짝 없으면 빈 칸
# - how='outer' : 양쪽 다 남김

m_inner = log.merge(master, on='설비ID')
m_left = log.merge(master, on='설비ID', how='left')
m_outer = log.merge(master, on='설비ID', how='outer')

print(m_inner.shape, m_left.shape, m_outer.shape)           # (185, 12) (200, 12) (201, 12)

print('실습 1')

import pandas as pd

F_SHOT = 'data/13_diecasting_shot.csv'
F_MASTER = 'data/13_diecasting_master.csv'

log = pd.read_csv(F_SHOT)
master = pd.read_csv(F_MASTER)

print('로그', log.shape)
print('대장', master.shape)

m_inner = log.merge(master, on='설비ID')
print('합친 표', m_inner.shape)

print(three.merge(master, on='설비ID').to_string(index=False))

# 합치기 전후 점검 코드

print(len(log))                                     # 200
print(len(master), master['설비ID'].nunique())      # 5 5

m_left = log.merge(master, on='설비ID', how='left')
print(len(m_left))                                  # 200
print(int(m_left['라인'].isna().sum()))             # 15

unmatched = m_left[m_left['라인'].isna()]
print(unmatched['설비ID'].head(1).tolist(), len(unmatched))     # ['DIE-C-01'] 15

print('실습 2')

m_inner = log.merge(master, on='설비ID')
print('inner', m_inner.shape)

m_left = log.merge(master, on='설비ID', how='left')
print('left', m_left.shape)

m_outer = log.merge(master, on='설비ID', how='outer')
print('outer', m_outer.shape)

unmatched = m_left[m_left['라인'].isna()]
print('미매칭', unmatched['설비ID'].head(1).tolist(), len(unmatched), '행')

no_log = m_outer[m_outer['샷'].isna()]
print(no_log['설비ID'].tolist(), len(no_log), '행')

# merge는 옆으로 칸을 붙이고, concat은 아래로 줄을 쌓는다
# concat은 키 열이 필요 없고, 칸 이름만 맞으면 된다

# pd.concat

# ex) 설비 로그를 1차, 2차로 나눠 받은 경우
part1 = log.iloc[:100].reset_index(drop=True)
part2 = log.iloc[100:].reset_index(drop=True)
print(part1.shape, part2.shape)         # (100, 8) (100, 8)

stacked = pd.concat([part1, part2])
print(stacked.shape)                    # (200, 8)
print(stacked.index[-3:].tolist())      # [97, 98, 99]
print(len(stacked.loc[[0]]))            # 2

# - 번호를 다시 매기기 -> ignore_index
renumbered = pd.concat([part1, part2], ignore_index=True)
print(int(renumbered.index[-1]))        # 199

# - 칸이(열이) 다른 표를 붙이면 -> 빈 칸
# 붙이기 전에 두 표의 columns 비교
# -> set(표1.columns) - set(표2.columns)

print('실습 3')

F_SHOT = 'data/13_diecasting_shot.csv'

log = pd.read_csv(F_SHOT)

part1 = log.iloc[:100].reset_index(drop=True)
part2 = log.iloc[100:].reset_index(drop=True)
stacked = pd.concat([part1, part2])

print(stacked.shape)  
print(len(stacked.loc[[0]]))

renumbered = pd.concat([part1, part2], ignore_index=True)
print(int(renumbered.index[-1]))

print('실습 4')

joined = log.merge(master, on='설비ID', how='left')
with_line = joined[joined['라인'].notna()]
print('라인이 붙은 줄', len(with_line))

not_ok = with_line[with_line['품질등급'] != '양품']
print('양품 아닌 줄', len(not_ok))

result = not_ok.sort_values('비스킷두께', ascending=False)
print(result[['샷', '설비ID', '라인', '비스킷두께', '품질등급']].head(5).to_string(index=False))