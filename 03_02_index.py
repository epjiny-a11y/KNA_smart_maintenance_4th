# 인덱싱 - 위치 번호로 글자 하나 꺼내기
# 형식: 문자열[번호]    (첫 글자 = 0번)

word = 'PYTHON'
print(word[0], word[2], word[5])        # P T N
# 음수 인덱스: 뒤에서부터 -1, -2, ...
print(word[-1], word[-2])               # N O

# print(word[6])          # IndexError: string index out of range

print('실습 1')
word = 'SIGNAL'
print(word[0], word[2], word[5])        # S G L

print('실습 2')
print(word[-1], word[-2])               # L A

# 슬라이싱 - 구간으로 잘라내기
# 형식: 문자열[시작:끝] (시작 포함, 끝 제외)
print(word[1:4])                        # I G N
# 생략 가능
# - 시작 생략 = 처음부터 (0번부터)
#  - 끝 생략 = 끝까지
# - 둘 다 생략 = 전체
print(word[:3])                         # SIG
print(word[3:])                         # NAL
print(word[:])                          # SIGNAL
# 음수
print(word[-3:])                        # NAL
print(word[:-1])                        # SIGNA

print('실습 3')
print(word[:3])                         # SIG
print(word[2:5])                        # GNA

print('실습 4')
word = 'temp_sensor'
print(word[:4])                         # temp

print('실습 5')
print(word[5:])                         # sensor

print('실습 6')
word = 'sensor_01'
print(word[-2:])                        # 01

# step 간격 주기
# 형식: 문자열[시작:끝:간격]
print(word[::2])                        # sno_1
print(word[1::3])                       # eo0

print('실습 7')
word = 'SIGNAL'
print(word[::2])                        # SGA

print('실습 8')
print(word[::-1])                       # LANGIS