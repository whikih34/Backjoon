a = int(input().strip())

answer = []
for _ in range(a):
    x, y = map(int, input().strip().split())
    answer.append(x + y)

for i in answer:
    print(i)