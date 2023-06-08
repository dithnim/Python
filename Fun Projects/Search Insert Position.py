class Solution(object):
    def searchInsert(self, nums, target):
        if target in nums:
            index = nums.index(target)
        else:
            for i in range(len(nums)):
                if nums[i]<target:
                    index = i + 1
            if target<nums[0]:
                index = 0

        print(index)

num = Solution()
num.searchInsert([1,3,5,6],2)