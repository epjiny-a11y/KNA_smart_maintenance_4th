# 입력 (input)
# 주의) 사용자 입력은 항상 "문자열"
# 형식: 변수 = input('안내문구: ')
# name = input('이름: ')
# age = input('나이: ')
# print(name)

# 형변환 - int(), float(), str()
# print(age + 1)    반례 
# print(int(age) + 1)

# 실습 - 숫자 입력받아 계산하기
# birth = int(input('출생년도: '))      
# year = 2026
# age = year - birth
# print(birth)        
# print(age)      # 나이 : 29세       # int() 형변환 후 연산
height = float('173.5')              # float() 실수 변환
# print(height, type(height))
# print('나이:' + str(30))

# 실습 - 여러 개의 값 입력받기
# country = input('거주 국가: ')
# city = input('거주 도시: ')
# print(country,'의', city,'에서 거주하시는군요!')

# 실습 - 두 수 입력받아 사칙연산
# a = int(input('첫 번째 숫자: '))        # 12
# b = int(input('두 번째 숫자: '))        # 3
# print('덧셈:', a + b)                   # 15
# print('뺄셈:', a - b)                   # 9
# print('곱셈:', a * b)                   # 36
# print('나눗셈:', a / b)                 # 4.0

# 실습 - 입력값 비교해 출력하기
# temp = int(input('온도를 입력하세요: '))     #기준 온도: 50
# print('기준 온도 이상인가요?:', temp >= 50)

# 실습 - 종합 처리 프로그램
x = int(input('score1: '))      # 10
y = int(input('score2: '))      # 8
z = int(input('score3: '))      # 6
average = (x + y + z) / 3       # 8
print('10 이상?', average >= 10) # False    
