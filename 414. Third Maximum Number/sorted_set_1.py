class Solution:
    """Approach 1: Using set to get unique elements and sorted to get third
                   element.
       Time complexity: O(n)
       Space complexity: O(1)
       Runtime: 52 ms
       Memory: 15.4 MB"""
    def thirdMax(self, nums):
        return sorted(set(nums))[-3] if len(set(nums)) > 2 else max(nums)

def main():
    numbers =[3, 2, 1]
    s=Solution()
    print(s.thirdMax(numbers))
    numbers = [1, 2]
    print(s.thirdMax(numbers))
    numbers = [2, 2, 3, 1]
    print(s.thirdMax(numbers))
    numbers = [1, 0, 1, 0]
    print(s.thirdMax(numbers))
    numbers = [1, 2, 3, 4, 5, 6]
    print(s.thirdMax(numbers))

if __name__ == '__main__':
    main()
