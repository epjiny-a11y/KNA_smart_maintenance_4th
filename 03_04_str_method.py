# 메서드 - 점(.) 문법
# 형식: 문자열. 메서드이름() 주의) 꼭 괄호를 붙여야 실행
word = 'python'
# upper(): 모두 대문자 / lower(): 모두 소문자
print(word.upper())         # PYTHON
print(word.count('p'))      # 1
print(word)                 # python (원본 값 그대로)

print('NORMAL'.lower())         # normal
print('python is'.capitalize()) # Python is
print('hong gil'.title())       # Hong Gil

print('실습 1')
x = 'ready'
print(x.upper())                # READY

print('실습 2')
x = 'WARNING'
print(x.lower())                # warning

print('실습 3')
name = 'kim chul soo'
print(name.title())             # Kim Chul Soo

print('실습 4')
x = 'Fault'
y = 'FAULT'
print(x == y)                   # False
print(x.lower() == y.lower())   # True

# 확인 메서드: is*** 메서드는 참/거짓 변환
print('ABC'.isupper(), 'abc'.islower())   # True True

# 공백 정리 - strip
# 형식: .strip() = 앞뒤 공백 제거
raw = ' 정상 '
print('['+ raw + ']')           # [ 정상 ]
print('[' + raw.strip() + ']')  # [정상]

# .lstrip() -> 왼쪽 공백 제거 / .rstrip() -> 오른쪽 공백 제거
# 주의) strip은 '앞뒤' 공백만 제거, 가운데 공백 제거X
# strip() 으로 특정 문자 제거 -> strip('문자')
s = '###정상###'
print(s.strip('#'))             # 정상

print('실습 5')
print('ABC'.isupper(), '/', 'abc'.islower(), '/', 'Abc'.islower())      # True / True / False

print('실습 6')
x = 'Sensor_LOG.CSV'
x = 'Sensor_LOG.CSV'.lower()
print(x.startswith('sensor'), '/', x.endswith('.csv'))                  # True / True (통일 전에는 False)

print('실습 7')
x = ' 가동중 '
print('[' + x.strip() + ']')                                            # [가동중]

print('실습 8')
x = ' 대기 '
print('[' + x.lstrip() + ']', '/', '[' + x.rstrip() + ']')              # [대기 ] / [ 대기]

print('실습 9')
warning = '***경고***'
print(warning.strip('*'))                                               # 경고

# 체이닝 - 메서드 이어 붙이기
# 형식: 문자열.strip().lower() -> 왼쪽부터 차례로 적용
clean = ' NORMAL '.strip().lower()
print(clean)            # normal

print('실습 10')
word = ' WARNING '.strip().lower()
print(word)             # warning
x = ' 경보 '
print('[' + x + ']')    # [ 경보 ]
x = ' 경보 '.strip()
print('[' + x + ']')    # [경보]