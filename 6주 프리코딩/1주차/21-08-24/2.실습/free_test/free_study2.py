print("일반 계산기 프로그램입니다!\n\n")

frist = input("계산할 첫번째 값을 입력해 주세요.\n\n")
second = input("계산할 두번째 값을 입력해 주세요.\n\n")

# 정수 입력
frist = int(frist)
second = int(second)

print("\n\n두개의 값 : {0}와 {1} 입니다.\n".format(frist, second))
print("더하기 값 (a + b) : {0}".format(frist + second))
print("빼기 값 (a - b) : {0}".format(frist - second))
print("곱하기 값 (a * b) : {0}".format(frist * second))
print("정수 나누기 값 (a // b): {0}".format(frist // second))
print("실수 나누기 값 (a / b) : {0}".format(frist / second))
print("나머지 값 (a % b) : {0}".format(frist % second))
