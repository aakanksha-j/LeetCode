class Solution:
    def firstUniqChar(self, s: str) -> int:
        # own approach - make count dictionary, iterate through string again and return 1st character with count 1's index
        # space O(N) for dictionary, time O(2N) worst in case ch with count 1 does not exist.

        s_dic = {ch: 0 for ch in s}
        for ch in s:
            s_dic[ch] += 1
        for i, ch in enumerate(s):
            if s_dic[ch] == 1:
                return i
        return -1
        
