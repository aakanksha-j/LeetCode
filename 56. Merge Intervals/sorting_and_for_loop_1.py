class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # done after meeting rooms, comes in array and sorting category
        # sort using start as key and then compare end time of output with the next interval's start, followed by end
        #[[1,10],[2,7],[3,19],[8,12],[10,20],[11,30]] output [1,30]


        intervals.sort(key = lambda x: x[0])

        output = [intervals[0]]

        for i in range(len(intervals) - 1):
            if output[-1][1] < intervals[i+1][0]: # eg. [1,6], [7,14] - output has both intervals as there is no overlap
                output.append(intervals[i+1])
            else:
                if output[-1][1] <= intervals[i+1][1]: # eg. [1,7], [6,14] - output is [1,14] merge the overlapping intervals
                    output[-1][1] = intervals[i+1][1] # output[-1][1] because we have to check the last value in output, not the last interval as it may have been skipped eg. [1,10],[2,7] output [1,10]

        return output
