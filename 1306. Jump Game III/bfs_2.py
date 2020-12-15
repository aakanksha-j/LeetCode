class Solution:
    """Approach 2: BFS and make value of array negative so that in future
                   we can continue for that condition.
       Time complexity: O(n)
       Space complexity: O(n) for crawled list
       Runtime: 216 ms
       Memory: 20.8 MB
    """
    def canReach(self, arr, start) -> bool:
        n = len(arr)
        q = [start]

        while q:
            node = q.pop(0)

            if arr[node] == 0: # check if reached zero
                return True

            if arr[node] < 0:
                continue

            for i in [node + arr[node], node - arr[node]]: # check available next steps
                if 0 <= i < n:
                    q.append(i)
            arr[node] = -arr[node] # mark as visited

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
