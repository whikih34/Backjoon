n = int(input())

total = []
for _ in range(n):
    a, b = map(int, input().split())
    total.append(a + b)

for i in range(len(total)):
    print(f'Case #{i+1}: {total[i]}')