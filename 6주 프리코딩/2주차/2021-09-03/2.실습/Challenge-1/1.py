# Challenge-1 비만도 측정하기

print("비만도계산기 프로그램입니다")

gender = input('''
성별이 어떻게 되십니까?
1. 남자
2. 여자
''')
gender = int(gender)

height = input("신장을 입력해주세요")
weight = input("체중을 입력해주세요")
age = input("나이를 입력해주세요")

height = int(height)
weight = int(weight)
age = int(age)

BMI = weight / (height * height / 10000)

if BMI < 18.5:
    BMI = "저체중"
elif BMI < 23:
    BMI = "정상"
elif BMI < 25:
    BMI = "과체중"
elif BMI < 30:
    BMI = "경도 비만"
elif BMI < 35:
    BMI = "중고도 비만"
else:
    print("고도 비만입니다.")

print("신장을 입력해주세요 : {0}cm".format(weight))
print("체중을 입력해주세요 : {0}kg".format(height))
print("나이를 입력해주세요 : {0}세".format(age))
print("당신의 BMI 수치는 {0}입니다".format(BMI))
