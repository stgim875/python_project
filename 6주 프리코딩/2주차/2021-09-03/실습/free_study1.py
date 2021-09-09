# 일반 계산기 - 모범 답안 내용으로 구현

# <요구사항 2>
first = input("계산할 첫번째 값을 입력하세요 :\n")
second = input("계산할 두번째 값을 입력하세요 :\n")
# 정수 입력
first = int(first)
second = int(second)

# <요구사항 1>
way = input('''
원하는 연산을 선택하세요.
1. 더하기
2. 뻬기
3. 곱하기
4. 정수나누기
5. 실수나누기
6. 나머지 구하기
''')
# 정수 입력
way = int(way)

# <요구사항 2>
print("두개의 값 : {0}와 {1} ".format(first, second))
if way == 1:
    print("더하기 값 (a + b) : {0} ".format(first + second))
elif way == 2:
    print("빼기 값 (a - b) : {0} ".format(first - second))
elif way == 3:
    print("곱하기 값 (a * b) : {0} ".format(first * second))
elif way == 4:
    print("정수나누기 값 : {0} ".format(first // second))
elif way == 5:
    print("실수나누기 값 : {0} ".foramat(first / second))
elif way == 6:
    print("나머지 구하기 값 : {0} ".format(first % second))
else:
    print("잘못된 연산 방법입니다. 프로그램을 종료합니다.")
