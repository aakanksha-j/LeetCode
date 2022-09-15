class Solution:
    def removeCoveredIntervals(self, intervals) -> int:
        # Array and sorting - solved after 253 meeting rooms, 56 merge intervals

        count = 0 # do not count if covered eg. [1,16], [1,10] or [2,8]
        prev_end = 0


        # sort by start time as key. If start time is same, sort by end time in reverse
        # Interval with longer time will be before shorter end time.
        intervals.sort(key = lambda x: (x[0], -x[1])) # eg. [1,10], [1,16]


        # for loop to count non-covered intervals
        for start, end in intervals:
            #print(start, end)

            if end > prev_end: # eg. [1,10] or [2,11] or [11,30]
                count += 1
                prev_end = end

        return count

def main():
    numbers = [[1,5], [10,15]]
    s=Solution()
    print(s.removeCoveredIntervals(numbers))
    numbers = [[1,4], [2,3]]
    print(s.removeCoveredIntervals(numbers))
    numbers = [[1,10], [1,16]]
    print(s.removeCoveredIntervals(numbers))
    numbers = [[1,4],[3,6],[2,8]]
    print(s.removeCoveredIntervals(numbers))



if __name__ == '__main__':
    main()
