class Solution(object):
    def findDisappearedNumbers(self, nums):
         return list(set(range(1,len(nums)+1)).difference(set(nums)))


num = Solution()
print(num.findDisappearedNumbers([4,3,2,7,8,2,3,1]))