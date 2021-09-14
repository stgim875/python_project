### Stage-3 로또 발생기 중복 제거

앞선 Challenge를 통하여 로또 발생기를 만들어 봤습니다. 하지만 중복된 숫자가 들어오는 문제가
있는데요. 이를 해결하기 위해서 중복이 됬을때 다시 번호를 부여 받을 수 있도록 하는 코드를 짜보겠습니다.
반복문을 이용합니다.

#### 중복 제거

<요구사항>
로또 번호 생성기 프로그램입니다!

랜덤 로또 발생기입니다. (중복이 가능합니다)

당첨 번호 :

2등 보너스 볼 :

#### 반복문의 이해

##### 반복문이란 무엇인가?

반복문은 특정한 조건이 만족할 때까지 똑같은 문장을 반복적으로 수행하는 것을 의미합니다.
컴퓨터와 우리와의 차이는 바로 이런점이 아닐까 생각됩니다. 계산이 엄청나게 빠르다는 것이죠.
다시 말해서, 반복적으로 무엇가를 계산하는 속도가 우리와는 비교도 안 될 만큼 빠릅니다.
지금부터 반복문을 제대로 살펴보겠습니다.

->>>
ㅣ ㅣ
<<--
특정조건 만족시

#### while문 이해하기

##### while문의 사용법

while 뒤에 2주차때 배웠전 조건문에 사용되는 조건 관련된 문장이 쓰여집니다. 예를 들어 a > 3, a == 1, True, False 등이 올 수 있게죠.
그 다음에 `:` 콜론을 찍고요. TAB으로 구분하여 반복할 문장을 작성합니다.

example

while 특정 조건:

    - 수행할 문장
    - 수행할 문장
    - 수행할 문장

#### continue와 break

#### continue

example
a = 0
while a != 10:
a = a + 1
print("aaaaaaaaaa")
continue
print("bbbbbbbbbb")
print("cccccccccc")

- "aaaaaaaaaa"만 10번 출력됩니다.
- continue가 있으면 다음 반복으로 계속되기 때문에, "bbbbbbbbbb"와 "cccccccccc"를 출력하는 문장은 수행되지 않습니다.

#### break

example

a = 0
while a != 10:
a = a + 1
print("aaaaaaaaaa")
break
print("bbbbbbbbbb")
print("cccccccccc")

- "aaaaaaaaaa"만 1번 출력됩니다.
- "aaaaaaaaaa"를 출력하고 `break`를 만나서 반복문이 멈추었기 때문입니다.

### 로또 번호 중복 제거하기

만약에 중복으로 2개의 숫자가 같이 나와서, 번호가 제거되면 한번 더 난수를 발생시키는 수행을 실행해주어야 합니다.
그래서 로또 번호를 가진 리스트의 길이가 7이 될 때까지 중복을 모두 피하는 리스트를 만들어내야 합니다.

#### while문 사용하기

life/lotto_numbers_creator.py

while len(lotto_numbers) != 7:
new_number = random.randrange(1, 46)
lotto_numbers.append(new_number)

- while문 안에서 난수를 발생합니다.
- 난수를 리스트에 추가합니다.
- 리스트의 길이가 7이 될때까지 반복합니다.

#### 중복 검사하기

새로운 숫자가 로또 번호 리스트 안에 있으면 로또 번호 리스트 안에 추가해서는 안됩니다.
이를 위해 검사하는 방법은 아래와 같습니다.

while len(lotto_numbers) != 7:
new_number = random.randrange(1, 46)
if new_number not in lotto_numbers:
lotto_number.append(new_number)

`!` if new_number not in lotto_numbers는 말 그대로 lotto_nunbers 리스트 안에
new_number가 없으면 아래의 문장을 실행하라는 것 입니다.
