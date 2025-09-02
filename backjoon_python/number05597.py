assign = []
for _ in range(28):
    assign.append(int(input()))

assign.sort()

for i in range(1, 31):
    if i not in assign:
        print(i)