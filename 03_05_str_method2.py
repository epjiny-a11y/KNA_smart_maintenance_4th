# replace - 바꾸기 / 지우기
# 형식: 문자열.replace('바꿀것', '새것')
# - 모두 바꾸기, 결과 저장 필요

print('정 상 가 동'.replace(' ',''))           # 정상가동
print('010-1234-5678'.replace('-',''))         # 01012345678  
print('3,000'.replace(',',''))                 # 3000

# split - 구분자로 나누기 (결과 -> 리스트)
# 형식: 문자열.split('구분자') (구분자 생략 = 공백 기준)
print('A1 A2 A3'.split())                         # ['A1', 'A2', 'A3']
print('사과,배,감'.split(','))                     # ['사과', '배', '감]

print('실습 1')
text = '설비 정상 가동'
print(text.replace('정상','점검'))              # 설비 점검 가동

print('실습 2')
text = 'PUMP A 03'
print(text.split())                             # ['PUMP', 'A', '03']

print('실습 3')
text = 'a,b,c,d'
print(text.split(','))                          # ['a', 'b', 'c', 'd']

print('실습 4')
print(text.split(',',1))                        # ['a', 'b,c,d']

# join - 합치기 (리스트 -> 문자열)
# 형식: '구분자'.join(리스트) (구분자가 앞에 옴)

# split + join 
# - split: 문자열 -> 리스트
# - join: 리스트 -> 문자열
raw = '사과, 배, 감'
p = raw.split(',')
print(p)                                                        # ['사과', '배', '감']
print('/'.join(p))                                              # 사과/ 배/ 감
print('/'.join([p[0].strip(), p[1].strip(), p[2].strip()]))     # 사과/배/감

print('실습 5')
print('-'.join(['2025','01','15']))         # 2025-01-15

print('실습 6')
print(2025, 1, 15, sep='-')                 # 2025-1-15
print(2025, 1, 15, sep=', ')                # 2025, 1, 15

print('실습 7')
date = '2025/01/15'
d = date.split('/')
print('-'.join(d))                          # 2025-01-15

print('실습 8')
raw = '1,NORMAL,25.3'
print(raw.split(',')[1].strip().lower())    # normal