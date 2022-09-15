class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Graph sum - after 200. number of islands
        # dfs recursive neetcode solution

        m,n = len(heights), len(heights[0])
        pac, atl = set(), set() # writing just () wont do, it will be considered as tuple instead of set

        def dfs(row, col, prevheight, visit):
            # value of current height should be more than prevheight so that water from ocean can move and cross to another ocean.
            if row < 0 or row >= m or col < 0 or col >= n or prevheight > heights[row][col] or (row, col) in visit: # remember to test if present in visit sets
                return

            visit.add((row, col)) # add to atl or pac visited sets

            # for pac set, increase column, increase row
            dfs(row, col + 1, heights[row][col], visit)
            dfs(row + 1, col, heights[row][col], visit)
            # for atl set, decrease column, decrease row
            dfs(row, col - 1, heights[row][col], visit)
            dfs(row - 1, col, heights[row][col], visit)

        for c in range(n):
            dfs(0, c, heights[0][c], pac)
            dfs(m-1, c, heights[m-1][c], atl)
        for r in range(m):
            dfs(r, 0, heights[r][0], pac)
            dfs(r, n-1, heights[r][n-1], atl)

        # find overlapping coordinates from both pac and atl sets
        res = []
        for i in range(m):
            for j in range(n):
                if (i,j) in pac and (i,j) in atl: # remember to compare set (i,j) not heights[i][j]
                    res.append([i,j])

        return res

"""     time O(mn)
        space O(mn)
        https://www.youtube.com/watch?v=s-VkcjHqkGI&t=417s&ab_channel=NeetCode
"""
