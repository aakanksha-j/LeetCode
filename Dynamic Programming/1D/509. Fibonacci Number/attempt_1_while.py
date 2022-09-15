class Solution(object):
    def fib(self, N):
        """
        Runtime: 24 ms
        Memory Usage: 12.6 MB
        :type N: int
        :rtype: int
        """
        n1=0
        n2=1
        i=1
        while i<=N:
            n1,n2=n2,n1+n2
            i+=1
        return n1

s=Solution()
print(s.fib(36))
