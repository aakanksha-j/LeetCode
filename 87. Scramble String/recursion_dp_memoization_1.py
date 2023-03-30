# recursion with memoization
# O(N^4)
# https://leetcode.com/problems/scramble-string/discuss/29452/Python-dp-solutions-(with-and-without-memorization).

class Solution:
    def __init__(self):
        self.dict = {}
        
    def isScramble(self, s1: str, s2: str) -> bool:
        if (s1, s2) in self.dict:
            return self.dict[(s1,s2)]
        
        if len(s1) != len(s2) or sorted(s1) != sorted(s2): # pruning
            self.dict[(s1, s2)] = False
            return False
        
        if s1 == s2:
            self.dict[(s1, s2)] = True
            return True
        
        for i in range(1, len(s1)):
            if (self.isScramble(s1[:i], s2[:i]) and \
                self.isScramble(s1[i:], s2[i:])) or \
               (self.isScramble(s1[:i], s2[-i:]) and \
                self.isScramble(s1[i:], s2[:-i])):
                return True   

        self.dict[(s1, s2)] = False
        return False