# 일반 계산기 - 내가 짜집기해서 구현

# <요구사항 2>
a = input("계산할 첫번째 값을 입력해 주세요 :\n")
b = input("계산할 두번째 값을 입력해 주세요 : \n")
# 정수 입력
a = int(a)
b = int(b)

# <요구사항 1>
calculation = input('''
원하는 연산을 선택하세요.
1. 더하기
2. 빼기
3. 곱하기
4. 정수 나누기
5. 실수 나누기
6. 나머지 구하기
''')
# 정수 입력
calculation = int(calculation)

# <요구사항 2>
print("두개의 값은 {0} 와 {1}".format(a, b))
if calculation == 1:
    plus = (a + b)
    print("더하기 값 : {0}" .format(plus))
elif calculation == 2:
    subtract = (a - b)
    print("뻬기 값 : {0}" .format(subtract))
elif calculation == 3:
    multiply = (a * b)
    print("곱하기 값 : {0}" .format(multiply))
elif calculation == 4:
    integer_division = (a // b)
    print("정수나누기 값 : {0}" .format(integer_division))
elif calculation == 5:
    division_of_mistakes = (a / b)
    print("실수나누기 값 : {0}" .format(division_of_mistakes))
elif calculation == 6:
    get_the_rest = (a % b)
    print("나머지 값 : {0}" .format(get_the_rest))
else:
    print("잘못된 연산 방법입니다. 프로그램을 종료합니다.")
