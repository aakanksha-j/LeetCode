class Solution:
    """Approach 2: https://leetcode.com/problems/numbers-at-most-n-given-digit-set/discuss/168279/Python-O(logN)
                   One while loop and one list comprehension for loop. Outer
                   while loop for n and inner lc for digits. Break while loop if
                   any digit in n is not present in string 'digits'. Add 1 to
                   counter if while loop runs upto length of n showing that all
                   digits in n are from string 'digits'.
       Time complexity: O(log n)
       Space complexity: O(log n)
       Runtime: 56 ms
       Memory: 14.3 MB
    """
    def atMostNGivenDigitSet(self, digits, n: int) -> int:
        N = str(n)
        n_len = len(N)

        # 1st for loop
        op = sum(len(digits) ** i for i in range(1, n_len)) # n = 2563, digits = {"1", "2", "6"}
        # add x, xx, xxx scenario i.e 3, 3^2, 3^3

        # 2nd for loop
        # add 1xxx, 21xx, 22xx, 261x, 262x for n = 2653, d = {"1", "2", "6"}
        i = 0
        while i < n_len:
            op += sum(d < N[i] for d in digits) * (len(digits) ** (n_len - 1 - i))
            if N[i] not in digits:
                break
            i += 1

        #print(i)
        return op + (i == n_len)

def main():
    digits = ["6","8"]
    n = 8
    s=Solution()
    print(s.atMostNGivenDigitSet(digits, n))
    digits = ["1","4","9"]
    n = 1000000000
    print(s.atMostNGivenDigitSet(digits, n))
    digits = ["1","3","5","7"]
    n = 100
    print(s.atMostNGivenDigitSet(digits, n))
    digits = ["1","2","6"]
    n = 2653
    print(s.atMostNGivenDigitSet(digits, n))

if __name__ == '__main__':
    main()
