class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # https://leetcode.com/problems/insert-interval/discuss/21809/Python-O(n)-and-O(nlgn)-solutions.
        # neetcode solution 
        
        # time: O(N) - iterate over every element in intervals array
				# not in-place, can use given property that input is sorted
        # space: O(N) - for output 
        
        output = []
        for i in range(len(intervals)):
            # first two cases no overlap
            if newInterval[1] < intervals[i][0]:
                output.append(newInterval)
                return output + intervals[i:] # can return earlier
            elif intervals[i][1] < newInterval[0]:
                output.append(intervals[i])  
            else: # overlap cases
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
                # not added to output because can overlap with next interval too, therefore keep updating
                
        # if newInterval not added from first case, add at the end of for loop
        output.append(newInterval)
        
        return output
                
        
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # https://leetcode.com/problems/insert-interval/discuss/21809/Python-O(n)-and-O(nlgn)-solutions.
        
        # same as merge intervals, not in-place solution
        # add the newInterval to intervals array, sort the intervals array
        # add to output when not overlapping, update last value of output when overlapping
        
        # time: O(NlogN) - due to sorting
        # space: O(N) - for output 
        
        output = []
        intervals.append(newInterval)
        intervals.sort(key = lambda x: x[0])
        print(intervals)
        for i in range(len(intervals)):
            if output and output[-1][1] >= intervals[i][0]:
                output[-1][1] = max(intervals[i][1], output[-1][1])
            else:
                output.append(intervals[i])
        return output
        
           
                
        
        
        
           
                
        