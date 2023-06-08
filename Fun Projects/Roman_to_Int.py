class Solution(object):
    def romanToInt(self, s):
        roman_dict = {"I": 1, "V": 5, "X": 10,
                      "L": 50, "C": 100, "D": 500, "M": 1000}
        out = 0
        for i in range(len(s)):
            curr = roman_dict[s[i]]
            if i < len(s) - 1:
                nxt = roman_dict[s[i + 1]]
                if curr < nxt:
                    out -= curr
                else:
                    out += curr

            else:
                out += curr

        print(out)
