class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        # using while loop, reduce both numbers such that one or both of them become odd
        # based on their state, return receptor

        # time: O(N)
        # space: O(1)

        # p odd, q even = 0
        # p odd, q odd = 1
        # p even, q odd = 2

        m, n = p, q
        while (m % 2 == 0 and n % 2 == 0):
            m /= 2
            n /= 2
        if (m % 2 == 0 and n % 2 == 1): return 2
        if (m % 2 == 1 and n % 2 == 1): return 1
        if (m % 2 == 1 and n % 2 == 0): return 0
