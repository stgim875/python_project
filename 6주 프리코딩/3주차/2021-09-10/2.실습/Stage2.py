import random
# num = random.randrange(1, 10)
# print(num)
# # 1 <= num < 10 범위에서 난수를 생성


# num = random.randint(1, 10)
# print(num)
# # 1 <= num < 10 범위에서 난수를 생성

# my_list = [1, 2, 3, 4, 5]
# random.shuffle(my_list)
# print(my_list)
# # [4, 5, 3, 1, 2] 등 리스트를 마구 섞음

# my_list = [1, 2, 3, 4, 5]
# result = random.choice(my_list)
# print(result)
# # my_list의 요소들 중 하난를 무작위로 선택


print("점심 추천기 프로그램입니다!")
print('''
메뉴판
===================================
{0:<10}{1:>0}{won}
{2:<10}{3:>0}{won}
{4:<10}{5:>0}{won}
{6:<10}{7:>0}{won}
{8:<10}{9:>0}{won}
{10:<10}{11:>0}{won}
{12:<10}{13:>0}{won}
===================================
'''.format('갈비탕', 10000,
           '떡볶이', 7000,
           '오뎅', 5000,
           '감자탕', 8000,
           '김치찌개', 8000,
           '제육볶음', 7000,
           '김치볶음밥', 5000, won="원"))


choice = random.randrange(0, len(menus))
print("오늘의 메뉴 선택: {0}".format(menus[choice]))
print("메뉴의 가격: {0}."format(price[choice]))
