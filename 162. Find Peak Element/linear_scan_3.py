class Solution:
    """Approach 3: Linear scan upto second last element.
       Time complexity: O(log n)
       Space complexity: O(1)
       Runtime: 44 ms
       Memory: 14.3 MB
    """
    def findPeakElement(self, nums) -> int:
        for i in range(len(nums)-1):
            if nums[i] > nums[i + 1]:
                return i
        return len(nums) - 1

def main():
    numbers = [16,17,18]
    s=Solution()
    print(s.findPeakElement(numbers))
    numbers =[16, 15, 14, 13]
    print(s.findPeakElement(numbers))
    numbers =[16,18,16,1,2,3,0]
    print(s.findPeakElement(numbers))

if __name__ == '__main__':
    main()
