# 가위바위보 게임 완성하기

print("가위 바위 보 게임입니다.")

first_player = input('''첫번째 플레이어 무엇을 낼 껀가요?!
1. 가위
2. 바위
3. 보
''')
# 정수 입력
first_player = int(first_player)

second_player = input('''두번째 플레이어 무엇을 낼 껀가요?!
1. 가위
2. 바위
3. 보
''')
# 정수 입력
second_player = int(second_player)

# first_player 입력 조건
if first_player == 1:
    first_player = "가위"
elif first_player == 2:
    first_player = "바위"
elif first_player == 3:
    first_player = "보"
else:
    first_player = "잘못된 입력"

# second_player 입력 조건
if second_player == 1:
    second_player = "가위"
elif second_player == 2:
    second_player = "바위"
elif second_player == 3:
    second_player = "보"
else:
    second_player = "잘못된 입력"

print("첫번째 플레이어는 {0}를(을) 내셨습니다.".format(first_player))
print("두번째 플레이어는 {0}를(을) 내셨습니다.)".format(second_player))

# 같은 것을 낼 경우(1번 조건)
if first_player == second_player:
    print("둘 다 {0}로 비겼습니다.".format(second_player))

# 두번째 플레이어 '가위' 일 때(2번 조건)
elif second_player == "가위":
    if first_player == "바위":
        print("첫번째 플레이어가 {0}로 승리!".format(first_player))
    elif second_player == "보":
        print("두번째 플레이어가 {0}로 승리!".format(second_player))

# 두번째 플레이어 '바위' 일 때(3번 조건)
elif second_player == "바위":
    if first_player == "보":
        print("첫번째 플레이어가 {0}로 승리!".format(first_player))
    elif first_player == "가위":
        print("두번째 플레이어가 {0}로 승리!".format(second_player))

# 두번재 플레이어 '보' 일 때(4번 조건)
elif second_player == "보":
    if first_player == "가위":
        print("첫번째 플레이어가 {0}로 승리!".format(first_player))
    elif second_player == "바위":
        print("두번재 플레이어가 {0}로 승리!".format(second_player))
else:
    print("잘못된 입력 입니다. 프로그램을 종료합니다.")
