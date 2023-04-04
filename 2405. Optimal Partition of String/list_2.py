class Solution:
    def partitionString(self, s: str) -> int:
        partitions = 1 # start with 1 as all characters might be unique
        last_seen_list = [-1]*26
        partition_start = 0
        for index in range(len(s)):
            if last_seen_list[ord(s[index]) - ord('a')] >= partition_start :
                partitions += 1
                partition_start = index
            last_seen_list[ord(s[index]) - ord('a')] = index
        return partitions
    
# time O(n)
# space O(26)