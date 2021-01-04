class Solution:
    """Approach 1: Linear scan. Every number has 2 factors, 1 and number itself.
                   Initialize left factor to 1 and append every new factor till
                   the already in list number is not reached.
       Time complexity: O(n) for in and sort()
       Space complexity: O(n) for factor_list
       Runtime: 36 ms
       Memory: 14.3 MB
    """
    def kthFactor(self, n: int, k: int) -> int:
        if n < 1 or k < 1 or n > 1000 or k > 1000:
            return 'Invalid input.'
        if n == 1:
            factor_list = [1]
            return 1 if k == 1 else -1
        factor_list = []
        left = 1
        while left not in factor_list:
            if n % left == 0:
                factor_list.append(left)
                if n // left not in factor_list:
                    factor_list.append(n // left)
            left += 1
        factor_list.sort()

        return factor_list[k-1] if k-1 < len(factor_list) else -1

def main():
    n = 100
    k = 6
    s=Solution()
    print(s.kthFactor(n, k))
    n = 1000
    k = 3
    print(s.kthFactor(n, k))
    n = 999
    k = 5
    print(s.kthFactor(n, k))
    n = 1
    k = 1
    print(s.kthFactor(n, k))

if __name__ == '__main__':
    main()
