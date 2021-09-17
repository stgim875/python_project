# 메뉴판 메뉴 반복 해결

import random

prices = [10000, 7000, 5000, 8000, 8000, 7000, 5000]

menus = list()
menus.append("갈비탕")
menus.append("떡볶이")
menus.append("오뎅")
menus.append("감자탕")
menus.append("김치찌개")
menus.append("제육볶음")
menus.append("김치볶음밥")

print("메뉴판")
print("====================================")
for index, value in enumerate(menus):
    print("{0:<10}{1:>10}{won},".format(value, prices[index], won='원'))
print("====================================")