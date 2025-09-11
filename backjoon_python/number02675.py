t = int(input())

for _ in range(t):
    r, s = input().split()
    code = ''
    for i in s:
        code += int(r) * i
    print(code)