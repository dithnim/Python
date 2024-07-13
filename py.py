nums = [9,6,4,2,3,5,7,0,1]

nums.sort()
num2 = list(range(nums[-1] + 1))

for i in num2:
    if i not in nums:
        print(i)
