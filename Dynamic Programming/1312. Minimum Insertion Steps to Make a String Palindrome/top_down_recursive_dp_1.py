"""
1312. Minimum Insertion Steps to Make a String Palindrome
Hard
Given a string s. In one step you can insert any character at any index of the string.

Return the minimum number of steps to make s palindrome.

A Palindrome String is one that reads the same backward as well as forward.

 

Example 1:

Input: s = "zzazz"
Output: 0
Explanation: The string "zzazz" is already palindrome we do not need any insertions.
Example 2:

Input: s = "mbadm"
Output: 2
Explanation: String can be "mbdadbm" or "mdbabdm".
Example 3:

Input: s = "leetcode"
Output: 5
Explanation: Inserting 5 characters the string becomes "leetcodocteel".
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.
"""
from functools import lru_cache


class Solution:
    def minInsertions(self, s: str) -> int:
        # top down recursive dp - refer vokasi
        
        # test cases abc, abb, bbb
        # if s[start] == s[end]: 0 insert + move to [start+1, end-1]
        # else 1 insertion + move to min(dfs[start+1, end], dfs[start, end-1])
        
        # time O(n^2)
        # space O(n^2)
        
        @lru_cache(None)
        def dfs(start, end):
            if start > end:
                return 0
            if start == end:
                return 0
            if s[start] == s[end]:
                return dfs(start+1, end-1)
            else:
                return 1 + min(dfs(start+1, end), dfs(start, end-1))
                
        N = len(s) 
        return dfs(0, N-1)