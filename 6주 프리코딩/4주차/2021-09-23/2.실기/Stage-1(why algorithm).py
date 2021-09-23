# Stage-1 야구 게임

import random


# 컴퓨터 난수 발생
new_number = random.randint(0, 9)


# 사용자가 4자리 입력
number1 = input("첫번째 숫자를 입력하세요")
number2 = input("두번째 숫자를 입력하세요")
number3 = input("세번째 숫자를 입력하세요")
number4 = input("네번째 숫자를 입력하세요")

# 안내 문구
print("4 스트라이크?")
print("축하해요! 맞추셨어요!")
