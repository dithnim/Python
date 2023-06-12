class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merge = sorted(nums1 + nums2)
        lenght = len(merge)

        if len(merge)%2 == 0:
            return (merge[lenght//2]+merge[lenght//2-1])/2
        return merge[len(merge)//2]



number = Solution()
print(number.findMedianSortedArrays([1,2],[3]))