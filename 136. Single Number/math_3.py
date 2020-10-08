class Solution:
    """Approach 1: 2(a+b+c)-(a+a+b+b+c)=c.
       Time complexity: O(n)
       Space complexity: O(n) for set
       Runtime: 84 ms
       Memory: 16.3 MB"""
    def singleNumber(self, nums):
        return 2*(sum(set(nums)))-sum(nums)

def main():
    numbers =[2,1,2]
    s=Solution()
    print(s.singleNumber(numbers))
    numbers =[4,1,2,1,2]
    print(s.singleNumber(numbers))


if __name__ == '__main__':
    main()
