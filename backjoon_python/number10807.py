# 첫 번째 코드
# n = int(input())

# map() 함수는 이터레이터 이므로, list로 만들어야 순회 여러번 가능
# nums = list(map(int, input().split()))
# v = int(input())

# # nums 리스트에서 v의 개수 세기, count()는 리스트의 메서드이기 때문에 nums를 리스트로 만듦
# print(nums.count(v))

# 두 번째 코드
n = int(input())
# 이터레이터로 한번만 순회하기
nums = map(int, input().split())   # 이터레이터 (리스트 아님)
v = int(input())

print(sum(1 for x in nums if x == v))

