# 2주차 급여에 수습 적용하기(1)

print("급여계산기 프로그램입니다.\n\n")

pay = input("시급을 입력해주세요\n\n")
time_of_day = input("일일근무시간\n\n")
day_of_month = input("한달근무시간\n\n")

pay = int(pay)
time_of_day = int(time_of_day)
day_of_month = int(day_of_month)

# 월급 계산
profit = pay * time_of_day * day_of_month

practice = input('''수습을 적용하나요?
1. 적용
2. 미적용
''')
practice = int(practice)

if practice == 1:
    practice_price = profit // 10
else:
    practice_price = 0
profit = profit - practice_price

print("{0}원으로 무엇을 할 수 있을까요".format(profit))
print("PC방 (1200원 기준 : {0}원".format(profit//1200))
print("점심 (7000원 기준 : {0}원".format(profit//7000))
print("영화 (11000원 기준 : {0}원".format(profit//11000))
print("노래방 (20000원 기준) : {0}원".format(profit//20000))

print('''
열심히 일하는 당신에게...
비록 세상이 그대를 속일지라도
슬퍼하거나 노여워하지 말아라
슬픈 날은 참고 견디라
기쁜 날이 오고야 말리니.
''')
