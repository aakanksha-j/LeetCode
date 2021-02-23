class Solution:
    """Approach 1: https://leetcode.com/problems/group-anagrams/discuss/19202/5-line-Python-solution-easy-to-understand
       Time complexity: O(NKlogK), where N is the length of strs, and KK is
                        the maximum length of a string in strs. The outer loop
                        has complexity O(N)O(N) as we iterate through each
                        string. Then, we sort each string in O(KlogK) time.
       Space complexity: O(NK), the total information content stored in ans.
       Runtime: 96 ms
       Memory: 17.8 MB
    """
    def groupAnagrams(self, strs):
        cache = {}
        for w in strs:
            # sorted gives output ['a','e','t'], tuple makes it immutable.
            word_key = tuple(sorted(w))
            cache[word_key] = cache.get(word_key, []) + [w]
            # concatenation of list, similar to strings
            # print(cache[word_key])
        return list(cache.values())

def main():
    strs = ["eat","tea","tan","ate","nat","bat"]
    s=Solution()
    print(s.groupAnagrams(strs))
    strs = [""]
    print(s.groupAnagrams(strs))
    strs = ["a"]
    print(s.groupAnagrams(strs))

if __name__ == '__main__':
    main()

"""defaultdict means that if a key is not found in the dictionary, then instead
of a KeyError being thrown, a new entry is created. The type of this new entry
is given by the argument of defaultdict.
d = defaultdict(list)
d = defaultdict(int)

from collections import defaultdict
ans = defaultdict(list)
for s in strs:
    ans[tuple(sorted(s))].append(s)
return list(ans.values())"""
