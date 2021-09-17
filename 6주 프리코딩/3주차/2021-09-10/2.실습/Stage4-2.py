# 로또 번호 반복 해결
import random

print("로또 번호 생성기 프로그램입니다!")
print("당첨 번호 : ", end="")

# list()에 random.randrage()을 이용하여 랜덤 번호를 하나씩 추가
lotto_numbers = list()
lotto_numbers.append(random.randrange(1, 46))
lotto_numbers.append(random.randrange(1, 46))
lotto_numbers.append(random.randrange(1, 46))
lotto_numbers.append(random.randrange(1, 46))
lotto_numbers.append(random.randrange(1, 46))
lotto_numbers.append(random.randrange(1, 46))
lotto_numbers.append(random.randrange(1, 46))

# 로또 번호 반복 해결
for index, value in enumerate(lotto_numbers):
    if index == len(lotto_numbers)-1:
        print("\n2등 보너스볼 : {0}번".format(value))
    else:
        print(value, end='')

# index가 마지막 인덱스(len(lotto_numbers)-1)이면 2등 보너스볼에 대한 내용을 출력합니다.
# print문 뒤에 end="" 를 넣어주면 기본적으로 print문이 개행되는 것을 방지하고 원하는 끝 문자를 설정할 수 있습니다.