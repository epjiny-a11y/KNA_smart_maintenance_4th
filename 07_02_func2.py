# 매개변수와 반환값

# 매개변수와 인자
# 형식:
# def 함수이름(매개변수):
#   ....
# 호출
# 함수이름(인자)

def check(name):                        # name = 매개변수
    print(name + '점검을 시작합니다.')

check('압축기 1')                       # '압축기 1' = 인자
check('펌프 1') 
# check()                              # TypeError: check() missing 1 required positional argument: 'name'
# check('A', 'B')                      # TypeError: check() takes 1 positional argument but 2 were given

print('실습 2')
def status(name, temp):
    print(name, str(temp) + '도')

status('모터', 78)
status('펌프', 92)

# 키워드 인자
def report(name, temp):
    print(name, temp)
    
    info('모터', temp=78)
    info(temp=92, name='펌프')
    

print('실습 3')
def info(name, temp):
    print(name, temp)

info('모터', temp=78)
info(temp=92, name='펌프')

# return
#  - print: 사람이 확인할 수 있게 출력 / return: 값을 프로그램에게 돌려줘서 이어 쓸 수 있게 한다
def add(a, b):
    return a+b
    print('실행 안됨')                  # return을 만나면 즉시 함수 종료 -> 그 아래 코드는 실행 x 

total = add(3, 4)
print(total)

print('실습 4')
def cal(a, b):
    return (a + b) / 2

result = cal(80, 90)
print(result)

result2 = result + 5
print(result2)

# 여러 값 반환 / 언패킹
#  - 쉼표로 여러 값을 retuen 하면 튜플로 묶여서 돌아옴 -> 언패킹 가능
def min_max(values):
    return  min(values), max(values)

print(min_max([75, 10, 100]))           # (10, 100)
low, high = min_max([75, 10, 100])
print(low, high)                        # 10 100

none = report('펌프', 10)
print(none)                             # None

print('실습 5')
def sensor_status(sensors):
    min_value = min(sensors)
    max_value = max(sensors)
    avg_value = sum(sensors) / len(sensors)

    return min_value, max_value, avg_value

min_temp, max_temp, avg_temp = sensor_status([78, 92])
print(min_temp, max_temp, avg_temp)