### Stage - 2 메뉴판 그려보기

- 파이썬으로 모니터에 문자를 출력하는 방법을 배워봅니다. - 먼저는 'Hello World!'를 출력해보고, 메뉴판까지 만들어 봅니다.

#### 메뉴판 그려보기

- 간단한 출력 연습을 해보고, 고급과정으로 메뉴판 그리기를 해봅니다. 이미 나는 좀 알아 하시는 분들은 당장 메뉴판을 그러보셔도 좋아요. 여러분이 가게를 차린다고 생각하시고 정성껏 메뉴판을 작성해보아요!

##### 점심 추천기 프로그램입니다!

##### 메뉴판

=================================
갈비탕 10,000원
떡복이 7,000원
오뎅 5,000원
감자탕 8,000원
김치찌개 8,000원
제육볶음 7,000원
김치볶음밥 5,000원
=================================

### Hello World! 출력하기

- Hello World!는 여러분이 모든 프로그래밍 언어를 배울 때 접하게 됩니다. 컴퓨터의 세상으로 온 여러분에게 컴퓨터가 인사를 하는 것이 아닐까 생각 되네요. 차근차근 따라하며 컴퓨터와 인사하는 시간을 가벼봐요!

#### print문 알아보기

- 'print'는 번역하면 '출력하다'라는 뜻이죠. 파이썬에서 print문을 사용하여 모니터에 우리가 원하는 문자들을 출력할 수 있습니다. 우리가 파이썬 파일에 print문을 쓰면 컴퓨터는 출력하라는 명령을 받아서 우리가 보는 모니터 화면에 print문 안의 내용을 보여주게 됩니다.

#### Hello World!

Stage 1에서 만든 main.py로 들어가보세요. main.py에 아래와 같은 코드를 작성해주세요.

main.py

print('Hello World')

#### 실행하기

main.py를 우클릭하고 Run 'main'을 클릭합니다.

### 파일 이름 출력하기

print문을 조금 더 연습해봅시다. 이번에는 각각의 파일에 들어가서 print문을 써본 뒤 각각의 파일
을 실행시켜보도록 합니다. 비만도 계산기 파일을 예시로 들어서 설명할테니 여러분은 나머지 5개
의 파일에서도 똑같이 해보세요.

#### 프로그램 설명문 작성하기

obesity_calculator.py를 열어 아래의 코드를 작성해주세요.

print("비만도 계산기 프로그램입니다.")

#### 실행하기

main.py를 실행했던 것 처럼, 이번에는 obesity_calculator.py에서 우클릭하여 Run
'obesity_calculator'를 클릭합니다.

### print문 응용

#### 이스케이프 코드 알아보기

이스케이프 코드란 출력할 때, 보기 좋게 하는 코드들을 문자 조합을 미리 지정해 둔 것입니다. 예
를 들어, 줄바꿈, 탭 띄우기, 따옴표 출력 등이 있습니다. 대표적으로 많이 사용되는 이스케이프 코
드에 대해 알아보겠습니다.

##### 줄바꿈 문자 -\n

example

print('enter\nokay enter!\nyes enter!')

##### 탭 띄우기 문자 -\t

example

print('\tthis\t is tab')

##### 역슬래쉬 문자 -\\

example

print('\\\\\\\\\\ this is back slash')

##### 따옴표 문자 -\'

example

print("\'\'\'\'\' single quote1")

##### 쌍따옴표 문자 -\"

example

print("\"\"\"\"\"\" double quote1")

##### 홑따옴표 안의 쌍따옴표

example

##### print("""""" double quote") # 에러발생 코드

example

print("'''' single quote2")

##### 쌍따옴표의 안의 홑따옴표

example

#### print(''''' single quote') # 에러 발생 코드

example

print('"""" double quote2')

#### 세 개의 따옴표

example

print('''
I love you
but miss you~ bye~!
''')

#### format문 알아보기

print("I love {0}, you love {1}.".format("apple", "me"))

#### 숫자넣기

example

print("I have {0} dollars.".format("10000"))

#### 이름으로 넣기

examle

print("you give me {gift}, he loves {gift}".format(gift="shoes"))

#### 10칸 차지하기

example

print("{0:10}aaa".format("hi"))

#### 왼쪽 정렬하기

example

print("{0:<10}aaa".format("hi"))

#### 가운데 정렬하기

example

print("{0:^10}aaa".format("hi"))

#### 오른쪽 정렬하기

#### example

print("{0:>10}aaa".format("hi"))

#### 공백 채우기

example

print("{0:!<100}aaa".format("hi"))

### 메뉴판 그리기

#### print문, format문에 대하여 학습하였습니다. 이제 여러분의 메뉴판을 작성해 봅시다. 제가 만든 메뉴판을 예시로 삼아 여러분의 메뉴판을 만들어 보세요.

life/lunch_recommander.py

1 print("점심 추천기 프로그램입니다!")
2
3 print('''
4 메뉴판
5 ======================
6 {0:<10}{1:>10}{won}
7 {2:<10}{3:>10}{won}
8 {4:<10}{5:>10}{won}
9 {6:<10}{7:>10}{won}
10 {8:<10}{9:>10}{won}
11 {10:<10}{11:>10}{won}
12 {12:<10}{13:>10}{won}
13 ======================
14 '''.format('갈비탕', 10000,
15 '떡볶이', 7000,
16 '오뎅', 5000,
17 '감자탕', 8000,
18 '김치찌개', 8000,
19 '제육볶음', 7000,
20 '김치볶음밥', 5000, won="원"))
