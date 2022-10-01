class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        # leetcode solution - sweep line, one pass
        
        # time: O(N) for traversing the list
        # space: O(1) without considering O(N) space for output list
        
        output = []
        remove_start, remove_end = toBeRemoved
        for start, end in intervals:
            if (end <= remove_start) or (remove_end <= start):
                output.append([start, end])
            else:
                if (start < remove_start):
                    output.append([start, remove_start])
                if (remove_end < end):
                    output.append([remove_end, end])
        return output
            