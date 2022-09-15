class Solution:
    def isPalindrome(self, x: int) -> bool:
        # revert half the number

        # edge case: negative numbers and multiples of 10
        if (x < 0) or (x % 10 == 0 and x != 0):
            return False

        # using rev to avoid manipulating input
        res = 0
        rev = x
        while res < rev:
            rem =  rev % 10 #remainder
            rev //= 10 #quotient
            print(rev, res)
            res = (res * 10) + rem
        print(rev, res, x)
        return (res == rev) or (res // 10 == rev)

        
