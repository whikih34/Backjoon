n = int(input())

x = []
y = []

for i in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

for i in range(n):
    print(f'Case #{i+1}: {x[i]} + {y[i]} = {x[i] + y[i]}')