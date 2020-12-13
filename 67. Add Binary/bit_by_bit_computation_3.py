class Solution():
    def addBinary(self, a, b):
        """
        Approach 3: Use carry variable and list to store the computed bits.
        Time complexity: O(max(N, M)) where N and M are input lengths of a, b.
        Space complexity: O(max(N, M)) to keep the answer
        Runtime: 32 ms
        Memory: 14.2 MB
        """
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)

        carry = 0
        answer = []

        for i in range(n-1, -1 ,-1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1

            if carry%2:
                answer.append('1')
            else:
                answer.append('0')

            carry //= 2

        if carry == 1:
            answer.append('1')
        answer.reverse()

        return ''.join(answer)


s= Solution()
print(s.addBinary('1011','1010'))
