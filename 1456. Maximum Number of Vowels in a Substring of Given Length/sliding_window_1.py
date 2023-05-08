"""1456. Maximum Number of Vowels in a Substring of Given Length
Medium
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length"""

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        max_cnt = 0
        cnt = 0
        for i in range(k):
            cnt += 1 if s[i] in 'aeiou' else 0
        max_cnt = cnt    
        for i in range(k, len(s)):   
            cnt += 1 if s[i] in 'aeiou' else 0
            cnt -= 1 if s[i-k] in 'aeiou' else 0
            max_cnt = max(max_cnt, cnt)
        return max_cnt

# time O(n)
# space O(1)

# leetcode solution - https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/solution/

# "weallloveyou"
# 7 