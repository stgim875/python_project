# 주민등록번호 분석기 프로그램

print("주민등록번호 분석기 프로그램입니다.")

resident_number = input("주민번호를 입력해 주세요 :\n")

# 주민번호 정보 분류
birth_year = resident_number[0:2]
birth_month = resident_number[2:4]
birth_day = resident_number[4:6]
sex = resident_number[6]
local_code = resident_number[7:9]

# 생년월일 및 성별 정수 입력
birth_year = int(birth_year)
birth_month = int(birth_month)
birth_day = int(birth_day)
local_code = int(local_code)

# 성별 조건식
if sex == '1' or sex == '3':
    sex = '남자'
elif sex == '2' or sex == '4':
    sex = '여자'
else:
    sex = '중성'

# 지역 코드 조건식
if 0 <= local_code <= 8:
    local_code = '서울특별시'
elif 9 <= local_code <= 12:
    local_code = '부산광역시'
elif 13 <= local_code <= 15:
    local_code = '인천광역시'
elif 16 <= local_code <= 25:
    local_code = '경기도'
elif 26 <= local_code <= 34:
    local_code = '강원도'
elif 35 <= local_code <= 39:
    local_code = '충청북도'
elif local_code == 40:
    local_code = '대전광역시'
elif 41 <= local_code <= 43 or 45 <= local_code <= 47:
    local_code = '충청남도'
elif local_code == 44 or local_code == 96:
    local_code = '세종특별시'
elif 48 <= local_code <= 54:
    local_code = '전라북도'
elif 55 <= local_code <= 66:
    local_code = '전라남도'
elif local_code == 55 or local_code == 56:
    local_code = '광주광역시'
elif 67 <= local_code <= 70:
    local_code = '대구광역시'
elif 71 <= local_code <= 81:
    local_code = '경상북도'
elif 82 <= local_code <= 84 or 86 <= local_code <= 90:
    local_code = '경상남도'
elif local_code == 85:
    local_code = '울산광역시'
else:
    local_code = '제주특별자치도'

# 주민번호로부터 정보 출력
print("생년월일 : {0}년 {1}월 {2}일".format(birth_year, birth_month, birth_day))
print("성별 : {0}".format(sex))
print("출생지역 : {0}입니다".format(local_code))
