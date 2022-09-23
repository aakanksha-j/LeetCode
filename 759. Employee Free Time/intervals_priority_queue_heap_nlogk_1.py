"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    # https://leetcode.com/problems/employee-free-time/discuss/170551/Simple-Python-9-liner-beats-97-(with-explanation) - in comments section by user9051k
    # why heap/ priority queue? as we want the smallest interval.start first
    # time: O(N log k) - N intervals, k employees, in heap - creating heap is N time as it is binary tree, adding elements is log N time, we add initially to the heap, only the first element of k employees, 
    # space: O(log N) - for adding to the recursion
    
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # use heap/priority queue (question similar to merge intervals) to merge k lists of sorted intervals O(Nlogk)
        # while merging track the previous interval pre
        # if pre does not overlap with curr, we found a gap and append it. Else, we update pre.end
        res = []
        pq = []
        
        for i, employee in enumerate(schedule):
            first_interval_of_this_employee = employee[0]
            heappush(pq, (first_interval_of_this_employee.start, i, 0)) 
            # append to the heap in format (start_of_first_interval_of_each_employee, employee_no, interval_index)
            #heap will sort based on first value in tuple i.e interval.start 
            
        pre = None
        while pq:
            # pop the interval with next smallest start time
            _, employee_index, interval_index = heappop(pq)
            interval = schedule[employee_index][interval_index]
            #print(interval.start, interval.end)
            
            # construct res
            if not pre:
                pre = interval
            elif pre.end < interval.start:
                #print(pre.start, pre.end, interval.start)
                res.append(Interval(pre.end, interval.start)) # mistake: appended list instead of Interval object
                pre = interval # mistake: forgot
            else:
                pre.end = max(pre.end, interval.end)
            
            # get the next interval from the corresponding employee if any left
            if interval_index < len(schedule[employee_index]) - 1:
                next_interval = schedule[employee_index][interval_index + 1]
                heappush(pq, (next_interval.start, employee_index, interval_index + 1))
                
        return res
                