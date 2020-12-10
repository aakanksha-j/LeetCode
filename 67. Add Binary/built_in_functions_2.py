class Solution():
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        Approach 2: Convert a and b into integers. Compute the sum. Convert the
                    sum back into binary form. This method has 2 drawbacks. If
                    the result is big, it may not fit into Integer, Long or
                    Biginteger in Java. Therefore use bit-by-bit manipulation
                    approach. This method has low performance in large input
                    numbers.
        Time complexity: O(N + M)
        Space complexity: O(N + M)
        Runtime: 32 ms
        Memory: 14.1 MB
        """
        return '{0:b}'.format(int(a,2)+int(b,2))

s= Solution()
print(s.addBinary('1011','1010'))
