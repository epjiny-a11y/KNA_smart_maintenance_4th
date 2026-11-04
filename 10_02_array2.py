import numpy as np

# 인덱싱, 슬라이싱
a = np.array([0,1,2,3,4])
print(a[0], a[-1])          # 0 4
print(a[1:4])               # [1 2 3]
print(a[::2])               # [0 2 4]

print('실습 1')

import numpy as np

rpm = np.array([4603, 4500, 4700, 4800, 4900,
                5000, 5100, 5200, 5300, 4603])

print('맨 앞', rpm[0])
print('맨 뒤', rpm[-1])

print(rpm[1:4])

print(rpm[::2])

print('실습 2')

import numpy as np

sensor = np.array([
    [4603, 120],
    [4700, 125],
    [4800, 130],
    [4900, 135]
])

print(sensor[2])

print(sensor[:, 0])

print(sensor[:, 1])