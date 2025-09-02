# import sys

# # 한 줄 입력, 한 줄 출력 반복
# # Ctrl + D 입력 시 종료
# for line in sys.stdin:              # EOF가 오면 반복 종료
#     a, b = map(int, line.split())
#     print(a + b)


# 한 줄 입력, 한 줄 출력 반복
# 입력하지 않거나 Ctrl + D 입력 시 종료
import sys
input = sys.stdin.readline

while True:
    line = input()
    if not line:                    # EOF면 빈 문자열
        break
    a, b = map(int, line.split())
    print(a + b)
