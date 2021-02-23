import bisect

class Solution:
    """Approach 1: Using bisect function.
       Time complexity: O(log n)
       Space complexity: O(1)
       Runtime: 108 ms
       Memory: 14.5 MB
    """
    def nextGreatestLetter(self, letters, target: str) -> str:
        pos = bisect.bisect_right(letters, target) # for all values <= target
        # print(pos)
        return letters[0] if pos == len(letters) else letters[pos]

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
