class Solution:
    """Approach 1: https://leetcode.com/problems/numbers-at-most-n-given-digit-set/discuss/168439/C%2B%2B-O(logN)-Clear-code-with-explanation
                   Two for loops. One for digits less than n. Another for loop
                   for digits upto n. If n contains a digit which is not present
                   in string 'digits', then return the sum of counter as output.
                   Otherwise, add 1 to output to include n which contains all
                   digits from string only.
       Time complexity: O(log n)
       Space complexity: O(log n)
       Runtime: 48 ms
       Memory: 14.1 MB
    """
    def atMostNGivenDigitSet(self, digits, n: int) -> int:
        op = 0
        d_len = len(digits)
        N = str(n)
        n_len = len(N)

        # 1st for loop
        op = sum(d_len ** i for i in range(1, n_len)) # n = 2563, digits = {"1", "2", "6"}
        # add x, xx, xxx scenario i.e 3, 3^2, 3^3

        # 2nd for loop
        # add 1xxx, 21xx, 22xx, 261x, 262x for n = 2653, d = {"1", "2", "6"}
        for i in range(n_len):
            has_same_num = False
            for digit in digits:
                if digit < N[i]: # n = 2653, 261x and 262x add 3+3 = 6 counts
                    print(d_len ** (n_len - 1 - i))
                    op += d_len ** (n_len - 1 - i)
                elif digit == N[i]:
                    has_same_num = True
            if not has_same_num:
                return op

        return op + 1

def main():
    digits = ["7"]
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
