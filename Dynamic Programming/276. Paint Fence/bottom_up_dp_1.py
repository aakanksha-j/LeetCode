class Solution:
    def numWays(self, n: int, k: int) -> int:
        # time: O(n)
        # space: O(1)

        # https://leetcode.com/problems/paint-fence/discuss/178010/The-only-solution-you-need-to-read
        if n == 1: return k
        if n == 2: return k**2
        num_ways_1, num_ways_2 = k, k**2
        num_ways_n = 0
        #print(num_ways_n, num_ways_2, num_ways_1)
        for i in range(3, n + 1):
            num_ways_n = (num_ways_1 + num_ways_2) * (k - 1)
            #print(num_ways_n, num_ways_2, num_ways_1)
            num_ways_2, num_ways_1 = num_ways_n, num_ways_2
        return num_ways_n
