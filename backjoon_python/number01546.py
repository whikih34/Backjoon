n = int(input())
# 공백으로 나눈 값을 리스트에 넣기
scores = list(map(int, input().split()))

# 리스트의 최대 값
m = max(scores)

# 제너레이터 표현식
print(sum(s / m * 100 for s in scores) / n)