# try-except-else-finally
# - else: 예외가 하나도 안 났을 때만 실행
# - finally: 성공/실패 상관없이 무조건 마지막 실행

text = '62.5'
try:
    temp = float(text)
except ValueError:
    print('변환 실패')
else:
    print('변환 성공:', temp)
finally:
    print('종료')

print('실습 1')

try:
    f = open('data/09_ict_inspection.csv', 'r', encoding='utf-8')
    first = f.readline()
    print(first.strip())        #헤더
except FileNotFoundError:
    print('파일이 존재하지 않습니다')
finally:
    f.close()
print('파일이 안전하게 닫힘')

print('실습 2')

import csv
total = 0

try:
    with open('data/09_ict_inspection_dirty.csv', 'r', encoding='utf8', newline='') as f:
        reader = csv.reader(f)
        next(reader)  

        for row in reader:
            try:
                score = float(row[1])
                total += score

            except ValueError:
                print('숫자 변환 실패:', row)
                continue

except FileNotFoundError:
    print('파일을 찾을 수 없습니다.')
else:
    print('점수 합계:', total)
finally:
    print('프로그램 종료')

print('실습 3')

try:
    with open('data/09_ict_inspection_dirty.csv', encoding='utf-8') as f:
        rows = f.readlines()[1:]                # 슬라이싱 (헤더 빼려고)
except FileNotFoundError:
    rows = []

total = 0.0
skipped = 0
for line in rows:
    try:
        total += float(line.split((',')[2]))      # 측정값(2열)
    except (ValueError, IndexError):
        skipped += 1
        continue

print('합계:', round(total, 1), '/건너뜀:', skipped)

print('실습 4')
names = [
    "data/09_ict_inspection.csv",
    "data/09_없는파일.csv",
    "data/09_ict_inspection_dirty.csv",
]

done = 0
for name in names:
    try:
        with open(name, 'r', encoding='utf8') as f:
            lines = f.readlines()

        print(name, '행 수:', len(lines))
        done += 1

    except FileNotFoundError:
        print('파일을 찾을 수 없습니다:', name)
        continue

print('처리한 파일:', done)

print('실습 5')

def check_value(text, lo = 0.0, hi = 5000.0):
    v = float(text)

    if not (lo <= v <= hi):
        raise ValueError(f'범위를 벗어난 값: {v}')
    return v

for t in ['128.5', '결측', '-999']:
    try:
        print('통과:', check_value(t))
    except ValueError as e:
        print('제외:', e)