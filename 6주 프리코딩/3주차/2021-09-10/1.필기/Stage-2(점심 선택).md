#### Stage 1 - 점심으로 뭘 먹지?

파이썬에 내장되어 있는 random을 사용하여 점심을 추천해주는 추천기를 완성합니다.

#### 점심 추천기

직장인 여러분! 매일매일 최대의 난제죠. 아 오늘 점심 뭐 먹지... 이상하게도 우리 회사 주변에 혹은
동네에 음식점은 엄청나게 많은데 먹을 것이 없죠. 참 이상한 이상한 일이에요. 그래서 더 이상 고민을
그만하기 위해 랜덤으로 메뉴를 추천해주는 점심 추천기를 만들어봅시다. 여러분이 마음껏 응용해서 사용
할 수 있으니까. 여러분의 실생활에서 사용해보면 좋겠네요!

```
<요구사항>
print("점심 추천기 프로그램입니다!")
print('''
메뉴판
===================================
{0:<10}{1:>0}{won}
{2:<10}{3:>0}{won}
{4:<10}{5:>0}{won}
{6:<10}{7:>0}{won}
{8:<10}{9:>0}{won}
{10:<10}{11:>0}{won}
{12:<10}{13:>0}{won}
===================================
'''.format('갈비탕', 10000,
            '떡볶이', 7000,
            '오뎅', 5000,
            '감자탕', 8000,
            '김치찌개', 8000,
            '제육볶음', 7000,
            '김치볶음밥', 5000, won = "원"))

오늘의 메뉴 선택 : 김치찌개
메뉴의 가격 : 8000

### 내장함수와 외장함수

#### 함수란 무엇인가?

여러분이 이제껏 코딩을 하면서 사용했던 대부분의 것들이 함수입니다. 함수는 6주차 때 더 자세히 배웁니다.
지금 시간에는 '아 우리가 했던게 함수구나' 이 정도만 알아두시면 됩니다. 그래서 무엇이 함수냐?
`print문`, `input문`, `format문`, `len문` 등 단어 다음에 소괄호가 오는 것이 함수입니다.
우리가 사용했던 함수는 모두 내장 함수로서 파이썬을 만든 사람이 사용하기 편하도록 파이썬 내부에 심어놓은
코드들을 우리는 편하게 사용합니다.

# print("abcdefg")

함수명 + 소괄호

#### 내장 함수

아무런 설정이 필요없이 파이썬을 설치만 하면 기본적으로 사용할 수 있는 함수를 의미합니다.

#### 외장 함수

외장함수를 알기 위해서는 먼저 '라이브러리'를 알아야 합니다. 라이브러니는 도선관이라는
뜻이죠. 책 대신에 함수들이 모여있는 도서관입니다. 그래서 우리는 외장 함수를 사용하려면
먼저 라이브러리를 코드에 심어주여야 합니다. 그리고 라이브러리에서 우리가 사용자고자 하는 함수를 찾아서 사용하면 됩니다.

#### 파이썬 내장 함수 (ex. print(), input(), len() 등)

#### 파이썬 라이브러리 (ex. random, os, sys 등)

#### random 파헤치기

파이썬에 수많은 라이브러리가 있지만, 우리는 random 라이브러리를 가져와서 사용합니다.
왜냐하면, 점심 추천기를 만들 때 임의의 추천할 메뉴를 골라주기 위해서죠. random 말고도 수많은 라이브러리가 있으니,
여러분이 무엇인가 필요하시다면 구글링을 통해 라이브러리를 찾아 보시길 권합니다. 이번 시간을 통해 random을 예제로
라이브러리를 가져와 외장 함수를 사용하는 법을 배웁니다.

#### random 라이브러리 가져오기

아래와 같은 코드를 파이썬 파일 최상단에 선언함으로써 random 라이브러리를 가져올 수 있습니다.

example

import random

random 라이브러리가 지원하는 함수 예제입니다.

#### randrange(a, b)

example

import random
num = random.randrange(1, 10)
print(num)

#### randint(a, b)

example

import random
num = random.randlint(1, 10)

#### shuffle(list)

example

import random
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)

#### choice(list)

import random
my_list = [1, 2, 3, 4, 5]
result = random.choice(my_list)
print(result)

### 점심 추천기 만들기

#### random 사용하여 숫자 뽑아내기

#### random 라이브러리 추가하기

import random

#### 난수 발생

choice = random.randrange(0, len(menus))

#### 추천 결과 출력하기

print("오늘의 메뉴 선택 : {0}".format(menus[choice]))
print("메뉴의 가격 : {0}".format(price[choice]))
```
