### Stage 4 - 주민번호 인적사항 판별하기

주민번호 앞 자리를 통해 생년월일을 알 수 있고, 뒷자리의 첫번째 자리로 성별을 판별할 수 있습니다.
사용자로부터 주민번호 정보를 입력 주민번호의 내용을 분석하여 조건문을 통해 정보를 뽑아내도록 하겠습니다.

#### 주민번호 분석기

주민번호 앞자리는 생년월일을 뒷자리에서 첫번째는 성별을 나타냅니다. 그런데 뒷자리가 가지는
또 다른 의미를 아시나요? 뒷자리의 나머지 자리는 여러분이 출생한 장소를 지역코드로 나타내는데요.
이번 Stage와 Challenge를 통해서 주민번호를 완전히 파헤쳐보도록 하겠습니다.

이번 시간에는 앞자리와 뒷자리의 첫번째를 가지고 정보를 파악해서 생년월일과 성별을 판별해내겠습니다.

<요구사항>

주민등록번호 분석기 프로그램입니다!
주민번호를 입력해주세요 :

생년월일 :
성별 : 남자

### 문자열 분석하기

#### 문자열은 어떻게 구성되는가?

주민등록을 사용자로부터 입력받으면 문자열 형태로 주민번호가 들어옵니다.
그러면 생년월일을 알기 위해선 앞의 6자리를 각각 2자리씩 끊어서 생각해야 합니다. 이를 위해서
우리는 문자열이 어떻게 구성되어 있는지 알아야 합니다. 그런데 전혀 어렵지 않습니다. 각각의 문자열에는 문자 하나하나마다
순서대로 숫자가 부여되어 있습니다. 우리는 그 문자가 문자열에서 몇번째 문자인지만 알면 우리가 원하는 문자를 가져올 수 있습니다.

|  0  | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 0   |
| :-: | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
|  I  |     | l   | o   | v   | e   |     | y   | o   | u   |

< 문자열 구성>

이렇게 각 문자마다 숫자가 부여된 것을 문자열 인덱싱이라고 합니다.

#### 문자열 인덱싱 알아보기

문자열 인덱싱에 대해 이해하셨으면, 이제는 파이썬에서 문자열 인덱싱을 사용해보도록 하겠습니다.
아래의 코드를 통해 이해해보도록 합시다.

#### example

a = "I love you"

print(a[0])
'I'가 출력

print(a[8])
'o'가 출력

print(a[-1])
'y'가 출력

print(a[10])
error 범위를 넘어감

print(a[-11])
error 범위를 넘어감

- `인덱싱은 대괄호([])안에 문자에 해당되는 숫자(인덱스)를 넣어주어 원하는 문자를 가져옵니다.
- 인덱싱은 음수로도 가능합니다. -1번째는 마지막 문자를 인덱싱합니다.
- 문자열의 범위를 넘어가면 안됩니다.

#### 문자열 슬라이싱 알아보기

인덱싱을 알아보았습니다. 하지만 인덱싱은 문자열 내에서 연속된 여러개의 문자를 가져오지 못합니다.
단 하나의 문자만 가져올 수 있지요. 그래서 `슬라이싱`이 있습니다. 말 그대로 문자열을 더
작은 조각으로 자르는 행위입니다. 어떻게 할 수 있는지 예문을 통해 살펴보겠습니다.

#### example

a = "I love you"

print(a[0:3])
'I l' 출력

print(a[7:-1])
'yo' 출력

print(a[3:])
'ove you' 출력

print(a[:4])
'I lo' 출력

### 주민번호로 인적사항 판별하기

#### 정보 뽑아내기

앞서 배운 문자열 슬라이싱을 사용하여 생년월일과 성별에 대한 정보를 가져옵니다.
