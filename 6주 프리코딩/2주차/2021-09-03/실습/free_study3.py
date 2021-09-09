# # 교과목 학점 평가 시스템

print("교과목 학점 평가 시스템입니다.")

test_score = input("시험 점수를 입력해 주세요")
study_score = input("과제 점수를 입력해 주세요")

# # 시험점수와 과제점수 정수 입력
test_score = int(test_score)
study_score = int(study_score)

if test_score >= 70:
    test_score = 0
elif test_score >= 50:
    test_score = 0
elif test_score >= 30:
    test_score = 0
elif test_score < 30:
    test_score = 0
else:
    test_score = "잘못된 입력"

if study_score >= 20:
    study_score = 0
elif study_score >= 15:
    study_score = 0
elif study_score >= 10:
    study_score = 0
elif study_score < 10:
    study_score = 0
else:
    study_score = "잘못된 입력"

print("당신의 점수는 {0}점 입니다.".format(test_score+study_score))
