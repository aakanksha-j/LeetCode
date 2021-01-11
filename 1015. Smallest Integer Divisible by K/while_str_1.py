class Solution:
    """Approach 1: Use while loop till N becomes divisible by K. Use type
                   conversion to str to find length of N.
       Time complexity: O(K) as loop runs till 0 remainder is found
       Space complexity: O(1) only variable n stored
       Runtime: 1964 ms
       Memory: 14.4 MB
    """
    def smallestRepunitDivByK(self, K) -> int:
        if K < 1 or K > 100000:
            return 'K is not in range(1,10000)'
        if K%2 == 0 or K%5 == 0:
            return -1
        unit_digit = K % 10
        if unit_digit == 2 or unit_digit == 4 or unit_digit == 6 or \
        unit_digit == 8 or unit_digit == 0 or unit_digit == 5:
           return -1
        n = 1
        #i = 1
        while n % K != 0:
            #print(i)
            n *= 10
            n += 1
            #i += 1
        return len(str(n))

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
    k = 10000
    print(s.smallestRepunitDivByK(k))

if __name__ == '__main__':
    main()
