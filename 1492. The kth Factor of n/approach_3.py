class Solution:
    """Approach 3: Run for loop from 1 to square root of n plus 1.
       Time complexity: O(sqrt(N)) for loop
       Space complexity: O(min(k, sqrt(N))) to store the list of divisors
       Runtime: 32 ms
       Memory: 14.2 MB
    """
    def kthFactor(self, n: int, k: int) -> int:
        divisors, sqrt_n = [], int(n**.5)
        for x in range(1, sqrt_n + 1):
            print(x, k, divisors)
            if (n % x == 0):
                k -= 1
                divisors.append(x)
                if k == 0:
                    return x

        if (sqrt_n ** 2 == n): # if n is a perfect square, we have to skip the
            k += 1             # duplicate in the divisor list.

        n_div = len(divisors)
        return n // divisors[n_div - k] if k <= n_div else -1  # we're here
        # becoause the kth divisor is not yet found. Although divisors already
        # contains all 'independent' (eg. 1,3 for n=15), all other 'paired' ones
        # (eg. 5,15) i.e. the kth divisor could be computed as
        # N/ divisors[len(divisors)- k]

def main():
    n = 100
    k = 6
    s=Solution()
    print(s.kthFactor(n, k))
    n = 1000
    k = 16
    print(s.kthFactor(n, k))
    n = 999
    k = 5
    print(s.kthFactor(n, k))
    n = 1
    k = 1
    print(s.kthFactor(n, k))

if __name__ == '__main__':
    main()
