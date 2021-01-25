class Solution:
    """Approach 1: https://leetcode.com/problems/magnetic-force-between-two-balls/discuss/794070/PythonC%2B%2B-Binary-search-solution-with-explanation-and-similar-questions
       Time complexity: O(NlogM) where M = max(position) - min(position)
       Space complexity: O(1)
       Runtime: 1452 ms
       Memory: 28.1 MB
    """
    def maxDistance(self, position, m: int) -> int:
        n = len(position)
        position.sort()

        def count(d):
            ans, curr = 1, position[0]
            for i in range(1, n):
                if position[i] - curr >= d:
                    ans += 1
                    curr = position[i]
            return ans

        l, r = 0, position[-1] - position[0]
        while l < r:
            mid = r - (r - l) // 2
            if count(mid) >= m:
                l = mid
            else:
                r = mid - 1
        return l

def main():
    numbers =[1,2,3,4,7]
    m = 3
    s=Solution()
    print(s.maxDistance(numbers, m))
    numbers =[5,4,3,2,1,10000]
    m = 2
    print(s.maxDistance(numbers, m))

if __name__ == '__main__':
    main()
