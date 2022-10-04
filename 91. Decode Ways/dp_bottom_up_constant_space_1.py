class Solution:
    def numDecodings(self, s: str) -> int:
        # bottom-up dp space optimized
        # https://leetcode.com/problems/decode-ways/discuss/30451/Evolve-from-recursion-to-dp
        
        # time O(N)
        # space O(1)
        
        # edge case if string starts with 0
        if s[0] == '0': return 0
        
        two_back, one_back = 1, 1 # if only one element, return 1 i.e one_back
        for i in range(1, len(s)): # start from 2nd element
            curr = one_back if s[i] != '0' else 0
            if 10 <= int(s[i - 1: i + 1]) <= 26:
                curr += two_back
            two_back, one_back = one_back, curr
            
        return one_back