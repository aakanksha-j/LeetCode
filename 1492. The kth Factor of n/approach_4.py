class Solution:
    """Approach 4: Run for loop from 1 to sqrt of n plus 1.
                   Checks for all values upto (n/2)+1. Similar to approach 3
                   but instead of altering k, we use a variable to keep count
                   of divisors.
       Time complexity: O(sqrt(n)) for loop of left side of divisors
       Space complexity: O(min(k,sqrt(n))) for list of divisors
       Runtime: 32 ms
       Memory: 14 MB
    """
    def kthFactor(self, n: int, k: int) -> int:
        cur_factor_count = 0
        divisors, sqrt_n = [], int(n**.5)
        for i in range(1, sqrt_n + 1):
            if n % i == 0:
                cur_factor_count += 1
                divisors.append(i)
                if cur_factor_count == k:
                    return i
        if sqrt_n**2 == n:
            n_div = 2 * len(divisors) - 1
        else:
            n_div = 2 * len(divisors)
        return n // divisors[n_div - k] if k <= n_div else -1

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
    n = 4
    k = 4
    print(s.kthFactor(n, k))

if __name__ == '__main__':
    main()
