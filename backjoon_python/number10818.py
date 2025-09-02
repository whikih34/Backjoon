n = int(input())
nums = list(map(int, input().split()))

max = nums[0]
min = nums[0]

for nu in nums:
    if nu > max:
        max = nu
    
    if nu < min:
        min = nu

print(min, max)