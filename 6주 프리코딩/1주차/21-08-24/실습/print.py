# print문 응용

# 줄바꿈 문자  -\n
# example
print('enter\nokay enter!\nyes enter!')

# 탭 띄우기 문자 -\t
# example
print('\tthis\t is tab')


# 역슬래쉬 문자 -\\
# example
print('\\\\\\\\\\ this is back slash')

# 따옴표 문자 -\'
# example
print("\'\'\'\'\' single quote1")


# 쌍따옴표 문자 -\"
# example
print("\"\"\"\"\"\" double quote1")

# 홑따옴표 안의 쌍따옴표
# example
# print("""""" double quote") # 에러발생 코드

# example
print("'''' single quote2")

# 쌍따옴표의 안의 홑따옴표
# example
# print(''''' single quote') # 에러 발생 코드

# example
print('"""" double quote2')

# 세 개의 따옴표
# example
print('''
I love you
but miss you~ bye~!
''')

# format문 알아보기
print("I love {0}, you love {1}.".format("apple", "me"))

# 숫자넣기
# example
print("I have {0} dollars.".format("10000"))

# 이름으로 넣기
# examle
print("you give me {gift}, he loves {gift}".format(gift="shoes"))

# 10칸 차지하기
# example
print("{0:10}aaa".format("hi"))

# 왼쪽 정렬하기
# example
print("{0:<10}aaa".format("hi"))

# 가운데 정렬하기
# example
print("{0:^10}aaa".format("hi"))

# 오른쪽 정렬하기
# example
print("{0:>10}aaa".format("hi"))

# 공백 채우기
# example
print("{0:!<100}aaa".format("hi"))
