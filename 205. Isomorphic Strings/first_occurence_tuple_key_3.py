class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # using first occurence as tuple key for dictionary

        return [s.find(ch) for ch in s] == [t.find(ch) for ch in t]

# https://leetcode.com/problems/isomorphic-strings/discuss/57941/Python-different-solutions-(dictionary-etc).
