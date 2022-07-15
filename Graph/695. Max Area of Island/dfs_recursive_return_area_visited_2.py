class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # dfs recursive with visited (extra space for set)

        m,n = len(grid), len(grid[0])
        area, visited = 0, set()

        def dfs(r, c):
            # we only want to pass the count, so
            # no need to pass grid as we only check for value 0 which remains constant
            # and visited set keeps getting the new sets
            if r < 0 or r == m or c < 0 or c == n or grid[r][c] == 0 or (r,c) in visited:
                return 0

            visited.add((r,c)) # (r,c) if written as add(r,c) then considers as 2 arguments

            # 1 because we need to add current coordinate to the sum, not added before dfs function
            return (1 + dfs(r + 1, c) +
                        dfs(r - 1, c) +
                        dfs(r, c + 1) +
                        dfs(r, c - 1))

        for r in range(m):
            for c in range(n):
                area = max(area, dfs(r,c))

        return area

"""     time O(mn)
        space O(mn)
        https://www.youtube.com/watch?v=iJGr1OtmH0c&ab_channel=NeetCode
"""
