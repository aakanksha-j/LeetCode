class Solution:
    """Approach 2: Use for loop to run for k times but remainder value is not stored.
       Time complexity: O(K)
       Space complexity: O(1)
       Runtime: 2476 ms
       Memory: 14.3 MB
    """
    def smallestRepunitDivByK(self, K) -> int:
        if K < 1 or K > 100000:
            return 'K is not in range(1,10000)'
        if K%2 == 0 or K%5 == 0:
            return -1
        n = 1
        for i in range(K):
            if n % K == 0:
                return i + 1
            n *= 10
            n += 1
        return -1


def main():
    k = 1
    s=Solution()
    print(s.smallestRepunitDivByK(k))
    k = 99999
    print(s.smallestRepunitDivByK(k))
    k = 43
    print(s.smallestRepunitDivByK(k))
    k = 3
    print(s.smallestRepunitDivByK(k))
    k = 7
    print(s.smallestRepunitDivByK(k))
    k = 9
    print(s.smallestRepunitDivByK(k))
    k = 100000
    print(s.smallestRepunitDivByK(k))

if __name__ == '__main__':
    main()
