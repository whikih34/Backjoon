a, b = map(int, input().strip().split())

if b >= 45:
    print(a, b - 45)
else:
    b = 60 - (45 - b)
    if a == 0:
        a = 24
    print(a - 1, b)