class Solution:
    """Approach 3: For loop is used and remainder after each loop is stored.
       Time complexity: O(k)
       Space complexity: O(1)
       Runtime: 60 ms
       Memory: 14.3 MB
    """
    def smallestRepunitDivByK(self, K) -> int:
        if K < 1 or K > 100000:
            return 'K is not in range(1,10000)'
        n = 0
        for length_N in range(1, K+1): # k+1-1 = k, loop goes till k only if k+1 is limit.
            n = ((n * 10) + 1) % K
            if n == 0:
                return length_N
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
