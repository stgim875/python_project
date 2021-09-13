# Challenge-2 비만도 계산기 만들기

print("비만도계산기 프로그램입니다!")

gender = input('''성별이 어떻게 되십니까?
1. 여자
2. 남자
''')
# 성별 정수 입력하기
gender = int(gender)

height = input("신장을 입력해 주세요\n")
weight = input("체중을 입력해주세요\n")
age = input("나이를 입력해주세요\n")

height = int(height)
weight = int(weight)
age = int(age)

# BMI 계산
BMI = weight / (height * height / 10000)

print("신장을 입력해주세요: {0}cm".format(height))
print("체중을 입력해주세요: {0}kg".format(weight))
print("나이를 입력해주세요: {0}세".format(age))
print("당신의 BMI 수치는 {0}입니다".format(BMI))

print('''
괜찮아요...
눈에 보이는게
전부는 아니잖아요.
''')
