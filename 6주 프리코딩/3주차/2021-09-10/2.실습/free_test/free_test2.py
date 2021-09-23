# 자율과제-2 가위바위보 게임 반복하기(2021-09-23)

# 가위바위보 게임 완성하기

import random

print("가위 바위 보 게임입니다.")

# play 가위바위보 선택

while True:
    player = input('''무엇을 낼 껀가요?!
1. 가위
2. 바위
3. 보
''')
    # 정수 입력
    player = int(player)

    # computer 가위바위보 선택(난수 발생)
    computer = random.randint(1, 3)
    computer = str(computer)

    # player 가위바위보 입력 조건
    if player == 1:
        player = "가위"
    elif player == 2:
        player = "바위"
    elif player == 3:
        player = "보"

    # computer 가위바위보 입력 조건
    # computer 난수 발생을 'str'으로 입력되게 해서 조건을 ""로 감싸 주어야 함
    if computer == "1":
        computer = "가위"
    elif computer == "2":
        computer = "바위"
    elif computer == "3":
        computer = "보"

    # 가위 바위 보 판별하기
    print("플레이어는 {0}를 내셨습니다.".format(player))
    print("컴퓨터는 {0}를 냈습니다.)".format(computer))

    # 같은 것을 낼 경우(1번 조건)
    if player == computer:
        print("둘 다 {0}로 비겼습니다.".format(player, computer))

    # 두번째 플레이어 '가위' 일 때(2번 조건)
    elif computer == "가위":
        if player == "바위":
            print("플레이어가 {0}로 승리!".format(player))
            break
        elif computer == "보":
            print("컴퓨터가 {0}로 승리!".format(computer))

    # 두번째 플레이어 '바위' 일 때(3번 조건)
    elif computer == "바위":
        if player == "보":
            print("플레이어가 {0}로 승리!".format(player))
            break
        elif computer == "가위":
            print("컴퓨터가 {0}로 승리!".format(computer))

    # 두번재 플레이어 '보' 일 때(4번 조건)
    elif computer == "보":
        if player == "가위":
            print("플레이어가 {0}로 승리!".format(player))
            break
        elif computer == "바위":
            print("컴퓨터가 {0}로 승리!".format(computer))
    else:
        print("잘못된 입력 입니다. 프로그램을 종료합니다.")
        break
