class Solution:
    """Approach 2: Run for loop from 1 to half of n plus 1.
                   Checks for all values upto (n/2)+1.
       Time complexity: O(n/2) for loop
       Space complexity: O(1) no extra data structure
       Runtime: 32 ms
       Memory: 14.2 MB
    """
    def kthFactor(self, n: int, k: int) -> int:
        cur_factor_count = 0
        for i in range(1, (n//2) + 1):
            if n % i == 0:
                cur_factor_count += 1
            if cur_factor_count == k:
                return i
        if cur_factor_count + 1 == k:
            return n
        return -1

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
