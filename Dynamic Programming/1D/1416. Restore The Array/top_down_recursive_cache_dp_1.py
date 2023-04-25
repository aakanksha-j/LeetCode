"""
1416. Restore The Array
Hard
A program was supposed to print an array of integers. The program forgot to print whitespaces and the array is printed as a string of digits s and all we know is that all integers in the array were in the range [1, k] and there are no leading zeros in the array.

Given the string s and the integer k, return the number of the possible arrays that can be printed as s using the mentioned program. Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: s = "1000", k = 10000
Output: 1
Explanation: The only possible array is [1000]
Example 2:

Input: s = "1000", k = 10
Output: 0
Explanation: There cannot be an array that was printed this way and has all integer >= 1 and <= 10.
Example 3:

Input: s = "1317", k = 2000
Output: 8
Explanation: Possible arrays are [1317],[131,7],[13,17],[1,317],[13,1,7],[1,31,7],[1,3,17],[1,3,1,7]
 

Constraints:

1 <= s.length <= 105
s consists of only digits and does not contain leading zeros.
1 <= k <= 109

"""

# algorithm: # https://leetcode.com/problems/restore-the-array/solution/
# k = 1000
# dfs(0) = dfs(1) + dfs(2) + dfs(3)
# '199304' = [1]'99304' + [19]'9304' + [199]'304'
# '04' invalid starts from '0'
# [1993] invalid as value > k

# base conditions:
# 1. reached end of string, remaining string is '' which is possible in one way so return 1
# 2. starts with '0', return 0
    
# for recursive condition, run for loop until (end of string / length of k) whichever is smaller
# and call dfs on next index

# https://leetcode.com/problems/restore-the-array/discuss/585552/JavaC%2B%2B-DFS-Memoization-Clean-code
from functools import lru_cache

def numberOfArrays(self, s: str, k: int) -> int:
        @lru_cache(None)
        def dfs(i):
            if i == len(s): return 1
            if s[i] == '0': return 0
            res, cur = 0, ''
            for j in range(i, len(s)):
                cur += s[j]
                if int(cur) > k: break
                res += dfs(j+1)
            return res % int(1e9 + 7)
        
        return dfs(0)

# O(n. logk) time - log k because of for loop which runs for k digits
# O(n) space for cache

# own approach - slower than above
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        mod = 10**9 + 7
        
        @lru_cache(None)
        def dfs(i):
            if i == len(s): return 1 
            if s[i] == '0': return 0
            
            ans = 0
            for j in range(i, min(len(s), i+len(str(k)))):
                if int(s[i:j+1]) > k:
                    break
                ans += dfs(j+1)
            
            return ans % mod
            
        return dfs(0) % mod





