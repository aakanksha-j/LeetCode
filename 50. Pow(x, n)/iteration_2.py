class Solution:
    """Approach 1: https://en.wikipedia.org/wiki/Exponentiation_by_squaring
       Time complexity: O(log n)
       Space complexity: O(1) we only need two variables for current product
                         and final result of x.
       Runtime: 32 ms
       Memory: 14.3 MB
    """
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n
        if n == 0:
            return 1
        y = 1
        while n > 1:
            if n % 2:
                # n is odd
                y = x * y
                x = x * x
                n = (n - 1) / 2
            else:
                # n is even
                x = x * x
                n = n / 2
        return x * y

def main():
    s=Solution()
    print(s.myPow(2.0, 10))
    print(s.myPow(2.1, 3))
    print(s.myPow(2.0, -2))

if __name__ == '__main__':
    main()
