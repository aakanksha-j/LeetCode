class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # create hashmap
        hashmap = {ch: [] for ch in s}
        for i, ch in enumerate(s):
            hashmap[ch].append(i)
        print(hashmap)
        
        # create intervals
        intervals = []
        for ch in hashmap:
            intervals.append([hashmap[ch][0], hashmap[ch][-1]])
        print(intervals)
        
        # merge intervals and add their size as output
        #intervals.sort(key =  lambda x: (x[0], x[1])) # no need to sort as python dictionary builds intervals while scanning the string from left, as we keep the dictionary with each char and its min/max index and then create a list from those, the intervals will be ordered.
        
        merged_intervals = [intervals[0]]
        for i in range(len(intervals) - 1):
            if merged_intervals[-1][1] < intervals[i + 1][0]:
                merged_intervals.append(intervals[i+1])
            else:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], intervals[i + 1][1])
                
        output = []
        for start, end in merged_intervals:
            output.append(end - start + 1)
        return output
            