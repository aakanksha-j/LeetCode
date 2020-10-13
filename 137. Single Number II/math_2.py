class Solution:
    """Approach 2: 3(a+b+c)-(a+a+b+b+c)=2c/2.
       Time complexity: O(n)
       Space complexity: O(n) for set
       Runtime: 52 ms
       Memory: 15.5 MB"""
    def singleNumber(self, nums):
        return (3*(sum(set(nums)))-sum(nums))//2

def main():
    numbers =[2,1,2,2]
    s=Solution()
    print(s.singleNumber(numbers))
    numbers =[4,1,2,1,2,1,2]
    print(s.singleNumber(numbers))


if __name__ == '__main__':
    main()
