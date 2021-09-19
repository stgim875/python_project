# Stage-3 로또 발생기 중복 제거

import random

print("로또 번호 생성기 프로그램입니다!")

# list()에 random.randrage()을 이용하여 랜덤 번호를 하나씩 추가
lotto_numbers = list()
lotto_numbers.append(random.randrange(1, 46))
lotto_numbers.append(random.randrange(1, 46))
lotto_numbers.append(random.randrange(1, 46))
lotto_numbers.append(random.randrange(1, 46))
lotto_numbers.append(random.randrange(1, 46))
lotto_numbers.append(random.randrange(1, 46))
lotto_numbers.append(random.randrange(1, 46))

# # while문 사용하기
# 로또 번호 중복 제거하기
while len(lotto_numbers) != 7:
    new_number = random.randrange(1, 46)
    lotto_numbers.append(new_number)

# 중복 검사하기
# 새로운 숫자가 로또 번호 리스트 안에 있으면 로또 번호 리스트 안에 추가해서는 안됨, 이를 위한 코드는 아래와 같다.
while len(lotto_numbers) != 7:
    new_number = random.randrange(1, 46)
    if new_number not in lotto_numbers:
        lotto_numbers.append(new_number)

print('''
랜덤 로또 발생기입니다.
당첨 번호 : {0}번, {1}번, {2}번, {3}번, {4}번, {5}번
2등 보너스 볼 : {6}번입니다.
'''.format(lotto_numbers[0],
           lotto_numbers[1],
           lotto_numbers[2],
           lotto_numbers[3],
           lotto_numbers[4],
           lotto_numbers[5],
           lotto_numbers[6]))
