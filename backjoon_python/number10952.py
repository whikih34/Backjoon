total = []

while True:
    a, b = map(int, input().split())

    if a == 0 and b == 0:
        break
    else:
        total.append(a+b)

for t in total:
    print(t)