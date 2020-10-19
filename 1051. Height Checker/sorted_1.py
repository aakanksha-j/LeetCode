class Solution:
    """Approach 1: Used sorted() to get sorted array and then took sum of
                   mismatch between original and sorted array using a list
                   comprehension and zip.
       Time complexity: O(n)
       Space complexity: O(n) for another array sorted heights
       Runtime: 36 ms
       Memory: 14.1 MB"""
    def heightChecker(self, heights):
        return sum(h1 != h2 for h1, h2 in zip(heights, sorted(heights)))

def main():
    numbers = [1,1,4,2,1,3]
    s=Solution()
    print(s.heightChecker(numbers))
    numbers = [5,1,2,3,4]
    print(s.heightChecker(numbers))
    numbers = [1,2,3,4,5]
    print(s.heightChecker(numbers))
    numbers = [1,2,1,2,1,1,1,2,1]
    print(s.heightChecker(numbers))

if __name__ == '__main__':
    main()
