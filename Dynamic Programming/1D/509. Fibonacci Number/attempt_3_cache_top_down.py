class Solution():
    """
    :type N: int
    :rtype: int
    """
    def __init__(self):
        self.cache={0:0,1:1}

    def fib(self,N)->int:
        if N==0 or N==1:
            return N
        return self.cached_fibo(N)

    def cached_fibo(self,N):
        if N in self.cache:
            return self.cache[N]
        return self.cached_fibo(N-1)+self.cached_fibo(N-2)
         
s=Solution()
print(s.fib(36))
print(s.fib(15))
