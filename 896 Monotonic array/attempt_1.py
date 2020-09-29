class Solution(object):
    def isMonotonic(self, A):
        """
        Runtime: 452 ms
        Memory Usage: 17.6 MB
        :type A: List[int]
        :rtype: bool
        """
        if len(A)==1 or len(A)==2:
            return True
        ascending_flag,descending_flag=False,False
        for i in range(len(A)-1):
            if A[i]<A[i+1]:
                ascending_flag=True
            if A[i]>A[i+1]:
                descending_flag=True
            if ascending_flag and descending_flag:
                return False
        return True

s=Solution()
print(s.isMonotonic([1,2,3,3]))
