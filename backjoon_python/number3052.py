remain = []
for _ in range(10):
    x = int(input())
    r = x % 42
    if r not in remain:
        remain.append(r)

print(len(remain))