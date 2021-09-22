# 컨테이너와 반복문
# 컨테이너와 반복문의 만남

members = ['gst', 'kst', 'gim', 'kim']
i = 0
while i < 3:
    print(members[0])
    i = i + 1

members = ['gst', 'kst', 'gim', 'kim']
i = 0
while i < 4:
    print(members[i])
    i = i + 1


# 리스트에 값이 삭제되고 반복 값이 고정되어 있을 경우, 에러 발생됨
members = ['gst', 'kst']
i = 0
while i < 4:
    print(members[i])
    i = i + 1

# print(members[0])
# print(members[1])
# print(members[2])
# print(members[3])

# 리스트에 값이 추가 되거나, 삭제 될 경우, '4'라고 적혀 있는 변하지 않는 값을 리스트에 있는 값이 몇개냐에 따라서 달라지도록 가변적으로 바꿔주는 명령어가 바로 'len'임
members = ['gst', 'kst', 'gim', 'kim']
i = 0
while i < 4:
    print(members[i])
    i = i + 1

# 4를 len으로 변경함
members = ['gst', 'kst', 'gim', 'kim']
i = 0
while i < len(members):
    print(members[i])
    i = i + 1