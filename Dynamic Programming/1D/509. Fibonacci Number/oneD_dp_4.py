class Solution:
    def fib(self, n: int) -> int:
        # 1d dp
        tn, tn1 = 0, 1
        if n == 0: return tn
        if n == 1: return tn1
        curr, tn2 = 2, 0
        while curr <= n:
            tn2 = tn + tn1
            tn, tn1 = tn1, tn2
            curr += 1
        return tn2

s=Solution()
print(s.fib(36))
