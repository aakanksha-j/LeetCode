class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # neetcode solution - constrained programming (to put restrictions afer each dot placement)
        # dont know where is backtracking used

        # time complexity: 3*3*3 = 27 combinations to check
        # space complexity: O(n) - space needed for recursion stack, to keep solutions

        # edge cases: 1. IP address cannot contain than 12 numbers (max: 255.255.255.255)
        # 2. No leading zeroes allowed. 0.0.0.0 is valid, 12.01.33.45 not allowed
        # 3. if there is string left after placing all 4 dots, do not add that IP address to result
        # 4. every integer has 256 choices between 0 and 255, no negative or more than 255 integers allowed

        res, validIP = [], ''

        if len(s) > 12:
            return

        def dfs_backtrack(i, dots, validIP):

            if dots == 4 and i == len(s):
                res.append(validIP[:-1]) # -1 to get rid of 4th dot
                return

            if dots > 4: # string left after 4 dots
                return

            for j in range(i, min(i + 3, len(s))):
                if int(s[i: j + 1]) < 256 and ((i == j) or (s[i] != '0')): # integer must be less than / equal to 255 and no leading zeroes, only '0' allowed
                    #print(validIP)
                    dfs_backtrack(j + 1, dots + 1, validIP + s[i: j + 1] + '.')

        dfs_backtrack(0, 0, validIP)

        return res
    
