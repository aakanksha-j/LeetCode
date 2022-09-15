class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # binary search intuitive solution using less than greater than variables

        l, r = 1, len(nums) - 1
        print('l:',l,'r:',r)
        while True:
            mid = (l + r) // 2
            print('mid:',mid)
            leq = 0
            geq = 0
            for n in nums:
                print('n:',n)
                if n <= mid:
                    leq += 1
                    print('leq:',leq)
                if n >= mid:
                    geq += 1
                    print('geq:',geq)
            if leq > mid:
                r = mid
                print('r becomes mid:',r)
            if geq > len(nums) - mid:
                l = mid
                print('l becomes mid:', l)
            if l == r:
                print('l=r', l)
                return l
            if l == mid:
                l += 1
            else:
                r -= 1



[[1, 1, 0, 0, 0, 0],[1, 1, 0, 0, 0, 0],[0, 0, 1, 0, 1, 0],[0, 0, 0, 1, 0, 0],[0, 0, 1, 0, 1, 0],[0, 0, 0, 0, 0, 1]]
