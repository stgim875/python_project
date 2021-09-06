# 2주차 수습에 세금 적용하기(2)

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

# 수습 기간 변수 추가
practice = int(practice)

# 수습 기간 적용한 급여 계산
if practice == 1:
    practice_price = profit // 10
else:
    practice_price = 0
profit = profit - practice_price

# 세금 적용 여부
tax = input('''세금을 적용하나요?
1. 미적용
2. 4대 보험만 적용(8.41%)
3. 소득세 공제만 적용(3.3%)
4. 모두 적용
''')

# 세금 변수 추가
tax = int(tax)

# 세금 적용하기

if tax == 2:
    tax_price = profit * 8.41 // 10000
elif tax == 3:
    tax_price = profit * 3.3 // 1000
elif tax == 4:
    tax_price = profit * 841 // +  3.3 // 1000
else:
    tax_price = 0
profit = profit - tax_price

##########################################################
# 화면 출력
print("{0}원으로 무엇을 할 수 있을까요?".format(profit))
print("PC방 (1200원 기준) : {0}원".format(profit//1200))
print("점심 (7000원 기준) : {0}원".format(profit//7000))
print("영화 (11000원 기준) : {0}원".format(profit//11000))
print("노래방 (20000원 기준) : {0}원".format(profit//20000))

print('''
열심히 일하는 당신에게...
비록 세상이 그대를 속일지라도
슬퍼하거나 노여워하지 말아라
슬픈 날은 참고 견디라
기쁜 날이 오고야 말리니.
''')
