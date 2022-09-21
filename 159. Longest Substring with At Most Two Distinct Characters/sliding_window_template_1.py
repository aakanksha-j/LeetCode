# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/discuss/49708/Sliding-Window-algorithm-template-to-solve-all-the-Leetcode-substring-search-problem.

# time: O(N) - iterate every element maximum twice, once to add from right, once to remove from left
# space: O(1) - size of hashmap (freq counter) is almost fixed i.e max 3 elements if k = 2

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        k = 2
        output = 0
        freq = Counter()
        l, r = 0, 0
        while r < len(s):
            freq[s[r]] += 1 
            r += 1
            while len(freq) > k:
                alphabet_to_be_removed = s[l]
                # print(alphabet_to_be_removed, s[l])
                freq[alphabet_to_be_removed] -= 1
                if freq[alphabet_to_be_removed] == 0:
                    del freq[alphabet_to_be_removed]
                l += 1
            output = max(output, r - l)
            # print(len(freq))
            # print(output)
                
        # print(output)
        return output
            
# test case 
# "eceba" op 3
# 2
# "aa" op 2
# 1
# "abaccc" op 4
# 2
