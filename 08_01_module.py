# 모듈 / 패키지 / 라이브러리
# - 모듈: 기능을 모아둔 .py 파일 하나
# - 패키지: 모듈을 모아둔 폴더
# - 라이브러리: 위에 사항들을 통칭

# import 방식
# 형식: import 모듈 / from 모듈 import 기능 / import 모듈명 as 별칭
import math                     # math 라는 모듈을 통째로 불러옴
print(math.sqrt(16))            # 4.0
from math import sqrt, ceil     # 일부만 불러옴 -> 모듈명 없이 바로 사용
print(sqrt(16), ceil(4.2))      # 4.0, 5
import math as m
print(m.sqrt(16))               # 4.0

print('실습 1')

import math
print(math.sqrt(16), math.ceil(4.5))

from math import sqrt, floor
print(sqrt(16), ceil(4.5))

import math as m
print(m.sqrt(16), m.ceil(4.5))

# 표준 라이브러리 - math / random / datetime
# 파이썬 설치 시 함께 깔리는 검증된 모듈들
import random
import datetime

print(random.randint(1, 100))
print(datetime.datetime.now())

print('실습 2')

import random
import math

sensor = random.randint(10, 100)

print('센서값:', sensor)
print('센서값 제곱근:', math.sqrt(sensor))

# ////////////////
# 경로와 os 모듈
# - 파일을 다루려면 어디에 있는지 경로를 알아야 한다
# 1) 절대경로                                       # C:\Users\MSI\Desktop\4th
#  - 최상위부터 전체 주소
# 2) 상대경로
#  - 지금 실행중인 위치를 기준으로 한 주소

import os
print('현재 실행 위치(절대경로)', os.getcwd())

# 폴더 유무 확인
print(os.path.exists('data'))                       # True

# 폴더 목록 확인
files = os.listdir('data')
print(files)

# 폴더명 + 파일명 -> 경로
path = os.path.join('data', '08_press_13_261029_3.csv')

if os.path.exists(path):
    print('파일경로:', path)

print('실습 3')

import os
print(os.getcwd())
files = os.listdir('data')

print('파일 목록:')
for file in files:
    if file.endswith('.csv'):
        print(file)

print('실습 4')

import os
file_path = os.path.join('data', '08_press_13_261029_3.csv')
result = os.path.exists(file_path)

print('파일 경로:', file_path)
print(result)

if result:
    print('파일 있음')
else:
    print('파일 없음')

print('실습 5')

import os
import datetime

file_list = os.listdir('data')
file_count = len(file_list)
check_time = datetime.datetime.now()

print(f'파일 {len(files)}개, 점검시각 {check_time}')

print('실습 6')

import os
file_list = os.listdir('data')
csv_list = []

for file in file_list:
    if file.endswith('.csv'):
        csv_list.append(file)

print('[CSV]')
for file in csv_list:
    file_path = os.path.join('data', file)
    print(file_path)