class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count = 0;out = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count = 0
            if out < count:
                out = count
        return out


num = Solution()
print(num.findMaxConsecutiveOnes([1,0,1,1,0,1]))