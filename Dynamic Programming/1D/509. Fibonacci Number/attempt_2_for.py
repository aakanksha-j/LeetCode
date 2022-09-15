class Solution(object):
    def fib(self, N):
        """
        Runtime: 20 ms
        Memory Usage: 12.7 MB

        :type N: int
        :rtype: int
        """
        n1=0
        n2=1
        for i in range(N):
            n1,n2=n2,n1+n2
        return n1

s=Solution()
print(s.fib(3))
