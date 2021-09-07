a = "I love you"

print(a[0])
# 'I'가 출력

print(a[8])
# 'o'가 출력
#
print(a[-1])
# 'u'가 출력
# 인덱싱은 음수도 가능 -1은 마지막 문자를 인덱싱

# print(a[10])
# # error 범위를 넘어감
#
# print(a[-11])
# # error 범위를 넘어감

print(a[0:3])
# 'I l' 출력
print(a[7:-1])
# 'yo' 출력

print(a[3:])
# 'ove you' 출력

print(a[:4])
# 'I lo' 출력
