import numpy as np

# 리스트 vs 배열
# 1) 리스트
# - 서로 다른 자료형도 같이 존재 가능
# - 계산이 느리고 반복문을 돌아야 한다

list = [70, 72, 71]
print(list * 2)                 # [72, 71, 70, 72, 71, 70]
print([v * 2 for v in list])    # [140, 144, 142]

# 2) 배열
# - 같은 자료형만 존재 가능
# - 계산이 빠르다

temp = np.array([70, 72, 71])
print(temp)                     # [70 72 71]
print(temp + 2)                 # [72 74 73] -> 반복문 없는 묶음 계산

# 튜플로 배열 만들기
print(np.array((1, 2, 3)))      # [1 2 3]

print('실습 1')

import numpy as np

celsius = np.array([20, 22, 24, 26, 28, 30])
fahrenheit = celsius * 1.8 + 32

print("섭씨 온도:", celsius)
print("화씨 온도:", fahrenheit)

# 배열 생성
# np.arange(시작, 끝, 간격) : 연속 정수
# - 끝값은 포함되지 않음
print(np.arange(5))             # [0 1 2 3 4]
print(np.arange(0, 10, 2))      # [0 2 4 6 8]

# np.linspace(시작, 끝, 개수) : 균등 분할
# - 끝값 포함
print(np.linspace(0, 1, 5))     # [0.   0.25 0.5  0.75 1.  ]
print(np.linspace(0, 10, 5))    # [ 0.   2.5  5.   7.5 10. ]    

print('실습 2')

print(np.linspace(0, 70, 8))

print('실습 3')

print(np.arange(0, 40, 5))

# 배열 속성
# - ndim, shape, size, dtype
# - 속성은 괄호 X

a = np.array([1,2,3])
b = np.array([[1,2,3], [4,5,6]])

print('dim:', a.ndim, b.ndim)       # dim: 1 2
print('shape:', a.shape, b.shape)   # shape: (3,) (2, 3)
print('size:', a.size, b.size)      # size: 3 6

print('실습 4')

import numpy as np

sensor = np.array([
    [20, 1.5],
    [22, 1.7],
    [24, 1.8],
    [26, 2.0]
])

print('센서 데이터:')
print(sensor)

print('차원:', sensor.ndim)
print('형태:', sensor.shape)
print('개수:', sensor.size)

print('행 x 열:', sensor.shape[0] * sensor.shape[1])

print('실습 5')

import numpy as np

currunt = np.array([18.69, 19.25, 20.78, 21.95])

print('전류 측정값:', currunt)
print('자료형:', currunt.dtype)

currunt_int = currunt.astype(int)

print('정수 변환:', currunt_int)

# reshape() 로 형태 바꾸기
# - -1 사용 시 자동 계산 (행 또는 열에 한번만 사용)
c = np.arange(12)
print(c.reshape(3, 4))
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# flatten() -> 1차원으로 만듦
b3 = np.array([[1, 2, 3], [4, 5, 6]])
print(b3.flatten())         # [1 2 3 4 5 6]

print('실습 6')

import numpy as np

time = np.array([10, 11, 12, 13, 14, 12, 15, 13, 14, 16, 15, 17])

print('원본 배열:', time)

table = time.reshape(3, 4)

print('변환된 배열:')
print(table)

print('배열 형태:', table.shape)
print('전체 개수:', table.size)

print('실습 7')

import numpy as np

sensor = np.array([20, 1.5, 1500, 22, 1.7, 1600, 24, 1.8, 1700, 26, 2.0, 1800])

table = sensor.reshape(4, 3)

print(table)
print(table.flatten())