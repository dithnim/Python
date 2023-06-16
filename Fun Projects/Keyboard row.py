class Solution(object):
    def findWords(self, words):
        result = []
        set1 = set("qwertyuiop")
        set2 = set("asdfghjkl")
        set3 = set("zxcvbnm")
        for word in words:
            w = set(word.lower())
            if w <= set1 or w <= set2 or w <= set3:
                result.append(word)
        return result


word = Solution()
print(word.findWords(["Hello","Alaska","Dad","Peace"])) 