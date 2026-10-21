# 문자열
# - "", '' 감싸서 표현

# 여러줄 문자열
# 형식: 삼중 따옴표 """ 적을내용.. """
notice = """
설비 점검 안내
1. 전원 확인
2. 센서 점검
"""
# print(notice)

# 이스케이프: \n 줄바꿈, \t 탭
# print('이름\t상태')
# print('첫줄\n둘째 줄')

print('실습 1')
print('''가동 점검표 /
1. 온도 확인 /
2. 압력 확인''')
print('가동 점검표 / \n1. 온도 확인 / \n2. 압력 확인')

print('실습 2')
code = 'PUMP_A'
status = '정상'
date = '2025-01-15'
print(code + ' / ' + status + ' / ' + date)

print('실습 3')
operating_time = 72
check_date = '2025 - 01 -18'
print('설비: ' + code + '\n상태: ' + status + '\n가동시간: ' + str(operating_time) + '시간\n점검일: ' + check_date ) 