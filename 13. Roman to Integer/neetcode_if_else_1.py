class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res = 0
        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]
        return res

"""https://www.youtube.com/watch?v=3jdxYj3DD98&t=335s&ab_channel=NeetCode"""

"""
leetcode Solution
class Solution:
    def romanToInt(self, s: str) -> int:
        # time and space- O(1)

        roman = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        n, output = len(s), 0

        i = 0
        while i < n:
            if i + 1 < len(s) and roman[s[i]] < roman[s[i+1]]:
                output += roman[s[i+1]] - roman[s[i]]
                i += 2
            else:
                output += roman[s[i]]
                i += 1

        return output


own approach
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dic = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}

        root = 0
        i, n = 0, len(s)
        while i < n - 1:
            if s[i] is 'C' and s[i+1] is 'M':
                root += 900
                i += 2
            elif s[i] is 'C' and s[i+1] is 'D':
                root += 400
                i += 2
            elif s[i] is 'X' and s[i+1] is 'C':
                root += 90
                i += 2
            elif s[i] is 'X' and s[i+1] is 'L':
                root += 40
                i += 2
            elif s[i] is 'I' and s[i+1] is 'X':
                root += 9
                i += 2
            elif s[i] is 'I' and s[i+1] is 'V':
                root += 4
                i += 2
            elif s[i] in roman_dic:
                root += roman_dic[s[i]]
                i += 1

        return root + roman_dic[s[n - 1]] if i == n - 1 else root


                
"""
