# Challenge-2 일반 학점 계산기

print("학점계산기 프로그램입니다!")

number_of_subject = input("과목 갯수를 입력해주세요")
number_of_subject = int(number_of_subject)

# 학점 정보 리스트(과목명, 점수, 학점)
subject_name = list()
subject_score = list()
subject_grade = list()

# 
while len(subject_name) != number_of_subject:
    subject_name.append(input("과목명을 입력해주세요 :"))
    subject_score.append(input("당신의 점수를 입력해주세요 :"))
    subject_grade.append(input("취득한 학점을 입력해주세요 :"))

calculating_way = input('''
학점 계산 방식을 선택해주세요.
1. 4.5 만점
2. 4.3 만점
''')

score = 0
amount_of_grade = 0

for index, value enumerate()
