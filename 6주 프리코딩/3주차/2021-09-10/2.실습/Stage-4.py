# my_list = ['a', 'b', 'c', 'd', 'e']
# for index, value in enumerate(my_list):
#     print("index : {0}, value : {1}".format(index, value))

import random

# 메뉴판 메뉴 반복 해결
# prices = [10000, 7000, 5000, 8000, 8000, 7000, 5000]

# menus = list()
# menus.append("갈비탕")
# menus.append("떡볶이")
# menus.append("오뎅")
# menus.append("감자탕")
# menus.append("김치찌개")
# menus.append("제육볶음")
# menus.append("김치볶음밥")

# print("메뉴판")
# print("====================================")
# for index, value in enumerate(menus):
#     print("{0:<10}{1:>10}{won},".format(value, prices[index], won='원'))
# print("====================================")

# 로또 번호 반복 해결
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
