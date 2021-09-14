import random
num = random.randrange(1, 10)
print(num)
# 1 <= num < 10 범위에서 난수를 생성


num = random.randint(1, 10)
print(num)
# 1 <= num < 10 범위에서 난수를 생성

my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)
# [4, 5, 3, 1, 2] 등 리스트를 마구 섞음

my_list = [1, 2, 3, 4, 5]
result = random.choice(my_list)
print(result)
# my_list의 요소들 중 하나를 무작위로 선택

choice = random.randrange(0, len(menus))
print("오늘의 메뉴 선택: {0}".format(menus[choice]))
print("메뉴의 가격: {0}.".format(prices[choice]))
