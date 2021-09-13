# # 교과목 학점 평가 시스템

print("교과목 학점 평가 시스템입니다.")

test_score = input("시험 점수를 입력해 주세요\n")
study_score = input("과제 점수를 입력해 주세요\n")

# # 시험점수와 과제점수 정수 입력
test_score = int(test_score)
study_score = int(study_score)

# 총 점수 계산 방법
score = test_score + study_score
score = int(score)

# 조건문s
if score >= 70:
    score = "A"
elif score >= 50:
    score = "B"
elif score >= 30:
    score = "C"
elif score < 30:
    score = "D"
elif score == 0:
    score = "F"
else:
    score = "잘못된 입력입니다."
print("당신의 점수는 {0}점".format(score))
