# Stage-2 야구 게임

import random

print("야구 게임 프로그램입니다!")

# 랜덤하게 4자리의 숫자 만들기(각 자리의 수는 중복 불가)
answer = list()

# 번호 중복을 피하고 중복 검사하기
# 리스트에 값이 추가 되거나, 삭제 될 경우, 'len(answer)'라고 적혀 있는 값을 리스트에 있는 값이 몇개냐에 따라서 달라지도록 가변적으로 바꿔주는 명령어가 바로 'len'임
while len(answer) != 4:
    new_number = random.randint(0, 9)
    if new_number not in answer:
        answer.append(new_number)

# print(answer)

strike = 0
count = 0  # 카운트 변수 추가(결과 출력하기)

# 반복 조건 정하기
while strike != 4:
    # 사용자에게 입력 받음
    your_answer = input("답을 맞혀보세요 : ")

    count += 1  # 카운트 변수 1씩 증가(결과 출력하기)
    strike = 0
    ball = 0

    # 스트라이크, 볼 검사
    for index, value in enumerate(your_answer):
        # print("index : {0}, value : {1}".format(index, value))

        # 값 비교하기
        if int(value) == answer[index]:
            strike += 1
        elif int(value) in answer:
            ball += 1

    # 조건에 따라 출력하기
    if strike == 0 and ball == 0:
        print("Out!!!!!!!!!!")
    else:
        print("{0} 스트라이크 {1} 볼입니다".format(strike, ball))
