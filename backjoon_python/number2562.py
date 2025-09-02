nums = []
for _ in range(9):
    nums.append(int(input()))

max = nums[0]
s = 0

for i in range(len(nums)):
    if nums[i] > max:
        max = nums[i]
        s = i

print(max)
print(s+1)
