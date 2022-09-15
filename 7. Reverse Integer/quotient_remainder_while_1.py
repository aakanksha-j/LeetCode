class Solution:
    def reverse(self, x: int) -> int:
        # leetcode solution
        # 32 bit signed integer range: -2147483648 to 2147483647

        quotient = abs(x)
        reversed_x = 0
        while quotient > 0:

            remainder = quotient % 10
            if reversed_x > 214748364: return 0
            if reversed_x == 214748364:
                if x < 0 and remainder > 8: return 0
                if x > 0 and remainder > 7: return 0
            reversed_x = (reversed_x * 10) + remainder
            quotient //= 10

            #print(reversed_x, quotient, remainder)


        return reversed_x if x > 0 else -1 * reversed_x


9 9 2022 7 Reverse Integer

time: O(log x) roughly log x base to 10 digits in x
space: O(1)
