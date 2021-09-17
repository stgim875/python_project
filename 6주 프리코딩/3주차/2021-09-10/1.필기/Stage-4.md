### Stage-4 출력을 보기 좋게

메뉴판에서는 메뉴들이 반복되어 출력되고, 로또 발생기에서는 로또 번호들이 반복되어 출력됩니다.
for문을 사용하여 반복되는 문장을 보기 좋게 바꿔봅니다.

#### 반복 코드 합치기

이젠 메뉴판 그리기와 로또 발생기에서 출력하는 부분의 코드를 보겠습니다. 보기 좋게 나열되어 있지만, 만약에
메뉴가 1,000,000개가 넘거나 로또 번호가 몇개인지 모른다면 저렇게 쓸 수 있을까요? 아마 힘드실 겁니다.
그걸 줄이기 위해서 이번에도 반복문을 사용해볼텐데요. 이번에는 while문이 아닌 for문을 사용해서 해결하겠습니다.

life/lunch_recommander.py

print('''
메뉴판
=============================
{0:<10}{1:>10}{won}
{2:<10}{3:>10}{won}
{4:<10}{5:>10}{won}
{6:<10}{7:>10}{won}
{8:<10}{9:>10}{won}
{10:<10}{11:>10}{won}
{12:<10}{13:>10}{won}
=============================
'''.format(menus[0], price[0],
menus[1], price[1],
menus[2], price[2],
menus[3], price[3],
menus[4], price[4],
menus[5], price[5],
menus[6], price[6], won = "원"
))

life/lotto_numbers_creator.py

print('''
2 랜덤 로또 발생기 입니다. (중복이 가능합니다)
3 당첨 번호 : {0}, {1}, {2}, {3}, {4}, {5}
4 2등 보너스 볼 : {6}
5 '''.format(lotto_numbers[0],
lotto_numbers[1],
lotto_numbers[2],
lotto_numbers[3],
lotto_numbers[4],
lotto_numbers[5],
lotto_numbers[6]))

#### for문이란?

#### for문이란 무엇인가?

앞서 반복문으로 while문에 대해 배웠지만, 사실 for문을 더 많이 사용합니다.
둘은 분명한 차이가 존재합니다. while문은 뒤에 조건이 왔다면, for문만의 반복에 대한 형식이 존재합니다.
아래와 같습니다.

example

for 변수 in 리스트(또는 튜플, 문자열):
수행할 문장
수행할 문장
수행할 문장

- 리스트나 튜플, 문자열의 길이만큼 반복됩니다.
- 반복이 되면서 요소 하나하나가 변수에 담겨집니다.
- for문 내에서 `for`와 `in` 사이의 수를 사용할 수 있습니다.

#### enumerate문의 사용

우리는 for문을 사용할 때 enumerate문을 함께 사용하면 더욱 편리하게 사용합니다.
`enumerate`는 `열거하다`라는 뜻입니다. enumerate문을 안에 `in` 뒤에 오는 리스트나 튜플, 문자열을
넣어주면, 그 안에 요소만 전달해주는 것이 아니라 그 요소에 해당되는 인덱스까지 전달해줍니다.
예를 통해 살펴보겠습니다.

example

my_list = ['a' , 'b', 'c', 'd', 'e']
for index, value in enumerate(my_list):
print("index : {0}, value : {1}".format(index, value))

<출력>
index : 0, value : a
index : 1, value : b
index : 2, value : c
index : 3, value : d
index : 4, value : e

### 메뉴 출력 바꾸어보기

#### 메뉴판 메뉴 반복 해결

print("메뉴판")
print("====================================")
for index, value in enumerate(menus):
print("{0:<10}{1:>10}{won},".format(value, prices[index], won='원'))
print("====================================")

#### 로또 번호 반복 해결
