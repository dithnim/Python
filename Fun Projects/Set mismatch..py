# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

# You are given an integer array nums representing the data status of this set after the error.

# Find the number that occurs twice and the number that is missing and return them in the form of an array.


# Input: nums = [1,2,2,4]
# Output: [2,3]

# Input: nums = [1,1]
# Output: [1,2]


#single line code
class Solution(object):
    def findErrorNums(self, nums):
        return [sum(nums) - sum(set(nums)), len(nums)*(len(nums)+1)//2-sum(set(nums))]