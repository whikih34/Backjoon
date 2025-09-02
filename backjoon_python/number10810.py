n, m = map(int, input().split())

basket = [0] * n
for _ in range(m):
    i, j, k = map(int, input().split())

    # 바구니 번호는 1~n번 까지지만 리스트 번호는 0번 부터 n-1번 까지임
    for b in range(i-1, j):
        basket[b] = k

# # 리스트 언패킹
# print(*basket)  # 한 줄 공백 구분 출력

for b in basket:
    print(b, sep='')