class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # iterative dp bottom up solution

        # https://leetcode.com/problems/paint-house/discuss/68256/Python-solutions-with-different-space-usages.

        n = len(costs) # no. of houses
        k = 3 # no. of colors

        dp = costs[0] # use this array to store the processing done at each home
        for i in range(1, n): # start from 1 since home at index 0 already added in dp
            pre = dp[:] # use duplicate array since we need dp state as per 1 before
            for j in range(k):
                dp[j] = costs[i][j] + min(pre[:j] + pre[j + 1:])

        return min(dp)

"""
eg. Input: costs = [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
Minimum cost: 2 + 5 + 3 = 10.

house/color 0    1   2
0           17   2   17
1           18   33  7
2           21   10  37
"""
