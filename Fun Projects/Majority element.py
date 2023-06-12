class Solution(object):
    def majorityElement(self, nums):
        hm={}
        ans=0
        for i in nums:
            hm[i]=hm.get(i,0)+1
        for i,j in hm.items():
            if len(nums)//2<j:
                ans=max(ans,i)
        return ans

num = Solution()
print(num. majorityElement([3,3,4]))
