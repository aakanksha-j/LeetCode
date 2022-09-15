class Solution:
    # https://leetcode.com/problems/max-points-on-a-line/discuss/47113/A-java-solution-with-notes

    # 5 use cases: horizontal line (dy = 0, key = 'dx_0'),
    # vertical line (dx = 0, key = '0_dy'),
    # parallel line (take max of current slope's points from a particular starting point),
    # n < 3,
    # slope is negative

    # time: O(n^2) - 2 nested for loops
    # space: O(n) for hashmap

    # get gcd
    def getGcd(self, a, b):
        if a == 0: return b
        return self.getGcd(b % a, a)

    def maxPoints(self, points: List[List[int]]) -> int:
        v, res, n = 0, 0, len(points)
        if n < 3: return n # two points form a line

        for i in range(n - res):
            hashmap = {}
            x1, y1 = points[i][0], points[i][1]
            max_v, duplicates = 0, 0 # current problem does not have duplicates, but if introduced in future

            for j in range(i + 1, n):
                x2, y2 = points[j][0], points[j][1]
                dx, dy = x2 - x1, y2 - y1 # slope = dy/dx, float rounds up so string as key

                if dx == 0 and dy == 0:
                    duplicates += 1
                else:
                    gcd = self.getGcd(dx, dy)
                    dx, dy = dx // gcd, dy // gcd

                    #if dx < 0: # to keep consistent representation, keep delta_x always positive
                    #    dx , dy = -1 * dx, -1 * dy

                    key = str(dx) + '_' + str(dy)
                    hashmap[key] = hashmap.get(key, 0) + 1
                    v = hashmap[key]

                max_v = max(max_v, v)
                res = max(res, duplicates + max_v + 1) # 1 is for starting point

        return res
