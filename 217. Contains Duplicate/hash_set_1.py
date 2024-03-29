class Solution:
    """Approach 1: Store unique elements in hashtable using set.
       Time complexity: O(n) to traverse using for loop
       Space complexity: O(n) to store distinct elements in hashtable.
       Runtime: 120 ms
       Memory: 20.4 MB
    """
    def containsDuplicate(self, nums) -> bool:
        return not len(nums) == len(set(nums))
        """nums_set = set()
        for num in nums:
            if num in nums_set:
                return True
            nums_set.add(num)
        return False"""

def main():
    numbers = [1,2,3,1]
    s=Solution()
    print(s.containsDuplicate(numbers))
    numbers = [1,2,3,4]
    print(s.containsDuplicate(numbers))
    numbers = [1,1,1,3,3,4,3,2,4,2]
    print(s.containsDuplicate(numbers))

if __name__ == '__main__':
    main()

"""Solved again using sorting and then comparing.
Time: O(nlogn) for sorting the list
space: O(n) to store sorted list as we do not modify input.

    def containsDuplicate(self, nums: List[int]) -> bool:
        num = sorted(nums)
        prev = num[0]

        for n in num[1:]:
            print(n)
            if n == prev:
                return True
            prev = n
        return False"""
