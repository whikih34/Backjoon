import sys
# sys.stdin.readline -> 표준 입력에서 한 줄을 그대로 읽어오는 함수
# input 이라는 이름에 바인딩해서, input() 함수를 빠른 버전으로 쓰게 만듦
# input() 보다 sys.stdin.readline이 훨씬 빠름
# input() -> 끝의 /n을 제거하고 문자열만 돌려줌
# sys.stdin.readline 개행 \n 을 포함해서 돌려줌 (마지막 줄 제외 가능)
# input()은 입력받는 것 외에 부가적인 기능을 더 수행하기 때문에 느림
input = sys.stdin.readline  # 빠른 입력

t = int(input())
out = []
for _ in range(t):
    a, b = map(int, input().split())  # .split()이면 \n 제거 불필요
    out.append(f"{a+b}\n")

sys.stdout.write(''.join(out))  # 한 번에 출력(속도 ↑)


# 두 번째 코드
import sys

data = sys.stdin.buffer.read().split()  # 전부 읽어서 공백 기준 분리
it = iter(data)
t = int(next(it))
out = []
for _ in range(t):
    a = int(next(it)); b = int(next(it))
    out.append(f"{a+b}\n")

sys.stdout.write(''.join(out))
