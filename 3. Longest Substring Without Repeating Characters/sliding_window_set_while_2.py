# neetcode solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window, two pointers, using set instead of dictionary

        result = 0
        seen = set()
        left = 0

        for right, ch in enumerate(s):
            # set contains only elements for current substring
            while ch in seen:
                seen.remove(s[left])
                left += 1

            result = max(result, right - left + 1)
            seen.add(ch)

        return result
