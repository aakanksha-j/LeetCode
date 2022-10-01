# github python link - https://github.com/mission-peace/interview/blob/master/python/geometry/skylinedrawing.py
# tushar roy video - https://www.youtube.com/watch?v=GSBLe8cKu0s&t=867s&ab_channel=TusharRoy-CodingMadeSimple

# build list of object to store points in sorted order according to (point, height, is_start)
# sort based on 3 edge cases: 1. both start at one point, keep higher height before smaller
# by negating both (h2 before h1) 2. both end at same point, h1 before h2 3. one start, one 
# end at same point, (start before end - make start negative)
# sort the list
# create queue and result, initialize queue with key - height 0, value - 1
# go through the list to add values to the result
# add values to the queue from list
# if start object, save height as key and increase count by 1.
# if end object, decrease count by 1 for that height
# add to result whenever max curr height changes.
# use prev and curr variables to keep track of highest key in queue

# time: O(NlogN) - add, delete and finding max take logN 
# space: O(logN) 

class BuildingPoint(object):
    def __init__(self, point, height, is_start):
        self.point = point
        self.height = height
        self.is_start = is_start

    def __lt__(self, other): # less than https://blog.finxter.com/python-__lt__-magic-method/
        if self.point != other.point:
            return self.point < other.point
        else:
            if self.is_start:
                h1 = -self.height
            else:
                h1 = self.height
            if other.is_start:
                h2 = -other.height
            else:
                h2 = other.height
        return h1 < h2
    
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        building_points = []
        for building in buildings:
            building_points.append(BuildingPoint(building[0], building[2], True))
            building_points.append(BuildingPoint(building[1], building[2], False))
        building_points.sort()
        
        queue, result = {}, []
        queue[0] = 1
        prev_max_height = 0
        
        for building_point in building_points:
            if building_point.is_start:
                if building_point.height in queue:
                    queue[building_point.height] += 1
                else:
                    queue[building_point.height] = 1
            else:
                if queue[building_point.height] == 1:
                    del queue[building_point.height]
                else:
                    queue[building_point.height] -= 1
                    
            curr_max_height = max(queue.keys())
            if curr_max_height != prev_max_height:
                result.append([building_point.point, curr_max_height])
                prev_max_height = curr_max_height
            
        return result
        

if __name__ == '__main__':
    buildings = [[1, 3, 4], [3, 4, 4], [2, 6, 2], [8, 11, 4], [7, 9, 3], [10, 11, 2]]
    print(get_skyline(buildings))