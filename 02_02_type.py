# 자료형

count = 3    # int 정수
temp = 25.5      # float 실수
name = '센서A'      # str 문자열

ok = True       # bool 불린형 - 참/거짓
no = False

#  type() -> 자료형을 알려줌
print(type(25))         # <class 'int'>
print(type('센서A'))    # <class 'str'>
print(type(ok))        # <class 'bool'>

# 자료형마다 다른 동작
print(3 + 5)            # 8 (숫자 더하기 = 계산)
print('3' + '5')        # 35 (글자 더하기 = 이어 붙이기)

print('실습1')
count = 10
print(count)
temp = 36.5
print(temp)
name = '설비'
print(name)
is_ok = True
print(is_ok)

print('실습2')
print(type(count))
print(type(temp))
print(type(name))
print(type(is_ok))

print('실습3')
100     #int
100.0   #float
'100'   #str
print(type(100))
print(type(100.0))
print(type('100'))

print('실습4')
a = 5
b = 3
print(a+b)      # 8
a = '5'     
b = '3'
print(a+b)      # 53
a = '53'
b = '47'
print(a+b)      # 5347
c = 53
d = 47
print(a+b)      # 5347
print(c+d)      # 100

print('실습5')
# 3이 2보다 큰지 확인
print(3 > 2)            # True
print(5 == 5)           # True
print(type(3 > 2))      # bool
print(type(5 == 5))     # bool

print('실습6')
num = 10
print(type(num))        # 10 int
num = 10.5
print(type(num))        # 10.5 float
num = '10'
print(type(num))        # 10 str

print('실습7')
device_temp = 62.5      # float
check_count = 4         # int
device_name = '모터'    # str
is_normal = True        # bool