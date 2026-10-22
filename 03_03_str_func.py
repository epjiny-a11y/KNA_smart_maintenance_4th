# 문자열 연산과 검색
# - 문자열 연결(+), 반복(*)

# len() - 글자 수
# 형식 - len(문자열)
print(len('PYTHON'))        # 6
print(len('AI 분석'))       # 5 (공백도 글자 수에 포함)
print(len(''))              # 0 (빈 문자열)

# in / not in - 포함 / 불포함 여부 (결과 bool)
# 형식: '찾을 것' in 문자열
print('고장' in '설비 고장 발생')       # True
print('정상' not in '고장 발생')        # True

# count
# 형식: 문자열.count('x') -> 개수
print('banana'.count('a'))              # 3

# find
# 형식: 문자열.find('x') -> 처음 나오는 위치
print('banana'.find('a'))               # 1
print('banana'.find('t'))               # -1 (못 찾았다는 신호)

print('실습 1')
tel = '01012345678'
print(len(tel))                         # 11

print('실습 2')
massge = '설비 고장 발생'
print('고장' in massge)                 # True
print('정상' in massge)                 # False

print('실습 3')
sen = 'seonsor-01-temp'
print(sen.count('-'))                   # 2

print('실습 4')
temp = 'temp_2024'
print(temp.find('_'))                   # 4
print(temp.find('x'))                   # -1

# index
# 주의) 위치를 반환하지만 없으면 오류
email = 'hong@company.com'
at = email.index('@')
print(at)                               # 4
print(email[:at])                       # hong

# statswith / endswith
# 형식: 문자열.startswith('x') -> bool
print('EQP-001'.startswith('EQP'))      # True
print('campass.csv'.endswith('csv'))    # True

print('실습 5')
log = 'sensor_log.csv'
print(log.startswith('sensor'))         # True
print(log.endswith('.csv'))             # True

print('실습 6')
status = 'WARNING'
print(status == 'WARNING')              # True
print(status == 'warning')              # False