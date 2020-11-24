import math
class Solution:
    """Approach 1: Using GCD from math library to reduce p and q. 
       Time complexity: O(n)
       Space complexity: O(1)
       Runtime: 24 ms
       Memory: 14 MB"""

    def mirrorReflection(self, p, q):
        if p < 1 or p > 1000 or q < 0 or q > p:
            return 'Invalid input.'

        x = p // math.gcd(p, q)
        y = q // math.gcd(p, q)

        if x % 2 == 1 and y % 2 == 1:
            return 1
        elif x % 2 == 0 and y % 2 == 1:
            return 2
        else:
            return 0

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
