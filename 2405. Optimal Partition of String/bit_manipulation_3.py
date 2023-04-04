# bit manipulation 

# O(N) time O(1) space

class Solution:
    def partitionString(self, s: str) -> int:
        partitions = 1 # start with 1 as all characters might be unique and entire word is 1 partition
        flag = 0 # this is z..ba = 0..00
        partition_start = 0
        for index in range(len(s)):
            val = ord(s[index]) - ord('a')
            if flag & (1 << val):
                partitions += 1
                flag = 0
            flag |= 1 << val # in-place or
            #print(flag)
        return partitions