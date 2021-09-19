#### 컨테이너와 반복문

#### 달콤한 for문의 등장

- for라는 문법이 등장
- for ㅁㅁ in ㅁㅁ
- in 뒤에는 컨테이너(리스트)가 온다.
- 리스트에 값들을 반복문이 실행될 때마다, 이 리스트에 담겨져 있는 각각의 값들이 `for` 뒤로 들어오게 된다. 이것은 파이썬 `for문의 규칙이고 약속이다.`
- `for 이리고 적고` `in 뒤에` `처리하고자 하는 값이 담겨져 있는 컨테이터를 이 맥락에서는 리스트를 위치한다.` 그 리스트에 있는 값들을 반복문이 실행될 때마다, 꺼내는데 그 꺼낸 값을 in 앞에 있는 변수에다가 담도록, 담겨지도록 약속되어 있는 문법이 바로 for in문이다.

<while문>
members = ['gst', 'kst', 'gim', 'kim']
i = 0
while i < len(members):
    print(members[i])
    i = i + 1

<for in문>
members = ['gst', 'kst', 'gim', 'kim']
for member in members:
    print(member)

- while문 보다 for문을 사용하는 이유
1. while문은 사용할 코드가 많다.
2. for문은 코드가 간결하다.(부품이 적다.)

<for in문 사용 범위>
- in 뒤에 컨테이너를 사용할 경우 그릇인 경우에만 사용할 수 있다.
- 파이썬에서는 리스트를 사용할 경우 `for in`문을 사용한다.

<while문>
- 대부분의 개발언어가 while문을 지원함
- `i < len(members):` 의 값이 무엇이든간에 즉, True 또는 False 될 수 있는 있는 것들은 모두 사용할 수 있는 사용 범위가 훨씬 많은 문법적 요소이다.


#### for문의 활용

- 안전하고 간결하고 버그가 발생되지 않는 for in문을 사용했음
- for문의 용도는 컨테이너의 값을 하나하나 열거해서 처리할 때 사용
- 반복문의 본연의 역활은 반복적으로 무언가를 처리하는 것, 몇번 반복하느냐?

members = ['gst', 'kst', 'gim', 'kim']
for member in members:
    print(member)

- i라고하는 변수를 가르키는 배열에 담겨있는 값들을 각각 반복문이 반복될 때마다 item이라는 변수에 담아주도록 약속되어 있는 코드
i = [0,1,2,3,4]
for item in i:

i = [0,1,2,3,4]
for item in i:
    print('Hello')

- i 변수를 제거하고 in 뒤에 컨테이너를 입력해서 사용할 수 있다.
 for item in [0,1,2,3,4]:
    print('Hello')

- in 뒤에 range(5)라는 명령어로 동일한 값을 출력하는 코드를 만들 수 있다.
 for item in range(5):
    print('item')

for item in [5,6,7,8,9,10]:
    print('item')

for item in range(5, 11):
    print(item)
