class Solution:
    """Approach 1:
       Time complexity: O(log n)
       Space complexity: O(log n)
       Runtime: 24 ms
       Memory: 14.1 MB
    """
    def myPow(self, x: float, n: int) -> float:
        if not n: # n == 0
            return 1
        if n < 0:
            return self.myPow(1/x, -n)
        if n%2: # n is odd
            return x * self.myPow(x*x, (n-1)/2)
        return self.myPow(x*x, n/2) # n is even


def main():
    s=Solution()
    print(s.myPow(2.0, 10))
    print(s.myPow(2.1, 3))
    print(s.myPow(2, -2))

if __name__ == '__main__':
    main()
