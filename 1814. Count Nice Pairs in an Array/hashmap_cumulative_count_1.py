class Solution:
    def rev(self, x):
        quotient = x
        reversed_x = 0
        while quotient > 0:
            remainder = quotient % 10
            reversed_x = (reversed_x * 10) + remainder
            quotient //= 10
        return reversed_x

    def countNicePairs(self, nums: List[int]) -> int:
        print(len(nums))
        hashmap = {}
        count_nice = 0
        for i, num in enumerate(nums):
            prev = hashmap.get((num - self.rev(num)), 0)
            count_nice += prev
            print(count_nice)
            hashmap[num - self.rev(num)] = prev + 1
        return count_nice % ((10**9) + 7)


"""def countNicePairs(self, A):
        res = 0
        count = collections.Counter()
        for a in A:
            b = int(str(a)[::-1])
            res += count[a - b]
            count[a - b] += 1
        return res % (10**9 + 7)"""
