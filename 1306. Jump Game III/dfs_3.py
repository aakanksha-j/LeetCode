class Solution:
    """Approach 3: DFS and make value of array negative so that in future
                   recursion that value is not considered in if condition.
       Time complexity: O(n)
       Space complexity: O(n) for crawled list
       Runtime: 224 ms
       Memory: 21.2 MB
    """
    def canReach(self, arr, start) -> bool:
        if 0 <= start < len(arr) and arr[start] >= 0:
            arr[start] = -arr[start]
            return arr[start] == 0 or \
                   self.canReach(arr, start + arr[start]) or \
                   self.canReach(arr, start - arr[start])
        return False

def main():
    numbers = [0,1] # wrong answer scenario
    start = 1
    s=Solution()
    print(s.canReach(numbers, start))
    numbers = [4,2,3,0,3,1,2]
    start = 0
    print(s.canReach(numbers, start))
    numbers = [4,4,1,3,0,3]
    start = 2
    print(s.canReach(numbers, start))
    numbers = [3,0,2,1,2]
    start = 2
    print(s.canReach(numbers, start))

if __name__ == '__main__':
    main()
