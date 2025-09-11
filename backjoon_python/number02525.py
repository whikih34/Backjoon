a, b = map(int, input().split())
c = int(input())

hour = (a + ((b + c) // 60)) % 24   # 0~23시 까지만 존재하므로 24의 나머지로 계산
min = (b + c) % 60

print(hour, min)