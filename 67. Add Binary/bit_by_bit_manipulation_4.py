class Solution():
    def addBinary(self, a, b):
        """
        Approach 4: Use x and y to store a and b in binary form. Calculate sum
                    without carry using xor. And carry using left-shifted AND.
                    Continue as while loop till y becomes 0. Carry gets added to
                    sum without carry which becomes the final result.
        Time complexity: O(N + M) where N and M are input lengths of a, b.
        Space complexity: O(max(N, M)) to keep the answer
        Runtime: 32 ms
        Memory: 14.4 MB
        """
        x, y = int(a, 2), int(b, 2)
        print(x, y)
        while y:
            answer, carry = x ^ y, (x & y) << 1
            x, y = answer, carry
            print(x, y)
        return bin(x)[2:]

s= Solution()
print(s.addBinary('1011','1010'))
