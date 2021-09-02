print("시급계산기 프로그램입니다")

pay = input("시급을 입력해 주세요 : ")
time_of_day = input("일일근무시간 : ")
day_of_month = input("한달근무시간 : ")

pay = int(pay)
time_of_day = int(time_of_day)
day_of_month = int(day_of_month)

# 월급 계산
profit = pay * time_of_day * day_of_month

# 결과 출력
print("예상 월급은 : {0}원 입니다.\n\n".format(profit))
print("{0}원으로 무엇을 할 수 있을까요?\n\n".format(profit))
print("PC방 (1200원 기준) : {0}시간".format(profit//1200))
print("점심 (7000원) : {0}끼".format(profit//7000))
print("영화 (11000원) : {0}편".format(profit//11000))
print("노래방 (20000원) : {0}시간".format(profit//20000))

print('''
열심히  일하시는 당신에게...
비록 세상이 그대를 속일지라도
슬퍼하거나 노여워하지 말아라
슬픈 날은 참고 견디라
기쁜 날이 오고야 말리리...''')

# '//'는 정수 나눗셈을 의미합니다. '/'파이썬3에서는 실수 나눗셈을 적용합니다.
