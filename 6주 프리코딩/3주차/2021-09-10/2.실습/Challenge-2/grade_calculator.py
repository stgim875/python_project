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

for index, value in enumerate(subject_score):
    grade = int(subject_grade[index])
    amount_of_grade += grade

# 4.5만점 기준
if calculating_way == '1':
    if value == 'A+':
        score += 4.5 * grade
    elif value == 'A':
        score += 4.0 * grade
    elif value == 'A-':
        amount_of_grade -= grade
    elif value == 'B+':
        score += 3.5 * grade
    elif value == 'B':
        score += 3.0 * grade
    elif value == 'B-':
        amount_of_grade -= grade
    elif value == 'C+':
        score += 2.5 * grade
    elif value == 'C':
        score += 2.0 * grade
    elif value == 'C-':
        amount_of_grade -= grade
    elif value == 'F':
        score += 0
    else:
        amount_of_grade -= grade

# 4.3만점 기준
elif calculating_way == '2':
    if value == 'A+':
        score += 4.3 * grade
    elif value == 'A':
        score += 4.0 * grade
    elif value == 'A-':
        score += 3.7 * grade
    elif value == 'B+':
        score += 3.3 * grade
    elif value == 'B':
        score += 3.0 * grade
    elif value == 'B-':
        score += 2.7 * grade
    elif value == 'C+':
        score += 2.3 * grade
    elif value == 'C':
        score += 2.0 * grade
    elif value == 'C-':
        score += 1.7 * grade
    elif value == 'F':
        score += 0
    else:
        amount_of_grade -= grade
else:
    print("잘못된 연산 방법입니다. 프로그램을 종료합니다.")
    break # 코드 실행시 위치가 여기가 아니라고 출력됨.

print('''
당신이 이번학기 들었던 총 학점 : {0}
당신의 GPA : {1}
'''.format(amount_of_grade, score/amount_of_grade))
