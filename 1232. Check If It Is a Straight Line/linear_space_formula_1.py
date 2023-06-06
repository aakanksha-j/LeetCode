"""
1232. Check If It Is a Straight Line
Easy
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

Example 1:



Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
Example 2:



Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false
 

Constraints:

2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.
"""

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # time O(N)
        # space O(1)
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        if x2 - x1 == 0: # slope inf, parallel to y-axis
            for x, y in coordinates[2:]:
                if x - x1 != 0:
                    return False
            return True
        if y2 - y1 == 0: # slope 0, parallel to x-axis
            for x, y in coordinates[2:]:
                if y - y1 != 0:
                    return False
            return True
        slope = (y2 - y1) / (x2 - x1)
        prev = slope
        for point in coordinates[2:]:
            x, y = point
            if y - y1 == 0 or x - x1 == 0:
                return False
            slope = (y - y1) / (x - x1)
            if prev != slope:
                return False
        return True
    
# shorter version 
# (x0, y0), (x1, y1) = coordinates[:2]
# for point in coordinates[2:]:
#     x, y = point
#     if (x - x0) * (y1 - y0) != (y - y0) * (x1 - x0):
#         return False
# return True
