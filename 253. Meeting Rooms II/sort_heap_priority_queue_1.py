import heapq

class Solution:

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # using sort and heap priority queue
        # sort the array based on start time
        # push end time of interval which occupies free room to heap
        # maintain heap of end time of meeting
        # time: O(N.log N) to sort and to push N elements, 1 element takes log N time to push/pop
        # space: O(N)
        # from solution given in leetcode

        # sort intervals based on start time
        intervals.sort(key = lambda x: x[0])

        freerooms = [] # init heap

        #add first interval's end time to heap
        heapq.heappush(freerooms, intervals[0][1])

        for i in intervals[1:]:
            if i[0] >= freerooms[0]: # do not use < and push condition because we want to pop only to replace
                heapq.heappop(freerooms)
            heapq.heappush(freerooms, i[1])

        #print(freerooms)
        return len(freerooms)

"""input = [[1,10],[2,7],[3, 19], [8, 12], [10, 20],[11, 30]]
output = 4"""
