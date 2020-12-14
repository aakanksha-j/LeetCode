class Solution:
    """Approach 1: DFS with BFS since only two nodes possible from one parent node.
       Time complexity: O(n)
       Space complexity: O(n) for crawled list
       Runtime: 216 ms
       Memory: 20.7 MB
    """
    def canReach(self, arr, start) -> bool:
        if len(arr) < 1 or len(arr) > 50000:
            return 'Invalid arr range.'
        if start < 0 or start > len(arr) - 1:
            return 'Invalid start value.'
        for num in arr:
            if num < 0 or num > len(arr) - 1:
                return 'Invalid value in arr.'

        toCrawl = [start]
        crawled = []

        while toCrawl:
            curr = toCrawl.pop()

            if arr[curr] == 0:
                return True

            if curr not in crawled:
                if -1 < curr + arr[curr] < len(arr):
                    toCrawl.append(curr + arr[curr])
                if -1 < curr - arr[curr] < len(arr):
                    toCrawl.append(curr - arr[curr])
                crawled.append(curr)

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
