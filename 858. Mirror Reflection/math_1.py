class Solution:
    """Approach 1:
       Time complexity: O(n)
       Space complexity: O(1)
       Runtime: 24 ms
       Memory: 14.1 MB"""

    def mirrorReflection(self, p, q):
        if p < 1 or p > 1000 or q < 0 or q > p:
            return 'Invalid input.'

        if q == 0:
            return 0

        if p%q == 0: # if divisor is a multiple of dividend, quotient is odd,
                     # return 1, else 2
            return 1 if (p/q)%2 else 2

        while p%2 == 0 and q%2 == 0:
            p //= 2 # output wil contain decimal if / used instead of //
            q //= 2

        if p%2 != 0 and q%2 != 0: # both are odd, return 1
            return 1
        elif p%2 == 0 and q%2 != 0: # p is even, q is odd, return 2
            return 2
        elif p%2 != 0 and q%2 == 0: # p is odd, q is even, return 0
            return 0


        # 2 line solution 28 ms 14.2 mb
        # while p % 2 == 0 and q % 2 == 0: p, q = p // 2, q // 2
        # return 1 - p % 2 + q % 2

def main():
    p = 2
    q = 0
    s=Solution()
    print(s.mirrorReflection(p,q))
    p = 1
    q = 0
    print(s.mirrorReflection(p,q))
    p = 16
    q = 6
    print(s.mirrorReflection(p,q))
    p = 38
    q = 6
    print(s.mirrorReflection(p,q))
    p = 43
    q = 3
    print(s.mirrorReflection(p,q))
    p = 43
    q = 6
    print(s.mirrorReflection(p,q))
    p = 15
    q = 5
    print(s.mirrorReflection(p,q))
    p = 10
    q = 2
    print(s.mirrorReflection(p,q))
    p = 10
    q = 5
    print(s.mirrorReflection(p,q))

if __name__ == '__main__':
    main()
