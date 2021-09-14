# Challenge-1 비만도 측정하기

print("비만도계산기 프로그램입니다")

# 정보 입력
gender = input('''
성별이 어떻게 되십니까?
1. 남자
2. 여자
''')
gender = int(gender)

# 정보 입력
height = input("신장을 입력해주세요")
weight = input("체중을 입력해주세요")
age = input("나이를 입력해주세요")

# 숫자로 변환
height = int(height)
weight = int(weight)
age = int(age)

# BMI 계산
BMI = weight / (height * height / 10000)

# 결과 조건 1 : (내가 직접 만든 코드)
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
    print("고도 비만")

# 결과 출력
print("신장을 입력해주세요 : {0}cm".format(weight))
print("체중을 입력해주세요 : {0}kg".format(height))
print("나이를 입력해주세요 : {0}세".format(age))
print("당신의 BMI 수치는 {0}입니다".format(BMI))

print('''
괜찮아요...
눈에 보이는게 
전부는 아니잖아요.
''')


# # 결과 조건 2: (모범 답안 코드)
# if BMI < 18.5:
#     BMI = "저체중"
#     # print("저체중 입니다. 살 좀 찌셔야겠어요.")
# elif BMI < 23:
#     BMI = "정상"
#     # print("정상이십니다.")
# elif BMI < 25:
#     BMI = "과체중"
#     # print("과체중이십니다. 살을 조그만 빼시면 좋겠어요.")
# elif BMI < 30:
#     BMI = "경도 비만"
#     # print("비만이세요. 꼭 살을 빼세요!")
# elif BMI < 35:
#     BMI = "중고도 비만"
#     # print("중등도 비만이십니다. 2단계 비만입니다. 약간 위험해요!")
# else:
#     # print("고도 비만이십니다. 건강이 위험해요! 꼭 살을 뻬세요!")
# print('''
# 괜찮아요...
# 눈에 보이는게
# 전부는 아니잖아요.
# ''')
