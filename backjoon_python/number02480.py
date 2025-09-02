# 첫 번째 코드
a, b, c = map(int, input().strip().split())

if a == b == c:
    reward = 10000 + a * 1000
elif a == b or a == c:
    reward = 1000 + a * 100     # a == c, a == b 모두 같은 결과로 묶을 수 있음
elif b == c:
    reward = 1000 + b * 100
# elif a == c:
#     reward = 1000 + c * 100
else:
    # if a > b and a > c:
    #     reward = a * 100
    # elif b > a and b > c:
    #     reward = b * 100
    # else:
    #     reward = c * 100
    reward = max(a, b, c) * 100     # max 함수를 써서 a, b, c 중 가장 큰 수 구하기

print(reward)


# 두 번째 코드
from collections import Counter

a, b, c = map(int, input().split())
cnt = Counter([a, b, c])
# ex) Counter({3: 2, 6: 1})

if 3 in cnt.values():   # 모두 같음
    reward = 10000 + a * 1000
elif 2 in cnt.values(): # 두 개 같음
    # 값이 2인 경우가 있을 때 (k, v)쌍에서 v가 2인 k를 리스트에 넣고 첫 번째 원소 반환하여 same에 대입
    # 리스트 컴프리헨션 (List Comprehension)
    same = [k for k, v in cnt.items() if v == 2][0]
    reward = 1000 + same * 100
else:                   # 모두 다름
    # Counter에 들어있는 세 개의 키 중 값이 가장 큰 키 반환
    reward = max(cnt) * 100

print(reward)
