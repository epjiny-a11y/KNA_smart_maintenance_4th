# 각종 예외 상황
# temp = int('스물')          # ValueError: invalid literal for int() with base 2: '스물'
# result = 10 / 0                 # ZeroDivisionError: division by zero
# print(undefined_var)                # NameError: name 'undefined_var' is not defined

# try-except 구조
try:
    temp = int('스물') 
except ValueError:
    print('ValueError')

try:
    result = 10 / 0 
except ZeroDivisionError:
    print('ZeroDivisionError')

try:
    print(undefined_var)
except NameError:
    print('NameError')

print('실습 1')
# num = int('숫자')           # ValueError
# result = 100 / 0            # ZeroDivisionError
# print(undefined)            # NameError

print('실습 2')
# try:
    # temperature = int(input('온도를 입력하세요: '))
    # print('입력한 온도:', temperature)

# except ValueError:
    # print('숫자를 입력해주세요.')
# print('프로그램을 계속합니다.')

# 여러 except
row = 'P-01,102'.split(',')
try:
    code_no = int(row[3])
except ValueError:
    print('숫자 아님')
except IndexError:
    print('칸 부족')

print('실습 3')
try:
    num = int(input('측정값을 입력하세요: '))
    print('계산결과:', 100 / num)
except ValueError:
    print('숫자 아님')
except ZeroDivisionError:
    print('0으로 나눌 수 없음')