x = int(input().strip())
n = int(input().strip())

total = 0
for _ in range(n):
    a, b = map(int, input().strip().split())
    total += a * b

if sum == x:
    print('Yes')
else:
    print('No')