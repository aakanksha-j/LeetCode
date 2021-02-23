class Solution:
    """Approach 1: Binary search template 2. Have to include letters[mid] = target
                   scenario in left= mid + 1 because we want next greater element.
       Time complexity: O(log n)
       Space complexity: O(1)
       Runtime: 100 ms
       Memory: 14.5 MB
    """
    def nextGreatestLetter(self, letters, target: str) -> str:
        # input array is sorted.
        if target < letters[0] or letters[-1] <= target: # z [a,b], j[c,j]
            return letters[0]
        left, right = 0, len(letters) - 1
        while left < right:
            mid = left + (right - left) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return letters[left]

def main():
    numbers = ["c", "f", "j"]
    target = "a"
    s=Solution()
    print(s.nextGreatestLetter(numbers, target))
    target = "e"
    numbers = ["e","e","e","e","e","e","n","n","n","n"]
    print(s.nextGreatestLetter(numbers, target))
    target = "k"
    numbers = ["c", "f", "j"]
    print(s.nextGreatestLetter(numbers, target))


if __name__ == '__main__':
    main()
