### 반복문이 없다면

print("Hello world 0")
print("Hello world 9")
print("Hello world 18")
print("Hello world 27")
print("Hello world 36")
print("Hello world 45")
print("Hello world 54")
print("Hello world 63")
print("Hello world 72")
print("Hello world 81")

### while

#### while문 (while : 무엇무엇 하는 동안에 반복적으로 실행한다.)

while문 뒤에는 if문처럼 블리언이 온다.(True, False)
while문에 `Flase`일 경우 `print('After while')` 코드가 실행이되고 `True` 일 경우 `print('Hello world')` 코드가 실행이 됨

while False:
    print('Hello world')
print('After while')

#### 반복조건

반복문은 무한이 반복되거나? 아니면 반복되지 않거나? 둘중의 하나의 상태
대부분의 중요한 것은 언제까지 반복할 것이냐? 몇번을 반복 할 것이냐?

반복문이 실행 될 때 마다 몇번을 반복하는지? 알아야 봐야 함

<반복을 알 수 있는 코드>
# i = 0
# i = i + 1
# print(i)

- 아래 코드는 1씩 증가하는 코드이자만 무한히 반복되는 코드임
i = 0
while True:
    print('Hello world')
    i = i + 1

- 아래 코드는 3번 반복되는 코드임
i = 0
while i < 3:
    print('Hello world')
    i = i + 1

### 활용

- 아래 코드는 9씩 10번 반복된느 코드임(생활코딩에서 문자와 숫자가 더해지지 않는다는 점 다시 복습하기)
i = 0
while i < 10:
    print('print("Hello world '+str(i*9)+'")')
    i = i + 1

- 아래 코드는 4만 출력되게 하는 코드임
i = 0
while i < 10:
    if i == 4:
        print(i)
    i = i + 1


# break문 사용법(continue는 따로 스터디 해볼것)
# 10번 다 반복 안하고 중간에 종료 할 수 있다.

i = 0
while i < 10:
    if i == 4:
        break
        print(i)
    i = i + 1
print('after while')