n, m = map(int, input().split())

basket = [(i+1) for i in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    basket[a-1], basket[b-1] = basket[b-1], basket[a-1]

# 리스트의 원소를 하나씩 풀어서 print의 인자로 넘긴 다음 공백을 두고 한 줄에 출력
# sep를 설정하지 않으면 기본은 공백
print(*basket)