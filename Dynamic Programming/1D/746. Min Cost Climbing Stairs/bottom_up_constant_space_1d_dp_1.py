class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # bottom up constant space approach - 1d

        if len(cost) == 2: return min(cost[0], cost[1])

        fi1, fi2 = cost[0], cost[1] # comparison starts from index 2
        fi = 0
        for i in range(2, len(cost)):
            #print(fi1, fi2)
            fi = cost[i] + min(fi1, fi2) # function formula
            fi1, fi2 = fi2, fi
            #print(fi)

        return min(fi,fi1) #fi2 has also become fi, so compare fi and fi1

"""
time: O(N) we need to traverse N-2 elements starting from index 2.
space: O(1) we need to store only last 2 inputs so constant space.
similar to 1 dimensional dp problems such as climbing stairs, fibonacci number.
"""
