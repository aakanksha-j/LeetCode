class Solution:
    """Approach 1: Run for loop on entire array and XOR.
       Time complexity: O(n)
       Space complexity: O(1)
       Runtime: 84 ms
       Memory: 16.4 MB"""
    def singleNumber(self, nums):
        missing=0
        for i in nums:
            missing^=i
        return missing

def main():
    numbers =[2,1,2]
    s=Solution()
    print(s.singleNumber(numbers))
    numbers =[4,1,2,1,2]
    print(s.singleNumber(numbers))


if __name__ == '__main__':
    main()
