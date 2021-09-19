# while
# while문(무엇무엇 하는 동안 반복적으로 실행한다.)

# while False:
#     print('Hello world')
# print('After while')

# 반복조건

# i = 0
# i = i + 1
# print(i)

# i = 0
# while True:
#     print('Hello world')
#     i = i + 1

# i = 0
# while i < 3:
#     print('Hello world')
#     i = i + 1

# 활용

# i = 0
# while i < 10:
#     print('print("Hello world '+str(i*9)+'")')
#     i = i + 1

# 조건문과 반복문의 합체
# 조건문을 이용하여 특정 숫자를 나오지 않게 하는 방법
# != !는 좌우 값이 다를 경우 참(True)
# 4가 출력되지 않게하는 방법
# i = 0
# while i < 10:
#     if i != 4: 
#         print(i)
#     i = i + 1

# i = 0
# while i < 10:
#     if i == 4:
#         print(i)
#     i = i + 1

# break문 사용법
# 10번 다 반복 안하고 중간에 종료 할 수 있다.
i = 0
while i < 10:
    if i == 4:
        break
        print(i)
    i = i + 1
print('after while')