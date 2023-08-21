"""
2272. Substring With Largest Variance
Hard
The variance of a string is defined as the largest difference between the number of occurrences of any 2 characters present in the string. Note the two characters may or may not be the same.

Given a string s consisting of lowercase English letters only, return the largest variance possible among all substrings of s.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "aababbb"
Output: 3
Explanation:
All possible variances along with their respective substrings are listed below:
- Variance 0 for substrings "a", "aa", "ab", "abab", "aababb", "ba", "b", "bb", and "bbb".
- Variance 1 for substrings "aab", "aba", "abb", "aabab", "ababb", "aababbb", and "bab".
- Variance 2 for substrings "aaba", "ababbb", "abbb", and "babb".
- Variance 3 for substring "babbb".
Since the largest possible variance is 3, we return it.
Example 2:

Input: s = "abcde"
Output: 0
Explanation:
No letter occurs more than once in s, so the variance of every substring is 0.
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.

"""
class Solution:
    def solve_one(self, a, b, s):
        var, max_var = 0, 0
        has_b, first_b = False, False
        
        for c in s:
            if c == a:
                var += 1
            elif c == b:
                has_b = True
                
                if first_b and var >= 0: # shift b, first was b and encountered another, 'baab'
                    first_b = False
                elif (var - 1) < 0: # restart subarray, 'bbaaa' max var is 2, not 1
                    first_b = True
                    var = -1
                else:
                    var -= 1 # var is always >=0 
                
            if has_b and var > max_var:
                max_var = var
        return max_var
        
    def largestVariance(self, s: str) -> int:
        # https://leetcode.com/problems/substring-with-largest-variance/discuss/2579146/%22Weird-Kadane%22-or-Intuition-%2B-Solution-Explained
        # kadane's algorithm application
        # time O(26*26*n) - two words a-z, kadane's on n length of string
        # space O(26) - freq counter
        
        max_variance = 0
        unique_ch = set(s)
        print(unique_ch)
        for major_ch in unique_ch:
            for minor_ch in unique_ch:
                if major_ch == minor_ch:
                    continue
                major_vs_minor_variance = self.solve_one(major_ch, minor_ch, s)
                max_variance = max(max_variance, major_vs_minor_variance)
        return max_variance