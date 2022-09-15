class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window, two pointers
        # after 1004, 487 max consecutive ones 3, 2

        # similar to 209. Minimum size subarray sum

        result = 0
        seen = {}
        left = 0

        for right, ch in enumerate(s):
            # if loop instead of while
            if ch in seen and left <= seen[ch]:
                    left = seen[ch] + 1 # similar to 487's lastzeroindex + 1
            else:
                result = max(result, right - left + 1)

            seen[ch] = right

        return result


"""
testcases:'pwkeo', 'pwwkewp', 'pwkew'
"""


"""
extra space for dictionary
own approach - uses while, takes extra time

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        # after max consecutive ones

        # no elements, empty string
        if not s:
            return 0

        # only one element
        if len(s) == 1: return 1

        # similar to 209. Minimum size subarray sum
        result = 0
        seen = {}
        left = 0
        for right, ch in enumerate(s):
            #print(right, ch)
            if ch in seen:
                while seen[ch] >= left: # if
                    result = max(result, right - left)
                    left += 1
            seen[ch] = right

        #print(right - left + 1)
        return max(result, right - left + 1)
"""
