# Stage-2 야구 게임

import random

print("야구 게임 프로그램입니다!")

# 컴퓨터 난수 발생
new_number = random.randint(0, 9)
print(new_number)

# 랜덤하게 4자리의 숫자 만들기(각 자리의 수는 중복 불가)
answer = list()

# 번호 중복 제거 및 검사하기
while len(answer) != 4:
    new_number = random.randint(0, 9)
    if new_number not in answer:
        answer.append(new_number)
print(answer)

# 사용자에게 입력 받음
your_answer = input("답을 맞혀보세요 : ")

# 스트라이크, 볼 검사
for index, value in enumerate(your_answer):
    print("index : {0}, value : {1}".format(index, value))