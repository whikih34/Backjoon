n, m = map(int, input().split())

basket = [(i+1) for i in range(n)]
for _ in range(m):
    i, j = map(int, input().split())
    # reversed는 단순히 역순으로 뒤집기만 하는 함수
    basket[i-1:j] = reversed(basket[i-1:j])

print(*basket)