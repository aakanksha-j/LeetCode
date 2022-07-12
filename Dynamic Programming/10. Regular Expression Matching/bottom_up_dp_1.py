class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # bottom up dp

        # refer wildcard matching diagram - https://leetcode.com/problems/wildcard-matching/discuss/256025/Python-DP-with-illustration
        # 2 bottom up dp solutions for reference - https://leetcode.com/problems/regular-expression-matching/discuss/599304/Python-bottom-up-DP
        # https://leetcode.com/problems/regular-expression-matching/discuss/1440437/C%2B%2B-or-Bottom-Up-DP-or-Explanation-or-O(m*n)-time-or-0ms-runtime
        # string s and pattern p are 0 indexed, dp is 1 indexed because it considers empty string in beginning

        dp = [[False for j in range(len(p) + 1)] for i in range(len(s) + 1)]

        dp[0][0] = True # base case 1: both s and p are empty

        for j in range(2, len(p) + 1):
            if p[j - 1] == '*' and dp[0][j - 2]: # base case 2: s is empty and p has '*''
                dp[0][j] = True

        # regenerative cases:
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if j == 3 and i == 2:
                    print(p[j-1], s[i - 1])
                if p[j - 1] in (s[i - 1], '.'):
                    print(j, i)
                    dp[i][j] = dp[i - 1][j - 1] # use prev
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] # matches 0 times
                    if p[j - 2] in (s[i - 1], '.'):
                        dp[i][j] = dp[i][j] or dp[i - 1][j] # matches atleast 1 time
        #print(dp)
        return dp[-1][-1]


"""test cases:
* matches 0 or more occurence of character before *
. matches any single character

pattern a.b
valid   acb aab
invalid ab cb acby

pattern a*b
valid   b ab aab aaab
invalid a acb

pattern a*b.*y
valid   by bly ably aablmy
invalid ay ab

pattern c*a*b
valid   aab   
[[True, False, True, False, True, False],
[False, False, False, True, True, False],
[False, False, False, False, True, False],
[False, False, False, False, False, True]]"""
