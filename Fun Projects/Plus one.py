class Solution(object):
    def plusOne(self, digits):
        return [int(x) for x in str(int(''.join([str(x) for x in digits])) + 1)]