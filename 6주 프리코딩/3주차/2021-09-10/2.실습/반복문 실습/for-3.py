# 컨테이너와 반복문
# for문의 활용

members = ['gst', 'kst', 'gim', 'kim']
for member in members:
    print(member)

i = [0,1,2,3,4]
for item in i:
    print('Hello')

# i 변수를 제거하고 in 뒤에 컨테이너를 입력해서 사용할 수 있다.
for item in [0,1,2,3,4]:
    print('Hello')

# in 뒤에 range(5)라는 명령어로 동일한 값을 출력하는 코드를 만들 수 있다.
for item in range(5):
    print('item')

for item in [5,6,7,8,9,10]:
    print('item')

for item in range(5, 11):
    print(item)