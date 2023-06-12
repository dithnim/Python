# Given an integer x, return true if x is a palindrome , and false otherwise

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

class Solution(object):
    def isPalindrome(self, x):
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False


number = Solution()
print(number.isPalindrome(121))