# 함수 설계와 활용

# 기본값 인자: 인자 생략 시 기본값 사용
# 형식:
# def 함수(매개변수필수, 선택=기본값):

# 거의 항상 같은 값을 매번 적는 번거로움을 줄임, 필요할 때만 덮어쓴다
def report(name, value, unit='도'):
    print(f'{name}: {value}{unit}')

report('압축기1', 75.3)                 # 압축기1: 75.3도
report('펌프1', 7.2, 'bar')             # 펌프1: 7.2bar (덮어쓰기)

print('실습 1')
def check_temp(temp, limit=90):
    if temp <= limit:
        print(temp,'-> 정상')
    else:
        print(temp, '-> 경고')

check_temp(78)
check_temp(95)
check_temp(50, 40)

# 지역변수와 범위(스코프)
#  - 함수 안의 변수, 함수 바깥 변수를 읽을 수 있지만, 바깥에서는 함수 안 지역변수를 읽을수 없다
def clac():                 # 함수 선언
    result = 10 + 5         #지역변수
    return result           # 밖에서 사용하려면 return으로 내보내야된다

print(clac())

x = 10
def change():
    x = 20                  # 함수 내부의 지역변수

change()
print(x)                    # 10 (함수 바깥의 x값 변경 X)

print('실습 2')
def test():
    temp = 30
    print(temp)

test()

# print(temp)                 # NameError: name 'temp' is not defined

# 함수 조합 (함수 설계: 입력/처리/출력)
def get_avg(values):
    return sum(values) / len(values)

def judge(avg, limit=80):
    if avg > limit:
        return '위험'
    else:
        return '정상'

temps = [75, 88, 91]
avg = get_avg(temps)
print(round(avg, 1), judge(avg))    # 84.7 위험

print('실습 3')
def get_avg(values):
    return sum(values) / len(values)

def judge(avg, limit=85):
    if avg > limit:
        return '위험'
    else:
        return '정상'

temps = [80, 85, 90]
avg = get_avg(temps)
print(round(avg, 1), judge(avg))

print('실습 4')
def sensor_avg(sensors):
    return sum(sensors) / len(sensors)


def check_status(avg, limit=90):
    if avg <= limit:
        return '정상'
    else:
        return '경고'


result = sensor_avg([80, 90])
status = check_status(result)

print(result, status)